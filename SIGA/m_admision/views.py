from django.shortcuts import render, redirect
from .forms import (
    FormularioApoderado, 
    FormularioEstudiante, 
    FormularioMatricula
)
from sweetify import success, warning
from .models import Apoderado, Estudiante


def admision(request):
    return render(request, "admision.html")


## Buscar Apoderado
def buscar_apoderado(request):
    if request.method == 'POST':
        num_rut = request.POST.get('rut') 
        try:
            ap_exist = Apoderado.objects.get(num_rut=num_rut)
            request.session['rut_apoderado'] = num_rut  
            return redirect('buscarEstudiante')
            
        except: 
            return redirect('registrarApoderado') 
             
       
            
    return render(request, 'buscar_apoderado.html')  

### Formulario Apoderado
def registrar_apoderado(request):
    if request.method == "GET":
        contexto = {
            "titulo": "Formulario Apoderado",
            "form_apoderado": FormularioApoderado()
        }
        return render(request, "formulario_apoderado.html", contexto)

    if request.method == "POST":
        datos_apoderado = FormularioApoderado(data=request.POST)
        validar = datos_apoderado.is_valid()
        if validar:
            datos_apoderado.save()
            success(
                request,
                "Registrado correctamente",
                text="Siga al siguiente formulario",
                timer=2000,
                button="Siguiente"
            )
            return redirect("buscarEstudiante")
        contexto = {"form_apoderado": datos_apoderado}
        warning(
            request,
            "Datos no válidos",
            text="Observe el formulario y valide sus datos",
            button="Ok",
        )
        return render(request, "formulario_apoderado.html", contexto)
    
## Buscar Estudiante
def buscar_estudiante(request):
    if request.method == 'POST':
        num_rut = request.POST.get('rut') 
        try:
            ap_exist = Estudiante.objects.get(num_rut=num_rut)
            request.session['rut_estudiante'] = num_rut  
            return redirect('registroMatricula')
            
        except: 
            return redirect('registroEstudiante') 
             
       
            
    return render(request, 'buscar_estudiante.html')  


### Formulario Estudiante
def registrar_estudiante(request):
    
    apoderados = Apoderado.objects.all()
    if request.method == "GET":
        contexto = {
            "titulo": "Formulario Estudiante",
            "form_estudiante": FormularioEstudiante(),
            "apoderados": apoderados,
        }
        return render(request, "formulario_estudiante.html", contexto)

    if request.method == "POST":
        datos_estudiante = FormularioEstudiante(data=request.POST)
        validar = datos_estudiante.is_valid()
        if validar:
            datos_estudiante.save()
            success(
                request,
                "Registrado correctamente",
                text="Siga al siguiente formulario",
                timer=2000,
                button="Siguiente"
            )
            return redirect("registroMatricula")
        contexto = {"form_estudiante": datos_estudiante}
        warning(
            request,
            "Datos no válidos",
            text="Observe el formulario y valide sus datos",
            button="Ok",
        )
        return render(request, "formulario_estudiante.html", contexto)


def registrar_matricula(request):
    apoderados = Apoderado.objects.all()
    estudiantes = Estudiante.objects.all()
    if request.method == "GET":
        contexto = {
            "titulo": "Formulario Matrícula",
            "form_matricula": FormularioMatricula(),
            "apoderados": apoderados,
            "estudiantes":estudiantes,
        }
        return render(request, "formulario_matricula.html", contexto)
    
    if request.method == "POST":
        datos_matricula = FormularioMatricula(data=request.POST)
        validar = datos_matricula.is_valid()
        if validar:
            datos_matricula.save()
            success(
                request,
                "Matricula completada",
                text="Gracias por ser parte de nuestra institución",
                timer=2000,
                button="Listo",
            )
            return redirect("mostrar_inicio")
        contexto = {"form_matricula": datos_matricula}
        warning(
            request,
            "Datos no válidos",
            text="Observe el formulario y valide sus datos",
            button="Ok",
        )
        return render(request, "formulario_matricula.html", contexto)






'''
### Formulario Apoderado
def registrar_apoderado(request):
    if request.method == "GET":
        contexto = {
            "titulo": "Formulario Apoderado",
            "form_apoderado": FormularioApoderado()
        }
        request.session['datos_apoderado_guardados'] = False
        return render(request, "matricula.html", contexto)

    if request.method == "POST":
        datos_apoderado = FormularioApoderado(data=request.POST)
        validar = datos_apoderado.is_valid()
        if validar:
            # Convertir la fecha a cadena antes de guardarla en la sesión
            datos_apoderado_cleaned = datos_apoderado.cleaned_data
            datos_apoderado_cleaned['fec_nac'] = str(datos_apoderado_cleaned['fec_nac'])

            request.session['temp_datos_apoderado'] = datos_apoderado_cleaned
            request.session['datos_apoderado_guardados'] = False
            success(
                request,
                "Registrado correctamente",
                text="Siga al siguiente formulario",
                timer=1000,
                button="Siguiente"
            )
            return redirect("registroEstudiante")
        contexto = {"form_apoderado": datos_apoderado}
        warning(
            request,
            "Datos no válidos",
            text="Observe el formulario y valide sus datos",
            button="Ok",
        )
        return render(request, "matricula.html", contexto)
'''