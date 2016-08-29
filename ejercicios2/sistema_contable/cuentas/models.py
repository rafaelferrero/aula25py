# -*- coding: UTF-8 -*-

from django.db import models
from django.db.models import Q
from django.utils.translation import ugettext_lazy as _


class Zona(models.Model):
    nombre = models.CharField(
        max_length=255,
        verbose_name=_('Nombre'))
    abreviatura = models.CharField(
        max_length=255,
        verbose_name=_('Abreviatura'),
        blank=True,
        null=True)

    def __str__(self):
        return "{0}".format(self.nombre)

    class Meta:
        abstract = True


class Pais(Zona):
    class Meta:
        ordering = ['nombre']
        verbose_name = _("Pais")
        verbose_name_plural = _("Paises")


class Provincia(Zona):
    pais = models.ForeignKey(
        Pais,
        verbose_name=_("Pais"),
        related_name='pais')

    def __str__(self):
        return "{0} ({1})".format(
            self.nombre,
            self.pais.abreviatura)

    class Meta:
        ordering = ['pais', 'nombre']
        verbose_name = _("Provincia")
        verbose_name_plural = _("Provincias")


class Localidad(Zona):
    provincia = models.ForeignKey(
        Provincia,
        verbose_name=_("Provincia"),
        related_name='provincia')
    codigo_postal = models.CharField(
        max_length=255,
        verbose_name=_("Codigo Postal"))

    def __str__(self):
        return "{0}, {1}".format(
            self.nombre,
            self.provincia)

    @property
    def nombre_completo(self):
        return "({0}) {1}, {2}".format(
            self.codigo_postal,
            self.nombre,
            self.provincia)

    class Meta:
        ordering = ['provincia', 'nombre']
        verbose_name = _("Localidad")
        verbose_name_plural = _("Localidades")


class Cuenta(models.Model):
    nombre = models.CharField(
        max_length=200,
        verbose_name=_("Nombre"))
    direccion = models.CharField(
        max_length=500,
        verbose_name=_("Dirección"))
    localidad = models.ForeignKey(
        Localidad,
        verbose_name=_("Localidad"))
    email = models.EmailField(
        blank=True,
        verbose_name=_("Correo Electrónico"))

    def __str__(self):
        return "{0}-{1}-{2}".format(
            self.nombre,
            self.localidad,
            self.email)

    class Meta:
        verbose_name = _('Cuenta')
        verbose_name_plural = _('Cuentas')


class Movimiento(models.Model):
    cuenta = models.ForeignKey(
        Cuenta,
        verbose_name=_("Cuenta"))
    comprobante = models.TextField(
        blank=True,
        verbose_name=_("Comprobante"))
    fecha = models.DateField(
        verbose_name=_("Fecha"))
    importe = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        default=0,
        verbose_name=_("Importe"))

    def __str__(self):
        return "{0} ({1}) - {2}".format(
            self.importe,
            self.fecha,
            self.cuenta.nombre)

    @staticmethod
    def ultimos():
        return Movimiento.objects.order_by('-id')[:10]

    @staticmethod
    def get_with(query, nombre='', limit=None, fecha=None):
        if nombre:
            queryset = Movimiento.objects.filter(
                cuenta__nombre__contains=nombre)
        else:
            q1 = Q(cuenta__nombre__contains=query)
            q2 = Q(comprobante__contains=query)
            queryset = Movimiento.objects.filter(q1 | q2)
        if fecha:
            queryset = queryset.filter(fecha__gte=fecha)
        if limit:
            return queryset[:limit]
        return queryset

    class Meta:
        verbose_name = _('Movimiento')
        verbose_name_plural = _('Movimientos')


class PerfilEmpleado(models.Model):
    fecha_ingreso = models.DateField()
    sueldo = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        default=20000)

    def __str__(self):
        return "{0} ({1})".format(
            self.fecha_ingreso.strftime(
                "%d, %b %Y"),
            self.sueldo)

    class Meta:
        verbose_name = _('Perfil de Empleado')
        verbose_name_plural = _('Perfiles de Empleado')


class GerenteDeCuentas(models.Model):
    nombre = models.CharField(
        max_length=300)
    cuentas = models.ManyToManyField(Cuenta)
    perfil = models.OneToOneField(
        PerfilEmpleado,
        null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = _('Gerente de Cuenta')
        verbose_name_plural = _('Gerentes de Cuenta')