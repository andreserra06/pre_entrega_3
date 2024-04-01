from django import forms


class Curso_formulario(forms.Form):

    nombre = forms.CharField(max_length=30)
    camada = forms.IntegerField()
    
class Alumnos_formulario(forms.Form):
   nombre = forms.CharField(max_length=30)
   cursando = forms.CharField(max_length=30)
   
class Profesor_formulario(forms.Form):
   nombre = forms.CharField(max_length=30)
   curso_a_cargo = forms.CharField(max_length=30)
   