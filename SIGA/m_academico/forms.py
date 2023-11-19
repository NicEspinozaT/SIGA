from django.forms import (
    ModelForm,
    Select,
)
from .models import Curso, lista_nivel, lista_seccion


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
