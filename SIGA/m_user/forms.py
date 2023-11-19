from django.forms import (
    ChoiceField,
    Form,
    EmailField,
    EmailInput,
    CharField,
    ModelForm,
    PasswordInput,
    BooleanField,
    CheckboxInput,
    TextInput,
    IntegerField,
    NumberInput,
    DateInput,
    Select,
)
from django.contrib.auth.forms import UserCreationForm
from .models import Apoderado, lista_generos


class LoginForm(Form):
    num_rut = IntegerField(
        label="RUT:",
        required=True,
        min_value=1000000,
        max_value=99999999,
        help_text="Sin puntos ni digito verificador",
        widget=NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "ej: 12345678",
            }
        ),
    )
    contrasenia = CharField(
        label="Contraseña",
        widget=PasswordInput(attrs={"class": "form-control"}),
    )
    recuerdame = BooleanField(
        required=False, label="Recordarme", widget=CheckboxInput()
    )
