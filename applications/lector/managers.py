import datetime
from django.db import models
from django.db.models import Q, Count, Avg


class PrestamoManager(models.Manager):
    '''procedimiento para prestamo'''

    def libros_promedio_edades(self):
        resultado = self.filter(libro__id='3').aggregate(
            promedio_edad=Avg('lector__edad')
        )
        return resultado

    def num_libros_prestados(self):
        resultado = self.values(
            'libro'
        ).annotate(num_prestados=Count('libro'))
        for r in resultado:
            print('********')
            print(r, r['num_prestados'])
        return resultado
