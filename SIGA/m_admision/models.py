from django.db.models import (
  Model,
  CharField,
  IntegerField,
  DateTimeField,
  BigAutoField,
)

op_estados = [
  [0, "No Pagado"],
  [1, "Pendiente"];
  [2, "Pagado"],
]

class Matricula(Model):
  id = BigAutoField (primary_key=True)
  estado = IntegerField(choices=op_estados)
  fecha = DateTimeField(auto_now_add=True)
  periodo = CharField (max_length=20)

  class Meta:
    db_table = "Matricula"

  def __str__(self):
    return f"{self.id}"