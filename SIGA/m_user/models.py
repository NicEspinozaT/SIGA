from django.db.models import (
    Model,
    IntegerField,
    CharField,
    DateField,
    EmailField,
    ForeignKey,
    CASCADE,
)

lista_generos = [
    [0, "Femenino"],
    [1, "Masculino"],
    [2, "No aplica"],
]


class TipoUsuario(Model):
    tipo = CharField(max_length=15)

    class Meta:
        db_table = "Tipo_usuario"

    def __str__(self):
        return {self.tipo}


class Usuario(Model):
    num_rut = IntegerField(primary_key=True)
    dv = CharField(max_length=1)
    pnombre = CharField(max_length=30)
    snombre = CharField(max_length=30, blank=True, null=True)
    appat = CharField(max_length=30)
    apmat = CharField(max_length=30)
    fec_nac = DateField()
    nacionalidad = CharField(max_length=20)
    direccion = CharField(max_length=100)
    genero = CharField(max_length=9, choices=lista_generos)
    email = EmailField(unique=True)
    numero = IntegerField()

    class Meta:
        db_table = "Usuario"

    def __str__(self):
        return f"{self.num_rut}-{self.dv}"


class Apoderado(Model):
    tipo = ForeignKey(TipoUsuario, on_delete=CASCADE)
    usuario = ForeignKey(Usuario, on_delete=CASCADE)

    class Meta:
        db_table = "Apoderado"

    def __str__(self):
        return f"{self.usuario.num_rut}-{self.usuario.dv}"


class Estudiante(Model):
    tipo = ForeignKey(TipoUsuario, on_delete=CASCADE)
    usuario = ForeignKey(Usuario, on_delete=CASCADE)
    Apoderado = ForeignKey(Apoderado, on_delete=CASCADE)
    parentezco = CharField(max_length=10)

    class Meta:
        db_table = "Estudiante"

    def __str__(self):
        return f"{self.usuario.num_rut}-{self.usuario.dv}"
