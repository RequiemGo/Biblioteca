from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('prestamo/', views.AddPrestamo.as_view(), name='prestamo'),
    path('prestamo/multiple', views.AddMultiplePrestamo.as_view(),
         name='prestamo_add_multiple'),
]
