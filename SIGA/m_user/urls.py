from django.urls import path
from .views import login, vistaAlumno, vistaApoderado, vistaDocente

urlpatterns = [
  path("login/", login, name="login"),
  path("alumno/", vistaAlumno, name="alumno"),
  path("apoderado/", vistaApoderado, name="apoderado"),
  path("docente/", vistaDocente, name="docente")
  
]