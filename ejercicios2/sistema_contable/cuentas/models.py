# -*- coding: UTF-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from .choices import SIGNO


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
        verbose_name=_("Correo Electrónico"))

    def __str__(self):
        return "{0}-{1}-{2}".format(
            self.nombre,
            self.localidad,
            self.email)


class Movimiento(models.Model):
    cuenta = models.ForeignKey(
        Cuenta,
        verbose_name=_("Cuenta"))
    comprobante = models.TextField(
        verbose_name=_("Comprobante"))
    fecha = models.DateField(
        verbose_name=_("Fecha"))
    signo = models.CharField(
        max_length=2,
        choices=SIGNO,
        verbose_name=_("Signo"))
    importe = models.DecimalField(
        max_digits=20,
        decimal_places=4,
        verbose_name=_("Importe"))

    def __str__(self):
        return "{0}{1} ({2})".format(
            self.signo,
            self.importe,
            self.fecha)
