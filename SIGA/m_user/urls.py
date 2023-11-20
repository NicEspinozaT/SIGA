from django.urls import path
from .views import (
    vista_login,
    vistaAlumno,
    vistaApoderado,
    vistaDocente,
    perfilDocente,
    solicitar_contraseña,
    vistaAdmin,
    logout_view,
)

urlpatterns = [
    path("login/", vista_login, name="login"),
    path("logout/", logout_view, name="logout"),
    path("solicitar_contraseña/", solicitar_contraseña, name="solicitarContraseña"),
    path("alumno/", vistaAlumno, name="alumno"),
    path("apoderado/", vistaApoderado, name="apoderado"),
    path("docente/", vistaDocente, name="docente"),
    path("perfil_docente/", perfilDocente, name="perfil_docente"),
    path("vistaAdmin/", vistaAdmin, name="administrador"),
]
