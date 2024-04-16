from django.shortcuts import render
from AppCoder.models import *
from django.http import HttpResponse
from django.template import loader
from AppCoder.forms import *
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

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

def Profesores(request):
    return render(request , "profesores.html")


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

def Buscar_profesor(request):

    return render(request, "buscar_profesor.html")



def buscar_A(request):

    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        alumnos = Alumno.objects.filter(nombre__icontains= nombre)
        return render( request , "resultadoAlumno.html" , {"alumnos":alumnos})
    else:
        return HttpResponse("Ingrese el nombre del alumno")
    
def buscar_P(request):

    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        Profesores = Profesor.objects.filter(nombre__icontains= nombre)
        return render( request , "resultadoProfesor.html" , {"profesor":Profesores})
    else:
        return HttpResponse("Ingrese el nombre del profesor")
    

def elimina_curso(request , id ):
    curso = Curso.objects.get(id=id)
    curso.delete()

    curso = Curso.objects.all()

    return render(request , "cursos.html" , {"cursos":curso})




def editar(request , id):

    curso = Curso.objects.get(id=id)

    if request.method == "POST":

        mi_formulario = Curso_formulario( request.POST )
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            curso.nombre = datos["nombre"]
            curso.camada = datos["camada"]
            curso.save()

            curso = Curso.objects.all()

            return render(request , "cursos.html" , {"cursos":curso})


        
    else:
        mi_formulario = Curso_formulario(initial={"nombre":curso.nombre , "camada":curso.camada})
    
    return render( request , "editar_curso.html" , {"mi_formulario": mi_formulario , "curso":curso})




def login_request(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user = authenticate(username=usuario , password=contra)

            if user is not None:
                login(request , user )
                avatares = Avatar.objects.filter(user=request.user.id)
                return render( request , "inicio.html" , {"url":avatares[0].imagen.url})
            else:
                return HttpResponse(f"Usuario no encontrado")
        else:
            return HttpResponse(f"FORM INCORRECTO {form}")


    form = AuthenticationForm()
    return render( request , "login.html" , {"form":form})




def register(request):
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse("Usuario creado")

    else:
        form = UserCreationForm()
    return render(request , "registro.html" , {"form":form})




def editarPerfil(request):

    usuario = request.user

    if request.method == "POST":
        
        mi_formulario = UserEditForm(request.POST)

        if mi_formulario.is_valid():

            informacion = mi_formulario.cleaned_data
            usuario.email = informacion["email"]
            password = informacion["password1"]
            usuario.set_password(password)
            usuario.save()
            return render(request , "inicio.html")

    else:
        miFormulario = UserEditForm(initial={"email":usuario.email})
    
    return render( request , "editar_perfil.html", {"miFormulario":miFormulario, "usuario":usuario})

