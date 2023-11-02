from django.urls import path
from .views import (
    login,
    vistaAlumno,
    vistaApoderado,
    vistaDocente,
    perfilDocente,
    solicitar_contraseña,
    vistaAdmin,
)

urlpatterns = [
    path("login/", login, name="login"),
    path("solicitar_contraseña/", solicitar_contraseña, name="solicitarContraseña"),
    path("alumno/", vistaAlumno, name="alumno"),
    path("apoderado/", vistaApoderado, name="apoderado"),
    path("docente/", vistaDocente, name="docente"),
    path("perfil_docente/", perfilDocente, name="perfil_docente"),
    path("vistaAdmin/", vistaAdmin, name="administrador"),
]
