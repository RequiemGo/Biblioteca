from tabnanny import verbose
from django.db import models
from django.db.models.signals import post_delete
from applications.libro.models import Libro
from applications.autor.models import Persona
from .signals import update_libro_stock
# from managers
from .managers import PrestamoManager
# Create your models here.


class Lector(Persona):

    class Meta:
        verbose_name = 'Lector'
        verbose_name_plural = 'Lectores'


class Prestamo(models.Model):
    lector = models.ForeignKey(Lector, on_delete=models.CASCADE)
    libro = models.ForeignKey(
        Libro, on_delete=models.CASCADE, related_name='libro_prestamo')
    fecha_prestamo = models.DateField(
        'Fecha de prestamo')
    fecha_devolucion = models.DateField(
        'Fecha de devolución', blank=True, null=True)
    devuelto = models.BooleanField()

    objects = PrestamoManager()

    def save(self, *args, **kwards):
        self.libro.stock = self.libro.stock - 1
        self.libro.save()
        super(Prestamo, self).save(*args, **kwards)

    def __str__(self):
        return self.libro.titulo + '-->' + self.lector.nombre


# def update_libro_stock(sender, instance, **kwards):
#     '''Actulizamos el stock luego de eliminar un prestamo'''
#     instance.libro.stock = instance.libro.stock + 1
#     instance.libro.save()


post_delete.connect(update_libro_stock, sender=Prestamo)
