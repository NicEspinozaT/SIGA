from django.urls import path
from .views import admision

urlpatterns = [
  path ("admision/", admision, name="admision"),
]