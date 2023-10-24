from django.shortcuts import render


def mostrar_inicio(request):
    return render(request, "hijo/inicio.html")


def mostrar_contacto(request):
    return render(request, "hijo/contacto.html")


def mostrar_nosotros(request):
    return render(request, "hijo/sobre-nosotros.html")


def login(reques):
    return render(reques, "hijo/login.html")


def matricula(reques):
    return render(reques, "hijo/matricula.html")
