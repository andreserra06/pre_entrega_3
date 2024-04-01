from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio , name="home"),
    path("ver_cursos", views.ver_cursos , name="cursos"),
    #path("alta_curso/<nombre>", views.alta_curso),
    path("alumnos", views.alumnos , name="alumnos"),
    path("alta_curso", views.curso_formulario, name= "formulario"),
    path("buscar_curso", views.buscar_curso, name= "buscando_curso"),
    path("buscar_alumno", views.Buscar_alumno, name= "buscando_Alumno"),
    path("buscar", views.buscar),
    path("ver_alumnos", views.ver_alumnos, name='ver_alumno'),
    path("alumnos_formulario", views.alumnos_formulario, name= 'alumno_formulario'),
    path("ver_profesores", views.ver_profesores, name='ver_profesor'),
    path("profesores_formulario", views.profesor_formulario, name= 'profesor_formulario'),
    

]

