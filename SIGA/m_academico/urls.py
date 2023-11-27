from django.urls import path
from .views import (
    listar_cursos,
    agregar_curso,
    lista_asignaturas,
    agregar_asignatura,
    modificar_curso,
    eliminar_curso,
)

urlpatterns = [
    # CURSO
    path("cursos/", listar_cursos, name="cursos"),
    path("cursos/agregar", agregar_curso, name="agregar_curso"),
    path("cursos/modificar/<int:pk>/", modificar_curso, name="modificar_curso"),
    path("cursos/eliminar/<int:pk>/", eliminar_curso, name="eliminar_curso"),
    # ASIGNATURA
    path(
        "cursos/asignaturas/<int:curso_id>", lista_asignaturas, name="lista_asignaturas"
    ),
    path(
        "cursos/asignaturas/<int:curso_id>/agregar",
        agregar_asignatura,
        name="agregar_asignatura",
    ),
]
