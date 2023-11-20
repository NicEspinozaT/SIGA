from django.forms import (
    ModelForm,
    Select,
    
)
from .models import Curso, Asignatura, lista_nivel, lista_seccion, EvaluacionPlanificada


class CursoForm(ModelForm):
    class Meta:
        model = Curso
        fields = [
            "nivel",
            "seccion",
        ]
        widgets = {
            "nivel": Select(attrs={"class": "form-control"}),
            "seccion": Select(attrs={"class": "form-control"}),
        }


class AsignaturaForm(ModelForm):
    class Meta:
        model = Asignatura
        fields = ["nombre", "sigla", "docentes"]  # Excluye 'cursos'
        

class EvaluacionForm(ModelForm):
    class Meta:
        model = EvaluacionPlanificada
        fields = ['titulo', 'descripcion', 'fecha']
