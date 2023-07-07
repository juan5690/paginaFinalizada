from django import forms
from .models import persona, pelicula, compraBoleto
from django.contrib.auth.forms import AuthenticationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django.core.exceptions import ValidationError

class RegistroForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'password1', 'password2']






class personaForm(forms.ModelForm):

    rut = forms.CharField(max_length=12)

    def clean_rut(self):
        rut = self.cleaned_data['rut']
        # Verificar la longitud del rut
        if len(rut) != 10:
            raise ValidationError("el formato del rut debe ser: 12345678-9")

        # Verificar que el penúltimo valor sea un guion
        if rut[-2] != '-':
            raise ValidationError("El penúltimo valor del rut debe ser un guion")

        return rut

    class Meta:
        model=persona
        fields=["rut","nombre","apellido"]
        

class peliculaForm(forms.ModelForm):
    
    class Meta:
        model = pelicula
        fields = ["nombrePeli", "descripcion", "credYreparto", "portada", "linkTrailer"]
        
class frmUpdatePersona(forms.ModelForm):

    class Meta:
        model=persona
        fields=["nombre"]
        #fields=["nombre","apellido","sexo"]


from datetime import datetime
class boletoForm(forms.ModelForm):  
    fecha = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        input_formats=['%Y-%m-%d']
    )

    class Meta:
        model = compraBoleto
        fields = ["nombrePeli", "horario", "cantidad", "fecha"]


  
class LoginForm(AuthenticationForm):
    def init(self, args, **kwargs):
        super(LoginForm, self).init(args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.add_input(Submit('submit', 'Iniciar sesión'))