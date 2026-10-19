from django.http import HttpResponse
from django.shortcuts import render
from .models import Aprendiz

def listar_aprendices(request):
    aprendices = Aprendiz.objects.all()

    contexto = {
        'aprendices': aprendices
    }

    return render (request, 'prueba/index.html', contexto)
