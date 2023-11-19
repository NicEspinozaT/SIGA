from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.hashers import check_password
from .forms import LoginForm
from .models import Apoderado, Estudiante
from sweetify import success


def vista_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            num_rut = form.cleaned_data["num_rut"]
            contrasenia = form.cleaned_data["contrasenia"]

            # Busca en Apoderado
            try:
                user = Apoderado.objects.get(num_rut=num_rut)
            except Apoderado.DoesNotExist:
                user = None

            # Si no se encuentra en Apoderado, busca en Estudiante
            if not user:
                try:
                    user = Estudiante.objects.get(num_rut=num_rut)
                except Estudiante.DoesNotExist:
                    user = None

            # Verifica la contraseña
            if user and check_password(contrasenia, user.contrasenia):
                login(request, user)
                success(request, f"Bienvenido {user.pnombre} {user.appat}")
                return redirect("mostrar_inicio")
            else:
                form.add_error(None, "Número de RUT o contraseña incorrectos.")
    else:
        form = LoginForm()

    return render(request, "login.html", {"form": form})


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
