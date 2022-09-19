from django.urls import path

from alumnos import views

urlpatterns = [
    ###Links templates principales
    path('', views.inicio, name="inicio"),
    path('ubicacion/', views.ubicacion, name="ubicacion"),
    path('estudiantes/', views.alumnos, name="alumnos"),
    path('curso/', views.curso, name="curso"),
    ###Links Cursos y Formularios
    path('crear-curso/', views.curso_formulario, name="curso_formulario"),
    path('crear-curso1/', views.curso_formulario1, name="curso_formulario1"),
    path('crear-curso2/', views.curso_formulario2, name="curso_formulario2"), 
    path('busqueda2/', views.busqueda2, name="busqueda2"),
    path('buscar/', views.buscar, name="buscar"),
    ###Links Help
    path('ayuda/', views.ayuda,  name="ayuda"),
    path('contacto/', views.contacto,  name="contacto"),
]



"""
    path('busqueda-curso-form/', views.busqueda_cursos, name="busqueda_curso_form"),
    path('busqueda-curso/', views.buscar, name="busqueda_curso"),
"""