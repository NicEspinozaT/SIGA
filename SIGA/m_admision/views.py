from django.shortcuts import render

def admision(request):
  return render (request, 'admision.html')

def matricula(request):
  return render(request, "matricula.html")