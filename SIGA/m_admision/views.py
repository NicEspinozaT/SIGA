from django.shortcuts import render, redirect
from .forms import FormularioApoderado, FormularioEstudiante
from sweetify import success, warning
from .models import Apoderado


def admision(request):
    return render(request, "admision.html")



def registrar_apoderado(request):
    if request.method == "GET":
        contexto = {
            "titulo":"Formulario Apoderado",
            "form_apoderado":FormularioApoderado()
        }
        request.session['datos_apoderado_guardados'] = False
        return render(request, "matricula.html", contexto)
    
    if request.method == "POST":
        datos_apoderado = FormularioApoderado(data=request.POST)
        validar = datos_apoderado.is_valid()
        if validar:
            request.session['temp_datos_apoderado'] = datos_apoderado.cleaned_data
            request.session['datos_apoderado_guardados'] = False
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
        datos_apoderado_temp = request.session.get('temp_datos_apoderado', {})
        contexto = {
            "titulo":"Formulario Estudiante",
            "form_estudiante":FormularioEstudiante(),
            "num_rut_apod":datos_apoderado_temp,
        }
        return render(request, "matricula.html", contexto)
    
    if request.method == "POST":
        datos_estudiante = FormularioEstudiante(data=request.POST)
        datos_apoderado_temp = request.session.get('temp_datos_apoderado', {}) # Traer el apoderado guardado
        datos_apoderado_guardados = request.session.get('datos_apoderado_guardados', False) # Para validar si el apoderado existe
        validar = datos_estudiante.is_valid()
        if validar:
            if not datos_apoderado_guardados:
                Apoderado.objects.create(**datos_apoderado_temp)
                request.session['datos_apoderado_guardados'] = True
            datos_estudiante.save()
            success(
                request,
                "Registrado correctamente",
                text="Gracias por ser parte de nuestra institución",
                timer=1000,
                button="OK",
            )
            request.session.pop('temp_datos_apoderado', None)
            request.session.pop('datos_apoderado_guardados', None)
            return redirect("mostrar_inicio")
        contexto = {"form_estudiante": datos_estudiante}
        warning(
            request,
            "Datos no válidos",
            text="Observe el formulario y valide sus datos",
            button="Ok",
        )
        return render(request,"matricula.html",contexto)


