from django.shortcuts import render
from m_user.models import Docente, Apoderado, Estudiante


# CRUD DOCENTE
def listar_Docente(request):
    docente = Docente.objects.all()
    return render(request, "listar_docente.html", {"docente": docente})


# CRUD ESTUDIANTE


def listar_Apoderado(request):
    apoderado = Apoderado.objects.all()
    return render(request, "listar_apoderado.html", {"apoderado": apoderado})


# CRUD Apoderado
def listar_Estudiante(request):
    estudiante = Estudiante.objects.all()
    return render(request, "listar_estudiante.html", {"estudiante": estudiante})
