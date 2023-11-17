from django.db.models import (
    Model,
    IntegerField,
    CharField,
    DateField,
    EmailField,
    ForeignKey,
    CASCADE,
)
from django.core.validators import MinLengthValidator, MaxLengthValidator
import secrets
import string
from django.core.mail import send_mail

lista_generos = [
    [0, "Femenino"],
    [1, "Masculino"],
    [2, "No aplica"],
]


### Tabla Apoderado
class Apoderado(Model):
    num_rut = IntegerField(primary_key=True)
    dv = CharField(max_length=1)
    contrasenia = CharField(max_length=128, null=True, blank=True)
    pnombre = CharField(max_length=30)
    snombre = CharField(max_length=30, blank=True, null=True)
    appat = CharField(max_length=30)
    apmat = CharField(max_length=30)
    fec_nac = DateField()
    nacionalidad = CharField(max_length=20)
    direccion = CharField(max_length=100)
    genero = IntegerField(choices=lista_generos)
    email = EmailField(unique=True)
    numero = IntegerField()

    class Meta:
        db_table = "Apoderado"

    def save(self, *args, **kwargs):
        if not self.contrasenia:  # Si es un nuevo registro
            pass_usuario = self.generar_contrasenia_aleatoria()
            # send_mail(
            #     "Holiiii!!! Tu pass es: ",
            #     f"{pass_usuario}",
            #     "nicolasespinoza1985@gmail.com",
            #     [self.email],
            #     fail_silently=False,
            # )

            self.contrasenia = pass_usuario
        super().save(*args, **kwargs)

    @staticmethod
    def generar_contrasenia_aleatoria(longitud=8):
        caracteres = string.ascii_letters + string.digits
        return "".join(secrets.choice(caracteres) for _ in range(longitud))

    def __str__(self):
        return f"{self.num_rut}-{self.dv} {self.pnombre} {self.appat} {self.apmat}"


### Tabla Estudiante
class Estudiante(Model):
    num_rut = IntegerField(primary_key=True)
    dv = CharField(max_length=1)
    contrasenia = CharField(max_length=8)
    apoderado = ForeignKey(Apoderado, on_delete=CASCADE)
    pnombre = CharField(max_length=30)
    snombre = CharField(max_length=30, blank=True, null=True)
    appat = CharField(max_length=30)
    apmat = CharField(max_length=30)
    fec_nac = DateField()
    nacionalidad = CharField(max_length=20)
    direccion = CharField(max_length=100)
    genero = IntegerField(choices=lista_generos)
    email = EmailField(unique=True)
    numero = IntegerField()
    parentezco = CharField(max_length=10)

    class Meta:
        db_table = "Estudiante"

    def save(self, *args, **kwargs):
        if not self.pk:  # Si es un nuevo registro
            self.contrasenia = self.generar_contrasenia_aleatoria()
        super().save(*args, **kwargs)

    @staticmethod
    def generar_contrasenia_aleatoria(longitud=8):
        caracteres = string.ascii_letters + string.digits
        return "".join(secrets.choice(caracteres) for _ in range(longitud))

    def __str__(self):
        return f"{self.num_rut}-{self.dv} {self.pnombre} {self.appat} {self.apmat}"
