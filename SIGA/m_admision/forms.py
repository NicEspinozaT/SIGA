from django.forms import (
  ModelForm,
  NumberInput,
  Select,
  TextInput,
  DateInput,
  EmailInput,
  CheckboxInput
)
from .models import (
  Matricula,
  Apoderado,
  Estudiante,
)

class FormularioApoderado(ModelForm):
  class Meta:
    model = Apoderado
    fields = [
      "num_run",
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
      "num_run": NumberInput(
        attrs = {
        "class":"form-control",
        "placeholder":"Ingrese rut sin puntos ni guión"
      }),
      "dv" : TextInput(
        attrs={
          "class" : "form-control"
      }),
      "pnombre" : TextInput,
      "snombre" : TextInput,
      "appat" : TextInput,
      "apmat" : TextInput,
      "fec_nac" : DateInput,
      "nacionalidad" : TextInput,
      "direccion" : TextInput,
      "genero" : Select,
      "email" : EmailInput,
      "numero" : NumberInput,
    }