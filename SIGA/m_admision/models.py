from django.db.models import (
  Model,
  CharField,
  IntegerField,
  DateTimeField,
  BigAutoField,
  ForeignKey,
  CASCADE,
)
from m_user.models import (
  Apoderado,
  Estudiante,
)
from django.utils import timezone

op_estados = [
    [0, "No Pagado"],
    [1, "Pendiente"],
    [2, "Pagado"],
]

class Matricula(Model):
  id = BigAutoField (primary_key=True)
  estado = IntegerField(choices=op_estados, null=False)
  fecha = DateTimeField(auto_now_add=True, null=False)
  periodo = IntegerField (default=timezone.now().year, null=False)
  Apoderado = ForeignKey(Apoderado, on_delete=CASCADE)
  Estudiante = ForeignKey(Estudiante, on_delete=CASCADE)

  class Meta:
    db_table = "Matricula"

  def __str__(self):
    return f"{self.id}"