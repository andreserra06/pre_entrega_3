from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("", views.inicio , name="home"),
    path("ver_cursos", views.ver_cursos , name="cursos"),
    #path("alta_curso/<nombre>", views.alta_curso),
    path("alumnos", views.alumnos , name="alumnos"),
    path("alta_curso", views.curso_formulario, name= "formulario"),
    path("buscar_curso", views.buscar_curso, name= "buscando_curso"),
    path("buscar_alumno", views.Buscar_alumno, name= "buscando_alumno"),
    path("buscar_profesor", views.Buscar_profesor, name= "buscando_profesor"),
    path("buscar", views.buscar),
    path("buscar_A", views.buscar_A, name='buscar_A'),
    path("buscar_P", views.buscar_P, name='buscar_P'),
    path("ver_alumnos", views.ver_alumnos, name='ver_alumno'),
    path("alumnos_formulario", views.alumnos_formulario, name= 'alumno_formulario'),
    path("ver_profesores", views.ver_profesores, name='ver_profesor'),
    path("profesores_formulario", views.profesor_formulario, name= 'profesor_formulario'),
    path("elimina_curso/<int:id>" , views.elimina_curso , name="elimina_curso"),
    path("editar_curso/<int:id>" , views.editar , name="editar_curso"),
    path("login", views.login_request , name="Login"),
    path("register", views.register , name="Register"),
    path("logout" , LogoutView.as_view(template_name="logout.html") , name="Logout"),
    path("editarPerfil" , views.editarPerfil , name="EditarPerfil"),
   
]

