from django.db.models import (
    Model,
    IntegerField,
    CharField,
    DateField,
    EmailField,
    ForeignKey,
    BigAutoField,
    CASCADE,
)
from django.core.validators import MinLengthValidator, MaxLengthValidator

lista_generos = [
    [0, "Femenino"],
    [1, "Masculino"],
    [2, "No aplica"],
]


### Tabla Usuario
class Usuario(Model):
    id_usuario = BigAutoField(primary_key=True)

    class Meta:
        db_table = "Usuario"

    def __str__(self):
        return f"{self.id_usuario}"


### Tabla Apoderado
class Apoderado(Model):
    num_rut = IntegerField(primary_key=True)
    dv = CharField(max_length=1)
    usuario = ForeignKey(Usuario, on_delete=CASCADE, null=True, blank=True)
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
        if not self.usuario:
            usuario = Usuario.objects.create()
            self.usuario = usuario
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.num_rut}-{self.dv} {self.pnombre} {self.appat} {self.apmat}"


### Tabla Estudiante
class Estudiante(Model):
    num_rut = IntegerField(primary_key=True)
    dv = CharField(max_length=1)
    usuario = ForeignKey(Usuario, on_delete=CASCADE, null=True, blank=True)
    Apoderado = ForeignKey(Apoderado, on_delete=CASCADE)
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
        if not self.usuario:
            usuario = Usuario.objects.create()
            self.usuario = usuario
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.num_rut}-{self.dv} {self.pnombre} {self.appat} {self.apmat}"
