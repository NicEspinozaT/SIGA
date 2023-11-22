from django.shortcuts import render, redirect, get_object_or_404
from m_user.models import Docente, Apoderado, Estudiante
from django.contrib.auth import login
from django.contrib.auth.hashers import check_password
from .models import Administrador
from .forms import FormularioDocente, LoginFormAdmin
from sweetify import success, warning, error
from m_admision.forms import FormularioApoderado, FormularioEstudiante


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
def listar_docentes(request):
    docentes = Docente.objects.all()  # Obtiene todos los docentes
    return render(request, "listar_docentes.html", {"docentes": docentes})

def modificar_docente(request, pk):
    docente = get_object_or_404(Docente, pk=pk)
    if request.method == "POST":
        form = FormularioDocente(request.POST, instance=docente)
        if form.is_valid():
            form.save()
            # Mensaje de éxito y redirección
            return redirect('listar_docentes')
    else:
        form = FormularioDocente(instance=docente)
    return render(request, 'registro_docente.html', {'form_docente': form})

def eliminar_docente(request, pk):
    docente = Docente.objects.filter(pk=pk)
    docente.delete()
    return redirect("listar_docentes")



# CRUD APODERADO
def listar_apoderados(request):
    apoderados = Apoderado.objects.all()
    return render(request, "listar_apoderados.html", {"apoderado": apoderados})

def modificar_apoderado(request, pk):
    apoderado = get_object_or_404(Apoderado, pk=pk)
    if request.method == "POST":
        form = FormularioApoderado(request.POST, instance=apoderado)
        if form.is_valid():
            form.save()
            return redirect('listar_apoderados')
    else:
        form = FormularioApoderado(instance=apoderado)
    return render(request, 'formulario_apoderado.html', {'form_apoderado': form})

def eliminar_apoderado(request, pk):
    apoderado = Apoderado.objects.filter(pk=pk)
    apoderado.delete()
    return redirect("listar_apoderados")



# CRUD ESTUDIANTE
def listar_estudiantes(request):
    estudiante = Estudiante.objects.all()
    return render(request, "listar_estudiantes.html", {"estudiante": estudiante})

def modificar_estudiante(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    if request.method == "POST":
        form = FormularioEstudiante(request.POST, instance=estudiante)
        if form.is_valid():
            form.save()
            return redirect('listar_estudiantes')
    else:
        form = FormularioEstudiante(instance=estudiante)
    return render(request, 'formulario_estudiante.html', {'form_estudiante': form})

def eliminar_estudiante(request, pk):
    estudiante = Estudiante.objects.filter(pk=pk)
    estudiante.delete()
    return redirect("listar_estudiantes")



def vista_admin(request):
    return render(request, "vista_admin.html")

def admin_login(request):
    if request.method == 'POST':
        form = LoginFormAdmin(request.POST)
        if form.is_valid():
            correo_electronico = form.cleaned_data['correo_electronico']
            contrasenia = form.cleaned_data['contrasenia']

            try:
                administrador = Administrador.objects.get(correo_electronico=correo_electronico)
                if check_password(contrasenia, administrador.contrasenia1):
                    request.session["tipo_usuario"] = "administrador"
                    # Aquí puedes manejar la sesión del administrador
                    # Por ejemplo, puedes usar el sistema de autenticación de Django
                    # login(request, administrador)
                    success(request, 'Inicio de sesión exitoso')
                    return redirect('vista_admin')
                else:
                    error(request, 'Contraseña incorrecta')
            except Administrador.DoesNotExist:
                error(request, 'Administrador no encontrado')
    else:
        form = LoginFormAdmin()

    return render(request, 'admin_login.html', {'form': form})

