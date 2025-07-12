from django.shortcuts import render
from .utils import datos_sistema

def dashboard(request):
    contexto = datos_sistema()
    return render(request, 'sistema/index.html', contexto)
