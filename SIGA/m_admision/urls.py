from django.urls import path
from .views import admision, matricula

urlpatterns = [
  path ("admision/", admision, name="admision"),
  path ("admision/matricula/", matricula, name="matricula" ),
]