from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class Curso_formulario(forms.Form):

    nombre = forms.CharField(max_length=30)
    camada = forms.IntegerField()
    
class Alumnos_formulario(forms.Form):
   nombre = forms.CharField(max_length=30)
   cursando = forms.CharField(max_length=30)
   
class Profesor_formulario(forms.Form):
   nombre = forms.CharField(max_length=30)
   curso_a_cargo = forms.CharField(max_length=30)
   
class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Modificar")
    password1 = forms.CharField(label="Contraseña" , widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir la contraseña" , widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email','password1','password2']
        help_text = {k:"" for k in fields}
