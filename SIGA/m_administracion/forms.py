from django.forms import (
    Form,
    EmailField,
    CharField,
    PasswordInput,
)


class LoginFormAdmin(Form):
    correo_electronico = EmailField(label="Correo Electrónico")
    contrasenia = CharField(widget=PasswordInput, label="Contraseña")
