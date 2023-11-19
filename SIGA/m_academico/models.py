from m_user.models import Estudiante, Docente
from django.utils import timezone
from django.db.models import (
    Model,
    CharField,
    IntegerField,
    ForeignKey,
    ManyToManyField,
    DecimalField,
    CASCADE,
)

lista_nivel = [
    [0, "1° basico"],
    [1, "2° basico"],
    [2, "3° basico"],
    [3, "4° basico"],
    [4, "5° basico"],
    [5, "6° basico"],
    [6, "7° basico"],
    [7, "8° basico"],
    [8, "1° medio"],
    [9, "2° medio"],
    [10, "3° medio"],
    [11, "4° medio"],
]
lista_seccion = [
    [0, "A"],
    [1, "B"],
]
lista_asign = [
    [0, "Matematicas"],
    [1, "Lenguaje"],
    [2, "Ingles"],
    [3, "Historia"],
    [4, "Ed. Fisica"],
]
lista_sigla = [
    [0, "MAT"],
    [1, "LEN"],
    [2, "ING"],
    [3, "HIST"],
    [4, "EFI"],
]


class Curso(Model):
    nivel = IntegerField(choices=lista_nivel, null=False)
    seccion = IntegerField(choices=lista_seccion, null=False)
    periodo = IntegerField(default=timezone.now().year, null=False)

    class Meta:
        db_table = "Curso"

    def __str__(self):
        return f"{self.nivel}{self.seccion} {self.periodo}"


class Asignatura(Model):
    nombre = IntegerField(choices=lista_asign, null=False)
    sigla = IntegerField(choices=lista_sigla, null=False)
    cursos = ManyToManyField(Curso, related_name="cursos")
    docentes = ManyToManyField(Docente, related_name="docentes")

    class Meta:
        db_table = "Asignatura"

    def __str__(self):
        return f"{self.nombre}-{self.sigla} {self.cursos}"


class EvaluacionPlanificada(Model):
    nombre = CharField(max_length=40)
    descripcion = CharField(max_length=100, null=True)
    ponderacion = DecimalField(max_digits=4, decimal_places=2)
    asignatura = ForeignKey(Asignatura, on_delete=CASCADE)
    curso = ForeignKey(Curso, on_delete=CASCADE)

    class Meta:
        db_table = "Evaluacion"

    def __str__(self):
        return f"{self.nombre} - {self.asignatura} (Ponderación: {self.ponderacion})"


class Calificacion(Model):
    evaluacion_planificada = ForeignKey(EvaluacionPlanificada, on_delete=CASCADE)
    nota = DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    estudiante = ForeignKey(Estudiante, on_delete=CASCADE)

    class Meta:
        db_table = "Calificacion"

    def __str__(self):
        return f"{self.evaluacion_planificada} - {self.estudiante}: {self.nota if self.nota is not None else 'Sin calificar'}"
