from django.urls import path
from .views import registrar_docente,admin_login, vista_admin, listar_docentes, listar_apoderados, eliminar_apoderado, modificar_docente, modificar_apoderado, eliminar_docente, listar_estudiantes, eliminar_estudiante, modificar_estudiante

urlpatterns = [
    path('admin_login/', admin_login, name='admin_login'),
    path("vista_admin/", vista_admin, name="vista_admin"),
    # URLS DOCENTE
    path("registrar_docente/", registrar_docente, name="registrarDocente"),
    path("listar_docentes/", listar_docentes, name="listar_docentes"),
    path('docente/modificar/<int:pk>/', modificar_docente, name='modificar_docente'),
    path("eliminar_docente/<int:pk>", eliminar_docente, name="eliminar_docente"),
    #URLS APODERADO
    path("listar_apoderados/", listar_apoderados, name="listar_apoderados"),
    path("eliminar_apoderado/<int:pk>", eliminar_apoderado, name="eliminar_apoderado"),
    path("modificar_apoderado/<int:pk>", modificar_apoderado, name="modificar_apoderado"),
    #URLS ESTUDIANTE
    path("listar_estudiantes/", listar_estudiantes, name="listar_estudiantes"),
    path("eliminar_estudiante/<int:pk>", eliminar_estudiante, name="eliminar_estudiante"),
    path("modificar_estudiante/<int:pk>", modificar_estudiante, name="modificar_estudiante"),
]
