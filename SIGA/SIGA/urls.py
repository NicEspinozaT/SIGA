"""
URL configuration for SIGA project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from m_user.urls import urlpatterns as urlUser
from m_admision.urls import urlpatterns as urlAdmision
from .views import (
    mostrar_inicio,
    mostrar_contacto,
    mostrar_nosotros,
    matricula,
    listar_evaluaciones,
    listar_horario,
    listar_asistencia,
    listar_curso,
    asistencia_alumno
)


urlpatterns = [
    path("", mostrar_inicio, name="mostrar_inicio"),
    path("contacto/", mostrar_contacto, name="mostrar_contacto"),
    path("nosotros/", mostrar_nosotros, name="mostrar_nosotros"),
    path("matricula/", matricula, name="matricula"),
    path("evaluaciones/", listar_evaluaciones, name="evaluaciones"),
    path("horario/", listar_horario, name="horario"),
    path("asistencia/", listar_asistencia, name="asistencia"),
    path("asistencia-alumno/", asistencia_alumno, name="asistencia-alumno"),
    path("cursos/", listar_curso, name="cursos"),
    path("", include(urlUser)),
    path("", include( urlAdmision)),
    path("admin/", admin.site.urls),
]

if settings.DEBUG == True:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
