# -*- coding: UTF-8 -*-
from django.http import (
    Http404,
    HttpResponse,
)
from django.shortcuts import (
    render,
    get_object_or_404,
    redirect,
)
from datetime import (
    datetime,
    date,
)
from cuentas.forms import (
    SearchForm,
    MovimientoForm,
    LocalidadForm,
    BuscaMovimientoForm,
)
from cuentas.models import (
    Cuenta,
    Movimiento,
    Localidad,
    GerenteDeCuentas,
)


def index(request):
    return render(request, 'base.html', {})


def busqueda(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            nombre = form.cleaned_data['nombre']
            limit = form.cleaned_data['limit']
            fecha = form.cleaned_data['fecha']
            movimientos = Movimiento.get_with(
                query,
                nombre,
                limit,
                fecha)
            return render(
                request,
                'resultados.html',
                {
                    'query': query,
                    'movimientos': movimientos
                }
            )
    else:
        form = SearchForm()

    return render(request, 'busqueda.html', {'form': form})


def movimientos(request):
    if request.method == 'POST':
        form = MovimientoForm(request.POST)
        if form.is_valid():
            movimiento = form.save(commit=False)
            movimiento.fecha = date.today()
            movimiento.save()
            return render(
                 request,
                 'movimientos.html',
                 {
                     'movimientos': Movimiento.ultimos(),
                 }
            )
    else:
        form = MovimientoForm()
        return render(
            request,
            'get_movimientos.html',
            {
                'form': form,
                'movimientos': Movimiento.ultimos()
            }
        )


def fecha(request):
    now = datetime.now()
    html = "<html><body>El año es {0}.</body></html>".format(now.year)
    return HttpResponse(html)


def cuentas(request):
    return render(
        request,
        'cuentas2.html',
        {
            'cuentas': Cuenta.objects.all(),
            'total': Cuenta.objects.count()
        }
    )


def cuenta(request, clave):
    try:
        c = Cuenta.objects.get(pk=clave)
    except Cuenta.DoesNotExist:
        raise Http404("No existe la cuenta")

    return render(request, 'cuenta2.html', {'c': c})


def localidades(request):
    return render(
         request,
         'localidades.html',
         {'localidades': Localidad.objects.all()}
    )


def localidad_update(request, clave):
    localidad = get_object_or_404(Localidad, pk=clave)
    if request.method == 'POST':
        form = LocalidadForm(request.POST, instance=localidad)
        if form.is_valid():
            form.save()
            return redirect('cuentas.views.localidades')
    else:
        form = LocalidadForm(instance=localidad)
        return render(
            request,
            'get_localidades.html',
            {
                'form': form,
                'localidades': Localidad.objects.all(),
                'clave': clave,
            }
        )


def localidad_create(request):
    if request.method == 'POST':
        form = LocalidadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cuentas.views.localidades')
    else:
        form = LocalidadForm()
        return render(
            request,
            'get_localidades.html',
            {
                'form': form,
                'localidades': Localidad.objects.all(),
            }
        )


def gerentes(request):
    gerentes = GerenteDeCuentas.objects.all()
    return render(
        request,
        'gerentes.html',
        {'gerentes': gerentes}

    )

def gerente(request, clave):
    return render(
        request,
        'gerente.html',
        {'gerente': GerenteDeCuentas.objects.get(pk=clave)}
    )

def busca_movimientos(request,clave):
    if request.method == 'POST':
        form = BuscaMovimientoForm(request.POST)
        if form.is_valid():
            importe = form.cleaned_data['importe']
            movimientos = Movimiento.get_movimiento(
                importe,
                clave,
            )
            return render(
                request,
                'gerente.html',
                {
                    'gerente': GerenteDeCuentas.objects.get(pk=clave),
                    'importe': importe,
                    'movimientos': movimientos
                }
            )
    else:
        form = BuscaMovimientoForm()

    return render(
        request,
        'gerente.html',
        {
            'gerente': GerenteDeCuentas.objects.get(pk=clave),
        }
    )