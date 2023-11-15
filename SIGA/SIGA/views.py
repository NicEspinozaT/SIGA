from django.shortcuts import render

def mostrar_inicio(request):
    return render(request, "home/inicio.html")

def mostrar_contacto(request):
    return render(request, "informacion/contacto.html")

def mostrar_nosotros(request):
    return render(request, "informacion/sobre_nosotros.html")

def matricula(request):
    return render(request, "matricula/matricula.html")

def listar_evaluaciones(request):
    return render(request, "informacion/listarEvaluaciones.html")

def listar_asistencia(request):
    return render(request, "informacion/listarAsistencia.html")

def listar_horario(request):
    return render(request, "informacion/listarHorario.html")

def listar_curso(request):
    return render(request, "informacion/cursos.html")

def asistencia_alumno(request):
    return render(request, "informacion/asistenciaAlumno.html")
