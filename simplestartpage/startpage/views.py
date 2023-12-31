from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.html import escape
from django.db.models import Max

from startpage.models import Ligne, Lien

def index(request):
    context = {}
    context["lignes"] = Ligne.objects.order_by('emplacement')
    return render(request, 'startpage/index.html', context=context)


def add_ligne(request):
    # On cherche la valeur maximale de l'emplacement enregistré en base
    emplacement_max = Ligne.objects.aggregate(Max('emplacement'))
    ligne = Ligne.objects.create(emplacement=emplacement_max['emplacement__max'] + 1)
    return render(request, 'startpage/ligne.html', context={'ligne': ligne})


def add_lien(request):
    nom = escape(request.POST.get("nom-lien"))
    url = escape(request.POST.get("url-lien"))
    if nom == '' or url == '':
        return HttpResponse('Veuillez renseigner un nom et une URL pour le lien', status=400)
    
    id_ligne = escape(request.POST.get("id-ligne"))
    ligne = Ligne.objects.get(ligne_id=id_ligne)
    emplacement_max = Lien.objects.filter(id_ligne=id_ligne).aggregate(Max('emplacement'))

    # Si la ligne est vide, on initialise l'emplacement à 0
    if emplacement_max['emplacement__max'] is None:
        emplacement = 0
    else:
        emplacement = emplacement_max['emplacement__max'] + 1
    
    lien = Lien.objects.create(nom=nom, 
                               url=url, 
                               id_ligne=ligne, 
                               emplacement=emplacement
                               )
    
    return render(request, 'startpage/lien.html', context={'lien': lien})


def delete_lien(request, lien_pk):
    lien = get_object_or_404(Lien, pk=lien_pk)
    lien.delete()

    return HttpResponse("")


def delete_ligne(request, ligne_pk):
    ligne = get_object_or_404(Ligne, pk=ligne_pk)
    ligne.delete()

    return HttpResponse("")


def move_lien_up(request, lien_pk):
    # On récupère l'enregistrement du lien en question
    lien = Lien.objects.get(pk=lien_pk)

    # On récupère l'enregistrement ayant l'emplacement juste au dessus
    lien_sup = Lien.objects.filter(id_ligne=lien.id_ligne).order_by("-emplacement").filter(emplacement__lt = lien.emplacement)[0]

    lien.emplacement, lien_sup.emplacement = lien_sup.emplacement, lien.emplacement
    lien.save()
    lien_sup.save()

    ligne = Ligne.objects.get(pk=lien.id_ligne_id)

    # On retourne toute la ligne mise à jour. (peut être moyen de faire mieux ?)
    return render(request, 'startpage/ligne.html', context={'ligne': ligne})


def move_lien_down(request, lien_pk):
    # On récupère l'enregistrement du lien en question
    lien = Lien.objects.get(pk=lien_pk)

    # On récupère l'enregistrement ayant l'emplacement juste en dessous
    lien_sup = Lien.objects.filter(id_ligne=lien.id_ligne).order_by("emplacement").filter(emplacement__gt = lien.emplacement)[0]

    lien.emplacement, lien_sup.emplacement = lien_sup.emplacement, lien.emplacement
    lien.save()
    lien_sup.save()

    ligne = Ligne.objects.get(pk=lien.id_ligne_id)

    # On retourne toute la ligne mise à jour. (peut être moyen de faire mieux ?)
    return render(request, 'startpage/ligne.html', context={'ligne': ligne})


def move_ligne_up(request, ligne_pk):
    # On récupère l'enregistrement du ligne en question
    ligne = Ligne.objects.get(pk=ligne_pk)

    # On récupère l'enregistrement ayant l'emplacement juste au dessus
    ligne_sup = Ligne.objects.order_by("-emplacement").filter(emplacement__lt = ligne.emplacement)[0]

    ligne.emplacement, ligne_sup.emplacement = ligne_sup.emplacement, ligne.emplacement
    ligne.save()
    ligne_sup.save()

    # On raffraichit la page. (peut être moyen de faire mieux ?)
    return redirect('home')


def move_ligne_down(request, ligne_pk):
    # On récupère l'enregistrement du ligne en question
    ligne = Ligne.objects.get(pk=ligne_pk)

    # On récupère l'enregistrement ayant l'emplacement juste en dessous
    ligne_sup = Ligne.objects.order_by("emplacement").filter(emplacement__gt = ligne.emplacement)[0]

    ligne.emplacement, ligne_sup.emplacement = ligne_sup.emplacement, ligne.emplacement
    ligne.save()
    ligne_sup.save()

    # On raffraichit la page. (peut être moyen de faire mieux ?)
    return redirect('home')


def edit_lien_form(request, lien_pk):
    lien = Lien.objects.get(pk=lien_pk)
    return render(request, 'startpage/edit-lien-form.html', context={'lien': lien})


def lien(request, lien_pk):
    lien = Lien.objects.get(pk=lien_pk)
        
    # Si méthode est POST, on met à jour l'enregistrement, sinon (methode GET) on retourne sans mettre à jour
    if request.method == 'POST':
        lien.nom = escape(request.POST.get("nom-lien"))
        lien.url = escape(request.POST.get("url-lien"))
        lien.save()

    return render(request, 'startpage/lien.html', context={'lien': lien})


def add_lien_form(request, ligne_pk):
    ligne = Ligne.objects.get(pk=ligne_pk)
    return render(request, 'startpage/add-lien-form.html', context={'ligne': ligne})


def add_lien_ctrl(request, ligne_pk):
    ligne = Ligne.objects.get(pk=ligne_pk)
    return render(request, 'startpage/add-lien-ctrl.html', context={'ligne': ligne})