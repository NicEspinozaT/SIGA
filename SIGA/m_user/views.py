from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.hashers import check_password
from .forms import LoginForm
from .models import Apoderado, Estudiante, Docente
from sweetify import success, warning
from SIGA.backends import CustomAuthUser


def vista_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            num_rut = form.cleaned_data["num_rut"]
            contrasenia = form.cleaned_data["contrasenia"]

            user = None
            tipo_usuario = None

            # Busca en Apoderado
            try:
                user = Apoderado.objects.get(num_rut=num_rut)
                tipo_usuario = "apoderado"
            except Apoderado.DoesNotExist:
                # Continúa buscando en otros modelos si no encuentra en Apoderado
                pass

            # Si no se encuentra en Apoderado, busca en Estudiante
            if not user:
                try:
                    user = Estudiante.objects.get(num_rut=num_rut)
                    tipo_usuario = "estudiante"
                except Estudiante.DoesNotExist:
                    # Continúa buscando en otros modelos si no encuentra en Estudiante
                    pass

            # Si no se encuentra en Estudiante, busca en Docente
            if not user:
                try:
                    user = Docente.objects.get(num_rut=num_rut)
                    tipo_usuario = "docente"
                except Docente.DoesNotExist:
                    # Usuario no encontrado en ningún modelo
                    pass

            # Verifica la contraseña y maneja el inicio de sesión
            if user and check_password(contrasenia, user.contrasenia):
                # Establece la sesión y realiza el inicio de sesión
                request.session["tipo_usuario"] = tipo_usuario
                request.session["usuario_autenticado"] = True
                user.backend = "SIGA.backends.CustomAuthUser"
                login(request, user)
                success(request, "Sesión iniciada correctamente", text=":)", timer=3000, button="OK")
                
                # Redirige según el tipo de usuario
                if tipo_usuario == "estudiante":
                    return redirect("alumno")
                elif tipo_usuario == "apoderado":
                    return redirect("apoderado")
                elif tipo_usuario == "docente":
                    return redirect("docente")
            else:
                # Contraseña incorrecta o usuario no encontrado
                warning(request, "Número de RUT o contraseña incorrectos", button="OK")
        else:
            # Formulario no válido
            warning(request, "Ups...", text="Observer el formulario y valide sus datos", timer=3000, button="OK")

    else:
        # GET request
        form = LoginForm()

    return render(request, "login.html", {"form": form})


def logout_view(request):
    # Limpiar la sesión
    request.session.flush()

    # Opcionalmente, puedes hacer logout para limpiar cualquier dato adicional
    # que Django maneja en la sesión (si estás utilizando partes del sistema de autenticación de Django)
    logout(request)
    success(
        request,
        "Sesión cerrada correctamente!",
        text="Vuelve pronto",
        timer=3000,
        button="OK",
    )

    # Redirigir al usuario a la página de inicio o de login
    return redirect("mostrar_inicio")


def vistaAlumno(request):
    return render(request, "alumno/vistaAlumno.html")


def vistaApoderado(request):
    return render(request, "apoderado/vistaApoderado.html")


def vistaDocente(request):
    return render(request, "docente/vistaDocente.html")


def perfilDocente(request):
    return render(request, "docente/perfil.html")


def solicitar_contraseña(request):
    return render(request, "solicitarContraseña.html")


def vistaAdmin(request):
    return render(request, "admin/admin.html")
