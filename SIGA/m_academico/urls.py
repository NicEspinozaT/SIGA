from django.urls import path
from .views import listar_cursos, agregar_curso, lista_asignaturas, agregar_asignatura

urlpatterns = [
    path("cursos/", listar_cursos, name="cursos"),
    path("cursos/agregar", agregar_curso, name="agregar_curso"),
    path(
        "cursos/asignaturas/<int:curso_id>", lista_asignaturas, name="lista_asignaturas"
    ),
    path(
        "cursos/asignaturas/<int:curso_id>/agregar",
        agregar_asignatura,
        name="agregar_asignatura",
    ),
]
