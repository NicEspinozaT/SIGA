from django.shortcuts import render, redirect, get_object_or_404
from .models import Curso, Asignatura
from .forms import CursoForm, AsignaturaForm

# Create your views here.


def listar_cursos(request):
    cursos = Curso.objects.all()
    return render(request, "listar_cursos.html", {"cursos": cursos})


def agregar_curso(request):
    if request.method == "POST":
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cursos")
    else:
        form = CursoForm()
    return render(request, "agregar_curso.html", {"form": form})


def lista_asignaturas(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    asignaturas = curso.cursos.all()  # Obtiene todas las asignaturas asociadas con este curso
    return render(request, 'lista_asignaturas.html', {'curso': curso, 'asignaturas': asignaturas})



def agregar_asignatura(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    if request.method == 'POST':
        form = AsignaturaForm(request.POST)
        if form.is_valid():
            asignatura = form.save(commit=False)
            asignatura.save()
            asignatura.cursos.add(curso)  # Agrega el curso actual a la asignatura
            return redirect('detalle_curso', curso_id=curso.id)
    else:
        form = AsignaturaForm()

    return render(request, 'agregar_asignatura.html', {'form': form, 'curso': curso})