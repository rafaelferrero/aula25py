# -*- coding: UTF-8 -*-

from django.contrib import admin
from .models import (
    Pais,
    Provincia,
    Localidad,
    Cuenta,
    Movimiento)


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