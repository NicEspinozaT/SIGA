from django.shortcuts import render, redirect
from m_user.models import Docente, Apoderado, Estudiante
from django.contrib.auth import login
from django.contrib.auth.hashers import check_password
from .models import Administrador
from .forms import FormularioDocente, LoginFormAdmin
from sweetify import success, warning, error


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



# CRUD ESTUDIANTE


def listar_Apoderado(request):
    apoderado = Apoderado.objects.all()
    return render(request, "listar_apoderado.html", {"apoderado": apoderado})


# CRUD Apoderado
def listar_Estudiante(request):
    estudiante = Estudiante.objects.all()
    return render(request, "listar_estudiante.html", {"estudiante": estudiante})

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