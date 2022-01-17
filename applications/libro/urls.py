from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('libros/', views.ListLibros.as_view(), name='libros'),
    path('libros-2/', views.ListLibros2.as_view(), name='libros2'),
    path('libros-trg/', views.ListLibrosTrg.as_view(), name='libros-trg'),
    path('libro-detalle/<pk>/', views.LibroDetailView.as_view(), name='libro_detalle'),
]
