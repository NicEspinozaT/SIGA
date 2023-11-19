from django.shortcuts import render, redirect
from .forms import FormularioApoderado
from sweetify import success, warning


def admision(request):
    return render(request, "admision.html")



def registrar_apoderado(request):
    if request.method == "POST":
        form = FormularioApoderado(request.POST)
        if form.is_valid():
            form.save()
            return redirect("mostrar_inicio")
    else:
        form = FormularioApoderado()

    return render(request, "matricula.html", {"form": form})
