from django.shortcuts import render

from startpage.models import Ligne, Lien

def index(request):
    context = {}

    context["lignes"] = Ligne.objects.order_by('emplacement')

    return render(request, 'startpage/index.html', context=context)