from django.shortcuts import render, redirect
from .forms import FormularioApoderado, FormularioEstudiante
from sweetify import success, warning


def admision(request):
    return render(request, "admision.html")



def registrar_apoderado(request):
    if request.method == "GET":
        contexto = {
            "titulo":"Formulario Apoderado",
            "form_apoderado":FormularioApoderado()
        }
        return render(request, "matricula.html", contexto)
    
    if request.method == "POST":
        datos_apoderado = FormularioApoderado(data=request.POST)
        validar = datos_apoderado.is_valid()
        if validar:
            datos_apoderado.save()
            success(
                request,
                "Registrado correctamente",
                text="Siga al siguiente formulario",
                timer=1000,
                button="Siguiente"
            )
            return redirect("mostrar_inicio")
        contexto = {"form_apoderado":datos_apoderado}
        warning(
            request,
            "Datos no válidos",
            text="Observe el formulario y valide sus datos",
            button="Ok",
        )
        return render(request,"matricula.html",contexto)


def registrar_estudiante(request):
    if request.method == "GET":
        contexto = {
            "titulo":"Formulario Estudiante",
            "form_estudiante":FormularioEstudiante()
        }
        return render(request, "matricula.html", contexto)
    
    if request.method == "POST":
        datos_estudiante = FormularioEstudiante(data=request.POST)
        validar = datos_estudiante.is_valid()
        if validar:
            datos_estudiante.save()
            success(
                request,
                "Registrado correctamente",
                text="Gracias por ser parte de nuestra institución",
                timer=1000,
                button="OK",
            )
            return redirect("mostrar_inicio")
        contexto = {"form_estudiante": datos_estudiante}
        warning(
            request,
            "Datos no válidos",
            text="Observe el formulario y valide sus datos",
            button="Ok",
        )
        return render(request,"matricula.html",contexto)


