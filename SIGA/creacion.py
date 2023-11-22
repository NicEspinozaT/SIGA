# create_admin.py

import os
import django

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "SIGA.settings"
)  # Reemplaza 'tu_proyecto.settings' con la ruta de tus ajustes de Django
django.setup()

from m_administracion.models import (
    Administrador,
)  # Asegúrate de cambiar 'm_administracion' al nombre correcto de tu app


def create_admin(correo, nombre, apellido, contrasenia):
    admin = Administrador(
        correo_electronico=correo,
        nombre=nombre,
        apellido=apellido,
        contrasenia1="",
    )
    admin.save()
    print(f"Administrador creado: {admin}")


if __name__ == "__main__":
    # Puedes pedir al usuario que ingrese los detalles o simplemente codificarlos aquí
    correo = "nicolasespinoza1985@gmail.com"
    nombre = "Nicolas"
    apellido = "Espinoza"
    contrasenia = ""

    create_admin(correo, nombre, apellido, contrasenia)
