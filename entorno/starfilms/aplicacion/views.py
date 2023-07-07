from django.shortcuts import render, redirect, get_object_or_404
from .models import pelicula, persona
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegistroForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm


def cerrar_sesion(request):
    logout(request)
    return redirect('inicio')



@login_required
def pagina_principal(request):
    return render(request, 'pagina_principal.html')

def inicio_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('pagina_principal')  # Redirige a la página de inicio después de iniciar sesión correctamente
       
    else:
        form = AuthenticationForm()
    return render(request, 'inicio_sesion.html', {'form': form})

# Create your views here.

def index(request):
    peliculas = pelicula.objects.all()
    
    data= {
        'peliculas' : peliculas        
    }
    return render(request, 'app/index.html', data)


def jaws2(request):
    return render(request, 'app/jaws2.html')

def halloween2(request):
    return render(request, 'app/halloween2.html')

def thedriver2(request):
    return render(request, 'app/thedriver2.html')

def sesion(request):
    return  render(request, 'inicio_sesion.html')

def jaws(request):
    return render(request, 'app/jaws.html')

def halloween(request):
    return render(request, 'app/halloween.html')

def thedriver(request):
    return render(request, 'app/thedriver.html')

def medioPago(request):
    return render(request, 'app/medioPago.html')


def mensaje_pago(request):
    return render(request, 'app/mensaje_pago.html')

def medioPago2(request):
    return render(request, 'app/medioPago2.html')


def mensaje_pago2(request):
    return render(request, 'app/mensaje_pago2.html')


def agregar_boleto(request):
    
    data={
        'form':boletoForm() 
    }
    
    if request.method =='POST':
        formulario = boletoForm(data = request.POST)
        
        if formulario.is_valid():
            formulario.save()
            return redirect('medioPago')
        else:
            data["form"] = formulario
        
    return render(request, 'app/boletos/agregar_boleto.html', data)


def agregar_boleto2(request):
    
    data={
        'form':boletoForm() 
    }
    
    if request.method =='POST':
        formulario = boletoForm(data = request.POST)
        
        if formulario.is_valid():
            formulario.save()
            return redirect('medioPago2')
        else:
            data["form"] = formulario
        
    return render(request, 'app/boletos/agregar_boleto2.html', data)

""" personas """

def agregar_persona(request):
    
    data={
        'form':personaForm() 
    }
    
    if request.method =='POST':
        formulario = personaForm(data = request.POST)
        
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]="usuario guardado exitosamente!!!"
        else:
            data["form"] = formulario
        
    return render(request, 'app/personas/agregar.html', data)


def listar_personas(request):
    personas = persona.objects.all()
    
    data = {
        'personas': personas
    }
    
    return render(request, 'app/personas/listar.html', data)


def updatepersona(request, id):
    persona_instance = get_object_or_404(persona, rut=id)

    form = frmUpdatePersona(instance=persona_instance)
    contexto = {
        "form": form,
        "persona": persona_instance
    }

    if request.method == "POST":
        form = frmUpdatePersona(data=request.POST, instance=persona_instance)

        if form.is_valid():
            form.save()
            return redirect("listar_personas")

    return render(request, "app/personas/modificar.html", contexto)


def eliminarpersona(request,id):
    personas=get_object_or_404(persona, rut=id)
    personas.delete()
    return redirect(to="listar_personas")



""" peliculas """
def agregar_pelicula(request):
    
    data={
        'form':peliculaForm() 
    }
    
    if request.method =="POST":
        formulario =peliculaForm(data=request.POST, files=request.FILES)
        
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]="pelicula guardada exitosamente!!!"
        else:
            data["form"] = formulario
        
    return render(request, 'app/peliculas/agregar.html', data)

def listar_peliculas(request):
    peliculas = pelicula.objects.all
    
    data={
        'pelicula': peliculas
    }
    return render(request, 'app/peliculas/listar.html', data)

def eliminarpelicula(request,id):
    peliculas=get_object_or_404(pelicula, nombrePeli=id)
    peliculas.delete()
    return redirect(to="listar_peliculas")


@login_required
def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('inicio_sesion')  # Redirige a la página de inicio después del registro exitoso
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})

def inicio(request):
    return render(request, 'app/index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('administrador')  # Reemplaza 'nombre_de_tu_url' por la URL a la que quieres redirigir después del inicio de sesión
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
    return render(request, 'app/login.html')
def logout_view(request):
    logout(request)
    return redirect('app/administrador.html')
def administrador(request):
    return render(request, 'app/administrador.html')