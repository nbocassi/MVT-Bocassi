from django import forms 
from .models import Post, Avatar

class CursoFormulario(forms.Form):
    nombre = forms.CharField()
    comision =forms.IntegerField()

class CursoFormulario1(forms.Form):
    nombre = forms.CharField()
    apellido =forms.CharField()

class CursoFormulario2(forms.Form):
    barrio = forms.CharField()
    provincia =forms.IntegerField()

class FormularioContacto(forms.Form):
    nombre = forms.CharField()
    apellido =forms.IntegerField()
    email = forms.EmailField()
    telefono = forms.IntegerField()
    pais = forms.CharField()
    mensaje = forms.CharField()

class postform(forms.ModelForm):
    title = forms.CharField()
    subtitle = forms.CharField()
    excerpt = forms.CharField()
    content = forms.CharField()
    header_image = forms.ImageField()
    slug = forms.CharField()

class AvatarFormulario(forms.ModelForm):

    class Meta:
        model = Avatar
        fields = ['imagen']