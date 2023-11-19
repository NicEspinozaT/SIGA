from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from m_user.models import Apoderado, Estudiante, Docente
from m_administracion.models import Administrador


class CustomAuthUser(BaseBackend):
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


class CustomAuthAdmin(BaseBackend):
    def authenticate(self, request, correo_electronico=None, contrasenia=None):
        # Intentar encontrar un Administrador con el correo electrónico proporcionado
        try:
            admin = Administrador.objects.get(correo_electronico=correo_electronico)
            # Verificar si la contraseña coincide
            if check_password(contrasenia, admin.contrasenia1):
                return admin
        except Administrador.DoesNotExist:
            return None

    def get_user(self, user_id):
        # Obtener un Administrador por su ID para mantener la sesión
        try:
            return Administrador.objects.get(pk=user_id)
        except Administrador.DoesNotExist:
            return None
