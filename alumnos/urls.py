from django.urls import path

from alumnos import views
from alumnos.views import PostDetailView, addpost, ArticleDetailView, Update_Post_View

urlpatterns = [
    ###Links templates principales
    path('', views.inicio, name="inicio"),
    path('ubicacion/', views.ubicacion, name="ubicacion"),
    path('estudiantes/', views.alumnos, name="alumnos"),
    path('curso/', views.curso, name="curso"),
    path('pages/', views.blog.as_view(), name="pages"),
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
    path('eliminarpost/<post_title>', views.eliminarpost, name="eliminarpost"),
    #path('createpost/', views.createpost, name="createpost"),
    #path('updatepost/<post_title>/', views.updatepost, name="updatepost"),
    path('add_post/', addpost.as_view(), name="addpost"),
    path('<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('article/update/<int:pk>/', Update_Post_View.as_view(), name='article-update'),
]
