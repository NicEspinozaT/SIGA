from django.urls import path
from .views import listar_cursos, agregar_curso

urlpatterns = [
    path("listar_cursos/", listar_cursos, name="cursos"),
    path("cursos/agregar", agregar_curso, name="agregar_curso"),
]

