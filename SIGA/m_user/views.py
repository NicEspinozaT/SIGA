from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.hashers import check_password, make_password
from .forms import LoginForm
from .models import Apoderado, Estudiante, Docente
from sweetify import success, warning
from django.core.mail import send_mail


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
                user = None

            # Si no se encuentra en Apoderado, busca en Estudiante
            if not user:
                try:
                    user = Estudiante.objects.get(num_rut=num_rut)
                    tipo_usuario = "estudiante"
                except Estudiante.DoesNotExist:
                    user = None

            # Si no se encuentra en Estudiante, busca en Docente
            if not user:
                try:
                    user = Docente.objects.get(num_rut=num_rut)
                    tipo_usuario = "docente"
                except Docente.DoesNotExist:
                    user = None

            # Verifica la contraseña
            if user and check_password(contrasenia, user.contrasenia):
                request.session["tipo_usuario"] = tipo_usuario
                user.backend = "SIGA.backends.CustomAuthUser"
                login(request, user)
                success(
                    request,
                    "Registrado correctamente",
                    text="Gracias por ser parte",
                    timer=3000,
                    button="OK",
                )
                return redirect("mostrar_inicio")
            else:
                form.add_error(None, "Número de RUT o contraseña incorrectos.")
        warning(
            request,
            "Ups...",
            text="Observer el formulario y valide sus datos",
            timer=3000,
            button="OK",
        )

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
    if request.method == 'POST':
        rut = request.POST.get('rut')
        usuario = None
        
        # Busca el usuario en las tablas correspondientes
        for model in [Apoderado, Estudiante, Docente]:
            usuario = model.objects.filter(num_rut=rut).first()
            if usuario:
                break
        
        if usuario:
            nueva_contrasena = Apoderado.generar_contrasenia_aleatoria()
            usuario.contrasenia = make_password(nueva_contrasena)
            usuario.save()
            send_mail(
                "Restablecimiento de contraseña sistema SIGA",
                f"Tu nueva contraseña es: {nueva_contrasena}",
                "siga.educacion@gmail.com",
                [usuario.email],
                fail_silently=False,
            )
            success(
                request,
                "Solicitud realizada",
                text="Hemos enviado a tú correo la nueva contraseña",
                timer=20000,
                button="Siguiente"
            )
            return redirect('login')
        else:
            # Manejar el caso de que no se encuentre el usuario
            pass
    return render(request, "solicitarContraseña.html")


def vistaAdmin(request):
    return render(request, "admin/admin.html")
