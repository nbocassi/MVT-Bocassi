from multiprocessing import context
from re import template
from typing import Dict
from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from datetime import datetime
from django.views.generic import TemplateView, CreateView, DetailView, ListView, UpdateView
from django.views.generic.detail import DetailView
from alumnos.models import Alumnos, Curso, Ubicacion, Post, Avatar
from alumnos.forms import CursoFormulario, CursoFormulario1, CursoFormulario2
from django.contrib import messages
from .forms import postform, AvatarFormulario
from .models import Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User


#----Sección Pages----#

def inicio(request):

      return render(request, "Alumnos/inicio.html")

def ubicacion(request):
      ubicacion = Ubicacion.objects.all()
      return render(request, "Alumnos/ubicacion.html",{'ubicacion': ubicacion})

def curso(request):
      curso = Curso.objects.all()
      return render(request, "alumnos/curso.html",{'curso': curso})

def alumnos(request):
      alumnos= Alumnos.objects.all()
      return render(request, "alumnos/estudiantes.html",{'alumnos': alumnos})

def estudiantes(request):

      return render(request, "Alumnos/estudiantes.html")

def ayuda(request):

      return render(request, "Alumnos/ayuda.html")

def contacto(request):

      return render(request, "Alumnos/contacto.html")      

def about(request):

      return render(request, "Alumnos/about.html")


#----Sección Forms & CRUD----#
def curso_formulario1(request):
      if request.method == 'POST':
            data_formulario: Dict = request.POST
            alumnos = Alumnos(nombre=data_formulario['nombre'], apellido=data_formulario['apellido'])
            alumnos.save()
            messages.success(request, "Tu usuario se creo correctamente!")
            return render(request, "Alumnos/estudiantes.html")
       
      else: 
       #GET  
            return render(request, "Alumnos/form_curso1.html")

def curso_formulario2(request):
      if request.method == 'POST':
            data_formulario: Dict = request.POST
            ubicacion = Ubicacion(barrio=data_formulario['barrio'], provincia=data_formulario['provincia'])
            ubicacion.save()
            messages.success(request, "Tu ubicacion se creo correctamente!")
            return render(request, "Alumnos/ubicacion.html")   
      else: 
       #GET  
            return render(request, "Alumnos/form_curso2.html")

def busqueda2(request):
      return render(request, "Alumnos/busqueda2.html")

def buscar(request):
      if request.GET["comision"]:
            comision = request.GET["comision"]
            curso = Curso.objects.filter(comision__icontains=comision)
            return render(request, "Alumnos/curso.html", {'curso': curso})
      else:
            return render(request, "Alumnos/curso.html", {'curso': []})

def eliminarpost (request, post_title):
      post = Post.objects.get(title=post_title)
      post.delete()
      
      messages.success(request, "Tu post se elimino correctamente!")
      posts = Post.objects.all()
      context = {"posts":posts}
      return render(request, "Alumnos/pages.html")




"""
def edit_post(request,post_title):
      post=Post.objects.get(title=post_title)
      return render(request,"Alumnos/editblog.html",{'post':post})
"""


"""
def update_post (request, post_title):
      post = Post.objects.get(title=post_title)
      post.save()
      
      messages.success(request, "Tu post se actualizo correctamente!")
      posts = Post.objects.all()
      context = {"posts":posts}
      return render(request, "Alumnos/editblog.html")
"""
"""
def create_post (request, post_title):
    post = Post.objects.get(title=post_title)
    form=postform(request.POST,instance=post)
    if form.is_valid:
        form.save()
        messages.success(request, "Tu post se actualizo correctamente!")
        object=Post.objects.all()
        return render(request, "Alumnos/editblog.html")
"""
"""
def createpost (request):
    if request.method == 'POST':
      form=postform(request.POST)
      
      if form.is_valid:
        data= form.cleaned_data
        post = Post(**data)
        post.save()
        messages.success(request, "Tu post se creo correctamente!")
        return render(request, "Alumnos/blog.html")
    
    else:
         form =   postform()
    return render(request, "Alumnos/form_post.html", {"form": form})
"""
"""
def updatepost (request, post_title):
    post = Post.objects.get(title=post_title)
    if request.method == 'POST':
      form=postform(request.POST)
      
      if form.is_valid:
        data= form.cleaned_data
        post.title = data['title']
        post.subtitle = data['subtitle']
        post.excerpt = data['excerpt']
        post.content = data['content']
        post.slug = data['slug']
        post.save()
        messages.success(request, "Tu post se actualizo correctamente!")
        return render(request, "Alumnos/blog.html")
    
    else:
      inicial = {
             'title': post.title,
             'subtitle': post.subtitle,
             'excerpt': post.excerpt,
             'content': post.content,
             'slug': post.slug,
      }
      form =   postform(initial=inicial)
    return render(request, "Alumnos/form_post.html", {"form": form})
"""

def curso_formulario(request):

      if request.method == 'POST':
            data_formulario: Dict = request.POST
            curso = Curso(nombre=data_formulario['nombre'], comision=data_formulario['comision'])
            curso.save()
            messages.success(request, "Tu curso se creo correctamente!")
            return render(request, "Alumnos/curso.html")
            
       
      else: 
       #GET  
            return render(request, "Alumnos/form_curso.html")


#----Experimental----#

class blog(TemplateView):
      template_name ="Alumnos/pages.html"

      def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context["posts"] = Post.postobjects.all()
            return context

class PostDetailView(DetailView):
      model = Post
      template_name = 'Alumnos/post-detail.html'
      context_object_name = 'post'

      def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            post = Post.objects.filter(slug=self.kwargs.get('slug'))
            return context

class addpost(CreateView):
      model = Post
      template_name = 'Alumnos/add_post.html'
      fields = '__all__'
      def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            addpost = Post.objects.filter(slug=self.kwargs.get('post'))
            return context

class ArticleDetailView(DetailView):
      model = Post
      template_name = 'Alumnos/article-details.html'

class Update_Post_View(UpdateView):
      model = Post
      template_name = 'Alumnos/update_post.html'
      fields = ['title', 'subtitle', 'content']


def Avatar(request):
      return render(request, "Alumnos/avatar.html")



@login_required
def nahuel(request):
    if request.method == 'POST':

        form = AvatarFormulario(request.POST, request.FILES) #aquí me llega toda la información del html

        if form.is_valid:   #Si pasó la validación de Django
            avatar = form.save()
            avatar.user = request.user
            avatar.save()
            return redirect(reverse('avatar'))

    form = AvatarFormulario() #Formulario vacio para construir el html
    return render(request, "Alumnos/nahuel.html", {"form":form})
