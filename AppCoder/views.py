from django.shortcuts import render
from AppCoder.models import *
from django.http import HttpResponse
from django.template import loader
from AppCoder.forms import *


# Create your views here.



def inicio(request):
    return render( request , "padre.html")



def alta_curso(request,nombre):
    curso = Curso(nombre=nombre , camada=234512)
    curso.save()
    texto = f"Se guardo en la BD el curso: {curso.nombre} {curso.camada}"
    return HttpResponse(texto)


def ver_cursos(request):
    cursos = Curso.objects.all()
    dicc = {"cursos": cursos}
    plantilla = loader.get_template("cursos.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)


def alumnos(request):
    return render(request , "alumnos.html")


def curso_formulario(request):

    if request.method == "POST":

        mi_formulario = Curso_formulario( request.POST )

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            curso = Curso( nombre=datos["nombre"] , camada=datos["camada"])
            curso.save()
            return render(request , "formulario.html")


    return render(request , "formulario.html")

#------------------------------------------------------------------------------------------

def buscar_curso(request):

    return render(request, "buscar_curso.html")



def buscar(request):

    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        cursos = Curso.objects.filter(nombre__icontains= nombre)
        return render( request , "resultado_busqueda.html" , {"cursos":cursos})
    else:
        return HttpResponse("Ingrese el nombre del curso")

#------------------------------------------------------------------------------------------    

def ver_alumnos(request):
    alumnos = Alumno.objects.all()
    dicc = {"alumno": alumnos}
    print("contenido alumno")
    for alumno in alumnos:
        print(alumno.id, alumno.nombre, alumno.cursando,)
    print("contendio del dicc")
    print(dicc)
    plantilla = loader.get_template("ver_alumnos.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)

#------------------------------------------------------------------------------------------

def alumnos_formulario(request):

    if request.method == "POST":

        mi_formulario = Alumnos_formulario( request.POST )

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            alumno = Alumno( nombre=datos["nombre"], cursando = datos["cursando"])
            alumno.save()
            print(datos)
            alumno = Alumno.objects.all()
            print("alumno validado")
            return render(request , "formularioAlumnos.html")
        
        else:
            print("alumno no validado", mi_formulario.errors)


    return render(request , "formularioAlumnos.html")

#------------------------------------------------------------------------------------------

def ver_profesores(request):
    profesor = Profesor.objects.all()
    dicc = {"profesor": profesor}
    print("contenido profesor")
    for profesor in profesor:
        print(profesor.id, profesor.nombre, profesor.curso_a_cargo,)
    print("contendio del dicc")
    print(dicc)
    plantilla = loader.get_template("ver_profesores.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)

def profesor_formulario(request):

    if request.method == "POST":

        mi_formulario = Profesor_formulario( request.POST )

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            profesor = Profesor( nombre=datos["nombre"], curso_a_cargo = datos["curso_a_cargo"])
            profesor.save()
            print(datos)
            profesor = Alumno.objects.all()
            print("profesor validado")
            return render(request , "formularioProfesores.html")
        
        else:
            print("profesor no validado", mi_formulario.errors)


    return render(request , "formularioProfesores.html")

#------------------------------------------------------------------------------------------

def Buscar_alumno(request):

    return render(request, "buscar_alumno.html")



def buscar_A(request):

    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        alumnos = Alumno.objects.filter(nombre__icontains= nombre)
        return render( request , "resultadoAlumno.html" , {"alumnos":alumnos})
    else:
        return HttpResponse("Ingrese el nombre del alumno")
    

