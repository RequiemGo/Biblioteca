from django.shortcuts import render
from django.views.generic import ListView
from .models import Autor
# Create your views here.


class ListAutores(ListView):
    #model = Autor
    template_name = "autor/lista.html"
    context_object_name = 'lista_autores'

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        return Autor.objects.buscar_autor(palabra_clave)
