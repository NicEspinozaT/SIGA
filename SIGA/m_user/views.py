from django.shortcuts import render

def login(request):
  return render(request, "user/login.html")

def vistaAlumno(request):
  return render (request, "user/alumno/vistaAlumno.html")

def vistaApoderado(request):
  return render (request, "user/apoderado/vistaApoderado.html")

def vistaDocente(request):
  return render (request, "user/docente/vistaDocente.html")

def perfilDocente(request):
  return render (request, "user/docente/perfil.html")
