# -*- coding: utf-8 -*-
from django import forms
from cuentas.models import Movimiento, Localidad


class SearchForm(forms.Form):
    query = forms.CharField(
        label='Busca!',
        max_length=10,
        required=False,
    )
    nombre = forms.CharField(
        label='Nombre!',
        max_length=10,
        required=False,
    )
    limit = forms.IntegerField(
        label='Limite',
        min_value=1,
        required=False,
    )
    fecha = forms.DateField(
        label="Desde cuando",
        required=False
    )


class MovimientoForm(forms.ModelForm):

    class Meta:
        model = Movimiento
        fields = ('cuenta', 'comprobante', 'importe')


class LocalidadForm(forms.ModelForm):

    class Meta:
        model = Localidad
        fields = (
            'codigo_postal',
            'nombre',
            'abreviatura',
            'provincia')