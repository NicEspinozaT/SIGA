from django.shortcuts import render
from m_user.models import Docente, Apoderado, Estudiante


# Vista Admin


def vista_admin(request):
    return render(request, "vista_admin.html")


def admin_login(request):
    return render(request, "admin_login.html")


# CRUD DOCENTE
def listar_Docente(request):
    return render(request, "vista_admin.html")


# CRUD ESTUDIANTE


def listar_Apoderado(request):
    apoderado = Apoderado.objects.all()
    return render(request, "listar_apoderado.html", {"apoderado": apoderado})


# CRUD Apoderado
def listar_Estudiante(request):
    estudiante = Estudiante.objects.all()
    return render(request, "listar_estudiante.html", {"estudiante": estudiante})
