from django.contrib import admin
from .models import TipoUsuario, Usuario, Apoderado, Estudiante

admin.site.register(TipoUsuario)
admin.site.register(Usuario)
admin.site.register(Apoderado)
admin.site.register(Estudiante)
