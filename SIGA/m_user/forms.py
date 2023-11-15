from django.forms import (
    Form,
    EmailField,
    EmailInput,
    CharField,
    PasswordInput,
    BooleanField,
    CheckboxInput,
    TextInput,
)
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class FormularioEntrar(Form):
    usuario = CharField(
        min_length=1,
        max_length=16,
        required=True,
        label="RUT:",
        widget=TextInput(
            attrs={"class": "form-control", "placeholder": "Nombre de usuario"}
        ),
    )
    contrasenia_usuario = CharField(
        required=True,
        min_length=4,
        max_length=16,
        label="Contraseña",
        widget=PasswordInput(
            attrs={"class": "form-control", "placeholder": "Password"}
        ),
    )
    recuerdame = BooleanField(
        required=False, label="Recordarme", widget=CheckboxInput()
    )


class FormularioRegistro(UserCreationForm):
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
        self.fields["password1"].widget.attrs = {"class": "form-control"}
        self.fields["password2"].widget.attrs = {"class": "form-control"}

    class Meta:
        model = User
        fields = [
            "username",
            "last_name",
            "first_name",
            "email",
            "password1",
            "password2",
        ]

        widgets = {
            "username": TextInput(attrs={"class": "form-control"}),
            "last_name": TextInput(attrs={"class": "form-control"}),
            "first_name": TextInput(attrs={"class": "form-control"}),
            "email": EmailInput(attrs={"class": "form-control"}),
        }