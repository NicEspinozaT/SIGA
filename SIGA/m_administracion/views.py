from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from django.contrib.auth import login
from sweetify import success, warning

from m_user.models import Docente, Apoderado, Estudiante
from .models import Administrador
from .forms import LoginFormAdmin

# Vista Admin


def admin_login(request):
    if request.method == "POST":
        form = LoginFormAdmin(request.POST)
        if form.is_valid():
            correo_electronico = form.cleaned_data["correo_electronico"]
            contrasenia1 = form.cleaned_data["contrasenia"]

            user = None
            tipo_usuario = None

            try:
                user = Administrador.objects.get(correo_electronico=correo_electronico)
                tipo_usuario = "administrador"
            except Administrador.DoesNotExist:
                user = None

            if user and check_password(contrasenia1, user.contrasenia1):
                request.session["tipo_usuario"] = tipo_usuario
                user.backend = "SIGA.backends.CustomAuthAdmin"
                login(request, user)
                # Redirigir a la página de inicio del administrador
                success(
                    request,
                    "Registrado correctamente",
                    text="Gracias por ser parte",
                    timer=3000,
                    button="OK",
                )
                return redirect("vista_admin")
            else:
                # Manejar el error de inicio de sesión
                form.add_error(None, "Correo electrónico o contraseña incorrectos")
        warning(
            request,
            "Ups...",
            text="Observer el formulario y valide sus datos",
            timer=3000,
            button="OK",
        )

    else:
        form = LoginFormAdmin()

    return render(request, "admin_login.html", {"form": form})


def vista_admin(request):
    return render(request, "vista_admin.html")


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
