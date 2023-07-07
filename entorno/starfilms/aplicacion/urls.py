from django.urls import path
from .views import *
from . import views
from .views import registro, inicio, inicio_sesion, cerrar_sesion
urlpatterns = [
    path('',index ,name="index"),
    
    path('sesion/', sesion, name="sesion"),
    path('jaws/', jaws, name="jaws"),
    path('thedriver/', thedriver, name="thedriver"),
    path('halloween/', halloween, name="halloween"),
    path('medioPago/', medioPago, name="medioPago"),
    path('medioPago2/', medioPago2, name="medioPago2"),
    path('agregar-persona/', agregar_persona, name='agregar_persona'),
    path('listar-personas/', listar_personas, name="listar_personas"),
    path('updatepersona/<id>',updatepersona,name="updatepersona"),
    path('eliminarPersona/<id>',eliminarpersona, name="eliminarpersona"),
    path('agregar_pelicula/', agregar_pelicula, name="agregar_pelicula"),
    path('listar_peliculas/', listar_peliculas, name="listar_peliculas"),
    path('eliminar_pelicula/<id>', eliminarpelicula, name="eliminarpelicula"),
    path('registro/', registro, name='registro'),
    path('inicio/', inicio, name='inicio'),
    path('inicio_sesion/', inicio_sesion, name='inicio_sesion'),
    path('pagina_principal/', pagina_principal, name='pagina_principal'),
    path('cerrar_sesion/', cerrar_sesion, name='cerrar_sesion'),
    path('mensaje_pago/', mensaje_pago, name='mensaje_pago'),
    path('mensaje_pago2/', mensaje_pago2, name='mensaje_pago2'),
    path('agregar_boleto', agregar_boleto, name='agregar_boleto'),
    path('agregar_boleto2', agregar_boleto2, name='agregar_boleto2'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('administrador/', administrador, name='administrador'),
    path('login/app/administrador/', views.administrador, name='administrador'),
    path('thedriver2/', thedriver2, name="thedriver2"),
    path('halloween2/', halloween2, name="halloween2"),
    path('jaws2/', jaws2, name="jaws2"),
]