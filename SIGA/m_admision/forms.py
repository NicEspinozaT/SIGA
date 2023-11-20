from django.forms import (
    ModelForm,
    NumberInput,
    Select,
    TextInput,
    DateInput,
    EmailInput,
)
from .models import Apoderado, Estudiante, Matricula


class FormularioApoderado(ModelForm):
    class Meta:
        model = Apoderado
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
        }



class FormularioEstudiante(ModelForm):
    apoderado_rut = TextInput(attrs={"class":"form-control", "readonly":True})
    class Meta:
        model = Estudiante
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
            "parentezco",
            "apoderado_rut",
        ]
        widgets = {
            "num_rut": NumberInput(
                attrs={"class": "form-control", "placeholder": "Sin puntos ni guión"}
            ),
            "dv": TextInput(
                attrs={"class": "form-control"}
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
                attrs={
                    "class": "form-control", 
                    "type":"date"
                }
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
            "parentezco": TextInput(
                attrs={"class":"form-control"}
            ),
            "apoderado_rut": Select(
                attrs={"class":"form-control", "readonly":True}
            ),
        }


class FormularioMatricula(ModelForm):
    class Meta:
        model = Matricula
        fields = [
            "estado",
            "periodo",
            "apoderado",
            "estudiante",
        ]
        widgets = {
            "estado": Select(
                attrs={"class":"form-control"}
            ),
            "periodo": NumberInput(
                attrs={"class":"form-control"}
            ),
            "apoderado": TextInput(
                attrs={"class":"form-control"}
            ),
            "estudiante": TextInput(
                attrs={"class":"form-control"}
            ),
        }
