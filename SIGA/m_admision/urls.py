from django.urls import path
from .views import admision, registrar_apoderado

urlpatterns = [
    path("admision/", admision, name="admision"),
    path("admision/matricula/", registrar_apoderado, name="matricula"),
]
