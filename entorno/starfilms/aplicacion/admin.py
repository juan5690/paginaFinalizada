from django.contrib import admin
from .models import persona, pelicula, compraBoleto, Usuario
# Register your models here.

admin.site.register(persona)

admin.site.register(pelicula)

admin.site.register(compraBoleto)

admin.site.register(Usuario)