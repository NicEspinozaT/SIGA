from django.urls import path
from .views import registrar_docente

urlpatterns = [
    path("registrar_docente/", registrar_docente, name="registrarDocente"),
]