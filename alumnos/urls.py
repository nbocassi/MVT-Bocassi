from django.urls import path

from alumnos import views
from alumnos.views import PostDetailView

urlpatterns = [
    ###Links templates principales
    path('', views.inicio, name="inicio"),
    path('ubicacion/', views.ubicacion, name="ubicacion"),
    path('estudiantes/', views.alumnos, name="alumnos"),
    path('curso/', views.curso, name="curso"),
    path('blog/', views.blog.as_view(), name="blog"),
    ###Links Cursos y Formularios
    path('crear-curso/', views.curso_formulario, name="curso_formulario"),
    path('crear-curso1/', views.curso_formulario1, name="curso_formulario1"),
    path('crear-curso2/', views.curso_formulario2, name="curso_formulario2"), 
    path('busqueda2/', views.busqueda2, name="busqueda2"),
    path('buscar/', views.buscar, name="buscar"),
    ###Links Help
    path('ayuda/', views.ayuda,  name="ayuda"),
    path('contacto/', views.contacto,  name="contacto"),
    path('about/', views.about, name="about"),
    path('<slug:slug>/', PostDetailView.as_view(), name='post-detail',
),
]
