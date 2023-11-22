from django.urls import path
from .views import admision, registrar_apoderado, registrar_estudiante, registrar_matricula,buscar_apoderado,buscar_estudiante

urlpatterns = [
    path("admision/", admision, name="admision"),
    path("admision/matricula/", buscar_apoderado, name="matricula"),
    path("admision/matricula/registrar_estudiante", registrar_estudiante, name="registroEstudiante"),
    path("admision/matricula/buscar_apoderado", buscar_apoderado, name="buscarApoderado"),
    path("admision/matricula/registrar_apoderado", registrar_apoderado, name="registrarApoderado"),
    path("admision/matricula/buscar_estudiante", buscar_estudiante, name="buscarEstudiante"),
    path("admision/matricula/registrar_matricula", registrar_matricula, name="registroMatricula"),
]
