from django.forms import (
    ModelForm,
    Select,
    TextInput,
    NumberInput,
    Textarea,
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
        fields = [
            "nombre", 
            "sigla",
            "cursos",
            "docentes",
        ]
        widgets = {
            "nombre": Select(
                attrs={"class":"form-control"}
            ),
            "sigla": Select(
                attrs={"class":"form-control"}
            ),
            "cursos": Select(
                attrs={"class":"form-control"}
            ),
            "docentes": Select(
                attrs={"class":"form-control"}
            )
        }


class EvaluacionForm(ModelForm):
    class Meta:
        model = EvaluacionPlanificada
        fields = [
            "nombre",
            "descripcion",
            "ponderacion",
            "asignatura",
            "curso",
        ]
        widgets = {
            "nombre": TextInput(
                attrs={"class":"form-control"}
            ),
            "descripcion": Textarea(
                attrs={"class":"form-control"}
            ),
            "ponderacion": NumberInput(
                attrs={
                    "class":"form-control",
                    "step":"0.1"
                }
            ),
            "asignatura": Select(
                attrs={"class":"form-control"}
            ),
            "curso": Select(
                attrs={"class":"form-control"}
            ),
        }
