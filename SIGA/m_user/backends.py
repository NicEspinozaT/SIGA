from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from .models import Apoderado, Estudiante, Docente


class BackendCustomAuth(BaseBackend):
    def authenticate(self, request, num_rut=None, contrasenia=None):
        # Buscar en Apoderado
        try:
            user = Apoderado.objects.get(num_rut=num_rut)
            if check_password(contrasenia, user.contrasenia):
                return user
        except Apoderado.DoesNotExist:
            pass

        # Buscar en Estudiante
        try:
            user = Estudiante.objects.get(num_rut=num_rut)
            if check_password(contrasenia, user.contrasenia):
                return user
        except Estudiante.DoesNotExist:
            pass

        # Buscar en Docente
        try:
            user = Docente.objects.get(num_rut=num_rut)
            if check_password(contrasenia, user.contrasenia):
                return user
        except Docente.DoesNotExist:
            pass

        return None

    def get_user(self, user_id):
        try:
            return Apoderado.objects.get(pk=user_id)
        except Apoderado.DoesNotExist:
            try:
                return Estudiante.objects.get(pk=user_id)
            except Estudiante.DoesNotExist:
                try:
                    return Docente.objects.get(pk=user_id)
                except Docente.DoesNotExist:
                    return None
