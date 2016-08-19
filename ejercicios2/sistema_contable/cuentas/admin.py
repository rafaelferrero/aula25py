# -*- coding: UTF-8 -*-

from django.contrib import admin
from django.db.models import Q
from .models import (
    Pais,
    Provincia,
    Localidad,
    Cuenta,
    Movimiento)


def set_zero(modeladmin, request, queryset):
    localidades = Localidad.objects.filter(Q(nombre__istartswith='p'))
    queryset.filter(cuenta__localidad__in=localidades).update(importe=0)

set_zero.short_description = "Convertir importe a 0 (Santa Fe y Rafaela)"


@admin.register(Pais)
class PaisAdmin(admin.ModelAdmin):
    actions_on_bottom = True
    list_display = [
        'nombre',
        'abreviatura']
    search_fields = [
        'nombre',
        'abreviatura']


@admin.register(Provincia)
class ProvinciaAdmin(admin.ModelAdmin):
    actions_on_bottom = True
    list_display = [
        'nombre',
        'abreviatura',
        'pais']
    search_fields = [
        'nombre',
        'abreviatura',
        'pais__nombre',
        'pais__abreviatura']
    list_filter = ['pais']


@admin.register(Localidad)
class LocalidadAdmin(admin.ModelAdmin):
    ordering = ('nombre',)


@admin.register(Cuenta)
class CuentaAdmin(admin.ModelAdmin):
    list_filter = ('localidad',)


@admin.register(Movimiento)
class MovimientoAdmin(admin.ModelAdmin):
    date_hierarchy = 'fecha'
    list_filter = ('cuenta__nombre',)