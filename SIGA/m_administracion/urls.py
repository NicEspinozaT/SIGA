from django.urls import path
<<<<<<< HEAD
from .views import registrar_docente

urlpatterns = [
    path("registrar_docente/", registrar_docente, name="registrarDocente"),
]
=======
from .views import admin_login, vista_admin

urlpatterns = [
    path("admin_login/", admin_login, name="admin_login"),
    path("vista_admin/", vista_admin, name="vista_admin"),
]
>>>>>>> e55a6d034eb82c70b09876108f40fc3ef554127f
