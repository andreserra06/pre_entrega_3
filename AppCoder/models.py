from django.db import models

# Create your models here.


class Curso(models.Model):

    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
    
class Profesor(models.Model):
    
    nombre = models.CharField(max_length=40)
    curso_a_cargo = models.CharField(max_length=40)
    
class Alumno(models.Model):
    
    nombre = models.CharField(max_length=40)
    cursando = models.CharField(max_length=40)