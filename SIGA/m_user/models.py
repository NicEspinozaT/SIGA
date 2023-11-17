from django.db.models import (
    Model,
    IntegerField,
    CharField,
    DateField,
    EmailField,
    ForeignKey,
    BigAutoField,
    CASCADE,
    OneToOneField
)
from django.core.validators import MaxValueValidator, MaxLengthValidator, MinLengthValidator, MinValueValidator
from django.utils import timezone
### Para darle validaciones propias al método clean
from django.core.exceptions import ValidationError

lista_generos = [
    [0, "Femenino"],
    [1, "Masculino"],
    [2, "No aplica"],
]


### Tabla Apoderado
class Apoderado(Model):
    num_rut = IntegerField(primary_key=True,validators=[MaxValueValidator(49999999), MinValueValidator(10000000)])
    dv = CharField(max_length=1, null=False)
    pnombre = CharField(max_length=30, null=False)
    snombre = CharField(max_length=30, blank=True, null=True)
    appat = CharField(max_length=30, null=False)
    apmat = CharField(max_length=30, null=False)
    fec_nac = DateField(validators=[MaxValueValidator(limit_value=timezone.now().date())])
    nacionalidad = CharField(max_length=20)
    direccion = CharField(max_length=100)
    genero = IntegerField(choices=lista_generos)
    email = EmailField(unique=True, null=False)
    numero = IntegerField(null=False)

    class Meta:
        db_table = "Apoderado"

    def __str__(self):
        return f"{self.num_rut}-{self.dv} {self.pnombre} {self.appat} {self.apmat}"


### Tabla Estudiante
class Estudiante(Model):
    num_rut = IntegerField(primary_key=True, validators=[MaxValueValidator(49999999), MinValueValidator(10000000)])
    dv = CharField(max_length=1)
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
    apoderado = ForeignKey(Apoderado, on_delete=CASCADE)

    class Meta:
        db_table = "Estudiante"

    def __str__(self):
        return f"{self.num_rut}-{self.dv} {self.pnombre} {self.appat} {self.apmat} {self.apoderado.num_rut}"


### Tabla Usuario
class Usuario(Model):
    id_usuario = BigAutoField(primary_key=True)
    contraseña = CharField(max_length=12)
    apoderado = OneToOneField(Apoderado, on_delete=CASCADE, related_name='usuario_apoderado', related_query_name='usuario_apoderado', null=True, blank=True)
    estudiante = OneToOneField(Estudiante, on_delete=CASCADE, related_name='usuario_estudiante', related_query_name='usuario_estudiante', null=True, blank=True)

    class Meta:
        db_table = "Usuario"

    def __str__(self):
        if self.apoderado:
            nombre = self.apoderado.pnombre
        elif self.estudiante:
            nombre = self.estudiante.pnombre
        else:
            nombre = "Usuario sin asociar a Apoderado o Estudiante"

        return f"{self.id_usuario} {nombre}"
    
    ### método modificado para las validaciones de las foreing keys de usuario
    def clean(self):
        if not self.apoderado and not self.estudiante:
            raise ValidationError('Debe asociar un Apoderado o un Estudiante al usuario.')
        if self.apoderado and self.estudiante:
            raise ValidationError('Sólo puede asociar un Apoderado o un Estudiante al usuario.')