from django.shortcuts import render, redirect
from .forms import FormularioApoderado, FormularioEstudiante
from sweetify import success, warning


def admision(request):
    return render(request, "admision.html")



def registrar_apoderado(request):
    if request.method == "POST":
        form = FormularioApoderado(request.POST)
        if form.is_valid():
            form.save()
            return redirect("mostrar_inicio")
    else:
        form = FormularioApoderado()

    return render(request, "matricula.html", {"form": form})


def registrar_estudiante(request):
    if request.method == "GET":
        contexto = {
            "titulo":"Formulario Estudiante",
            "formulario":FormularioEstudiante()
        }
        return render(render, "matricula.html", contexto)
    
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