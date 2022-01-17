from django.db import models
from django.db.models import Q


class AutorManager(models.Manager):
    '''Managers para el modelo Autor'''

    def buscar_autor(self, kword):
        resultado = self.filter(nombre__icontains=kword)
        return resultado

    def buscar_autor2(self, kword):
        '''Filtro con operador ó: nombre y apellidos '''
        resultado = self.filter(
            Q(nombre__icontains=kword)
            | Q(apellidos__icontains=kword))
        return resultado

    def buscar_autor3(self, kword):
        '''excluir con operador Y'''
        resultado = self.filter(nombre__icontains=kword).exclude(edad=100)
        return resultado

    def buscar_autor4(self, kword):
        '''filtro mayor que (gt) y menor que (lt)'''
        resultado = self.filter(edad__gt=99, edad__lt=101).order_by(
            'nombre', 'apellidos')
        return resultado
