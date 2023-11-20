from django.db.models import (
    Model,
    IntegerField,
    DateTimeField,
    BigAutoField,
    ForeignKey,
    CASCADE,
)
from m_user.models import Apoderado, Estudiante
from django.utils import timezone

op_estados = [
    [0, "No Pagado"],
    [1, "Pendiente"],
    [2, "Pagado"],
]


class Matricula(Model):
    id = BigAutoField(primary_key=True)
    estado = IntegerField(choices=op_estados, null=False)
    fecha = DateTimeField(auto_now_add=True)
    periodo = IntegerField(null=False)
    apoderado = ForeignKey(Apoderado, on_delete=CASCADE)
    estudiante = ForeignKey(Estudiante, on_delete=CASCADE)

    class Meta:
        db_table = "Matricula"

    def __str__(self):
        return f"{self.id}"
