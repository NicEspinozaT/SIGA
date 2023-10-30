from django.shortcuts import render


def mostrar_inicio(request):
    return render(request, "home/inicio.html")


def mostrar_contacto(request):
    return render(request, "informacion/contacto.html")


def mostrar_nosotros(request):
    return render(request, "informacion/sobre_nosotros.html")


def matricula(request):
    return render(request, "matricula/matricula.html")
