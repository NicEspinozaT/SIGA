from django.urls import path
from .views import admision, registrar_apoderado, registrar_estudiante, registrar_matricula

urlpatterns = [
    path("admision/", admision, name="admision"),
    path("admision/matricula/", registrar_apoderado, name="matricula"),
    path("admision/matricula/registrar_estudiante", registrar_estudiante, name="registroEstudiante"),
    path("admision/matricula/registrar_apoderado", registrar_apoderado, name="registrarApoderado"),
    path("admision/matricula/registrar_matricula", registrar_matricula, name="registroMatricula"),
]
