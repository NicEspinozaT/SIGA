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

def modificar_curso(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == "POST":
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            # Mensaje de éxito y redirección
            return redirect('cursos')
    else:
        form = CursoForm(instance=curso)
    return render(request, 'registro_docente.html', {'form_docente': form})

def eliminar_curso(request, pk):
    curso = Curso.objects.filter(pk=pk)
    curso.delete()
    return redirect("cursos")

def lista_asignaturas(request, curso_id):
    curso = get_object_or_404(Curso, pk=curso_id)
    asignaturas = Asignatura.objects.filter(cursos=curso)
    return render(request, 'lista_asignaturas.html', {'curso': curso, 'asignaturas': asignaturas})





def agregar_asignatura(request, curso_id):
    curso = get_object_or_404(Curso, pk=curso_id)
    if request.method == 'POST':
        form = AsignaturaForm(request.POST)
        if form.is_valid():
            asignatura = form.save(commit=False)
            asignatura.cursos = curso
            asignatura.save()            
            return redirect('lista_asignaturas', curso_id=curso.id)
    else:
        form = AsignaturaForm()

    return render(request, 'agregar_asignatura.html', {'form': form, 'curso': curso})