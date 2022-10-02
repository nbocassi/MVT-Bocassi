import random
import string

from django.test import TestCase
from .models import Alumnos, Ubicacion
# Create your tests here.

class Alumnos(TestCase):
    

    def test_creacion_alumnos(self):
        # Test 1: Comprobar puedo crear un alumno con un nombre con letras random
        lista_letras_nombre = [random.choice(string.ascii_letters + string.digits) for _ in range(20)]
        lista_letras_apellido = [random.choice(string.ascii_letters + string.digits) for _ in range(20)]
        nombre_prueba = "".join(lista_letras_nombre)
        apellido_prueba = "".join(lista_letras_apellido)
        alumno_35 = Alumnos.objects.create(nombre=nombre_prueba, apellido=apellido_prueba)

        self.assertIsNotNone(alumno_35.id)
        self.assertEqual(alumno_35.nombre, nombre_prueba)
        self.assertEqual(alumno_35.apellido, apellido_prueba)