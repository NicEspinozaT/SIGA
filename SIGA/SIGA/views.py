from django.shortcuts import render


def mostrar_inicio(request):
    return render(request, "hijo/inicio.html")

def mostrar_contacto(request):
    return render(request, "hijo/contacto.html")

def mostrar_nosotros(request):
    return render(request, "hijo/sobre-nosotros.html")
