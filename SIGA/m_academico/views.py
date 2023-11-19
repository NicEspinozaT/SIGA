from django.shortcuts import render, redirect
from .models import Curso, Asignatura
from .forms import CursoForm

# Create your views here.


def listar_cursos(request):
    cursos = Curso.objects.all()
    return render(request, "listar_cursos.html", {"cursos": cursos})


def agregar_curso(request):
    if request.method == "POST":
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_cursos")
    else:
        form = CursoForm()
    return render(request, "agregar_curso.html", {"form": form})
