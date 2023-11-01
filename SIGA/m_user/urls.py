from django.urls import path
from .views import login, vistaAlumno, vistaApoderado, vistaDocente, perfilDocente

urlpatterns = [
    path("login/", login, name="login"),
    path("alumno/", vistaAlumno, name="alumno"),
    path("apoderado/", vistaApoderado, name="apoderado"),
    path("docente/", vistaDocente, name="docente"),
    path("perfil_docente/", perfilDocente, name="perfil_docente"),
]
