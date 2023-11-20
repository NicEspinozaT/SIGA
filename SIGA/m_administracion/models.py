from django.utils import timezone
from django.db.models import Model, EmailField, CharField, DateTimeField, BooleanField
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
import secrets, string


class Administrador(Model):
    correo_electronico = EmailField(unique=True)
    nombre = CharField(max_length=100)
    apellido = CharField(max_length=100)
    contrasenia1 = CharField(max_length=128, null=True, blank=True)
    fecha_creacion = DateTimeField(auto_now_add=True)
    last_login = DateTimeField("last_login", default=timezone.now)
    es_activo = BooleanField(default=True)

    class Meta:
        db_table = "Administrador"

    def save(self, *args, **kwargs):
        if not self.contrasenia1:  # Si es un nuevo registro
            adminpass1 = self.generar_contrasenia_aleatoria()

            send_mail(
                "Contraseña de Administrador del sistema SIGA",
                f"Tu contraseña de Administrador son:\n1: {adminpass1}",
                "siga.educacion@gmail.com",
                [self.correo_electronico],
                fail_silently=False,
            )

            self.contrasenia1 = make_password(adminpass1)

        super().save(*args, **kwargs)

    @staticmethod
    def generar_contrasenia_aleatoria(longitud=12):
        caracteres = string.ascii_letters + string.digits
        return "".join(secrets.choice(caracteres) for _ in range(longitud))

    def __str__(self):
        return self.nombre
