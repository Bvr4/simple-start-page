from django.http import HttpResponse
from django.shortcuts import render
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
    id_ligne = escape(request.POST.get("id-ligne"))
    ligne = Ligne.objects.get(ligne_id=id_ligne)
    emplacement_max = Lien.objects.filter(id_ligne=id_ligne).aggregate(Max('emplacement'))
    
    lien = Lien.objects.create(nom=nom, 
                               url=url, 
                               id_ligne=ligne, 
                               emplacement=emplacement_max['emplacement__max'] + 1
                               )
    
    return render(request, 'startpage/lien.html', context={'lien': lien})
