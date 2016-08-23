# -*- coding: UTF-8 -*-

from django.db.models import Q
from cuentas.models import *
from datetime import datetime


#Localidades con nombres que contengan la letra 'r'
respuesta = Localidad.objects.filter(nombre__icontains='r')

#Localidades sin cuentas
respuesta = Localidad.objects.filter(cuenta__localidad__isnull=True)

#Cuentas sin email
respuesta = Cuenta.objects.filter(
    Q(email__isnull=True) | Q(email=''))

#Movimientos de cuentas en Paraná
respuesta = Movimiento.objects.filter(
    cuenta__localidad__nombre__icontains='Paraná')

#Movimientos de cuentas que no estén en Paraná
respuesta = Movimiento.objects.exclude(
    cuenta__localidad__nombre__icontains='Paraná')

#Suma de los importes de los movimientos de las cuentas que no están en Paraná
respuesta = Movimiento.objects.exclude(
    cuenta__localidad__nombre__icontains='Paraná').aggregate(Sum('importe'))

#Cantidad de cuentas en Santa Fe
respuesta = Cuenta.objects.filter(
    localidad__nombre__icontains='Santa Fe').count()

#Gerentes que hayan ingresado antes de 1999 y que cobren más de $ 20000
respuesta = GerenteDeCuentas.objects.filter(
    Q(perfil__fecha_ingreso__year__lt=1999) &
    Q(perfil__sueldo__gt=20000))


#Gerentes con cuentas con movimientos de este mes
respuesta = GerenteDeCuentas.objects.filter(
    Q(cuentas__movimiento__fecha__year=datetime.now().year) &
    Q(cuentas__movimiento__fecha__month=datetime.now().month)).distinct()

#Gerentes con cuentas sin comprobante
respuesta = GerenteDeCuentas.objects.filter(
    cuentas__movimiento__comprobante__isnull=True).distinct()

