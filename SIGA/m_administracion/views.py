from django.shortcuts import render, redirect
from m_user.models import Docente, Apoderado, Estudiante
from .forms import FormularioDocente
from sweetify import success, warning


def registrar_docente(request):
    if request.method == "GET":
        contexto = {
            "titulo":"Formulario Docente",
            "form_docente":FormularioDocente()
        }
        return render(request, "registro_docente.html", contexto)
    
    if request.method == "POST":
        datos_docente = FormularioDocente(data=request.POST)
        validar = datos_docente.is_valid()
        if validar:
            datos_docente.save()
            success(
                request,
                "Registrado correctamente",
                text="Se a ingresado al docente con exito.",
                timer=2000,
                button="OK"
            )
            return redirect("mostrar_inicio")
        contexto = {"form_docente":datos_docente}
        warning(
            request,
            "Datos no válidos",
            text="Observe el formulario y valide sus datos",
            button="Ok",
        )
        return render(request,"registro_docente.html",contexto)

# CRUD DOCENTE
def listar_Docente(request):
    return render(request, "listar_docentes.html")


# CRUD ESTUDIANTE


def listar_Apoderado(request):
    apoderado = Apoderado.objects.all()
    return render(request, "listar_apoderado.html", {"apoderado": apoderado})


# CRUD Apoderado
def listar_Estudiante(request):
    estudiante = Estudiante.objects.all()
    return render(request, "listar_estudiante.html", {"estudiante": estudiante})
