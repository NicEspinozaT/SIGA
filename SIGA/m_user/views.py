from django.shortcuts import render


def login(request):
    return render(request, "login.html")


def vistaAlumno(request):
    return render(request, "alumno/vistaAlumno.html")


def vistaApoderado(request):
    return render(request, "apoderado/vistaApoderado.html")


def vistaDocente(request):
    return render(request, "docente/vistaDocente.html")


def perfilDocente(request):
    return render(request, "docente/perfil.html")


def solicitar_contraseña(request):
    return render(request, "solicitarContraseña.html")


def vistaAdmin(request):
    return render(request, "admin/admin.html")
