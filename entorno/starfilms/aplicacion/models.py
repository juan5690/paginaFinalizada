from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.core.validators import MinLengthValidator, MaxLengthValidator



HORARIO = [
        (1, "10:00 AM"),
        (2, "12:00 PM"),
        (3, "2:00 PM"),
        (4, "4:00 PM"),
        (5, "6:00 PM"),
    ]



def rut_validator(value):
    if not value[-2] == "-":
        raise ValidationError("El rut debe cumplir con el siguiente formato: 12345678-3")
    if len(value) != 10:
        raise ValidationError("El rut debe tener 10 caracteres")

class persona(models.Model):
    rut=models.CharField(primary_key=True, null=False, validators=[rut_validator], max_length=10,error_messages="Debe ingresar rut")
    nombre=models.CharField(max_length=50, null=False)
    apellido=models.CharField(max_length=50, null=False)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
@classmethod
def obtener_por_id(cls, persona_id):
    return cls.objects.get(id=persona_id)


class pelicula(models.Model):
    nombrePeli=models.CharField(max_length=50, null=False)
    descripcion=models.CharField(max_length=500,  null=False)
    credYreparto=models.CharField(max_length=50, null=False)
    portada=models.ImageField(upload_to="portadas", null=True)
    linkTrailer=models.CharField(max_length=500, null=True)
    def __str__(self):
        return f"{self.nombrePeli}"


class compraBoleto(models.Model):
    nombrePeli=models.ForeignKey(pelicula, on_delete=models.PROTECT,null=False)
    horario=models.IntegerField(null=False,choices=HORARIO,)
    cantidad = models.IntegerField(null=False)
    fecha=models.DateField(null=False)
    
    def __str__(self):
        return f"{self.nombrePeli} {self.fecha}"
# Create your models here.






class Usuario(AbstractUser):
    # Campos adicionales para el modelo de usuario
    # Puedes personalizar esto según tus necesidades
    
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='usuarios',
        blank=True,
        help_text='Los grupos a los que pertenece el usuario.',
        verbose_name='grupos'
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='usuarios',
        blank=True,
        help_text='Los permisos específicos de usuario.',
        verbose_name='permisos del usuario'
    )