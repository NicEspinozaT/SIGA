from django.shortcuts import render,redirect
from .forms import FormularioApoderado
from sweetify import success, warning

def admision(request):
  return render (request, 'admision.html')

def matricula(request):
  if request.method == "GET":
    contexto = {"titulo":"Formulario apoderado","form_apod":FormularioApoderado()}
    return render(request, "matricula.html", contexto)
  
