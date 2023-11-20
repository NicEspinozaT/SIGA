from django.forms import (
    DateInput,
    EmailInput,
    ModelForm,
    NumberInput,
    Select,
    TextInput
)
from m_user.models import Docente

class FormularioDocente(ModelForm):
    class Meta:
        model = Docente
        fields = [
            "num_rut",
            "dv",
            "pnombre",
            "snombre",
            "appat",
            "apmat",
            "fec_nac",
            "nacionalidad",
            "direccion",
            "genero",
            "email",
            "numero",
            "especialidad",
            "fecha_contrato",
        ]
        widgets = {
"num_rut": NumberInput(
                attrs={"class": "form-control", "placeholder": "Sin puntos ni guión"}
            ),
            "dv": TextInput(attrs={"class": "form-control"}
            ),
            "pnombre": TextInput(
                attrs={"class": "form-control", "placeholder": "Primer nombre"}
            ),
            "snombre": TextInput(
                attrs={"class": "form-control", "placeholder": "Segundo nombre"}
            ),
            "appat": TextInput(
                attrs={"class": "form-control", "placeholder": "Apellido paterno"}
            ),
            "apmat": TextInput(
                attrs={"class": "form-control", "placeholder": "Apellido materno"}
            ),
            "fec_nac": DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "nacionalidad": TextInput(
                attrs={"class": "form-control"}
            ),
            "direccion": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "ej: Calle Esparta 25, comuna La Granja",
                }
            ),
            "genero": Select(
                attrs={"class": "form-control"}
            ),
            "email": EmailInput(
                attrs={"class": "form-control", "placeholder": "example@gmail.com"}
            ),
            "numero": NumberInput(
                attrs={"class": "form-control"}
            ),
            "especialidad": Select(
                attrs={"class":"form-control"}
            ),
            "fecha_contrato": DateInput(
                attrs={"class":"form-control"}
            ),
        }