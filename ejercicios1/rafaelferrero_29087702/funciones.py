# -*- coding: utf-8 -*-


def divide_enteros_y_al_cuadrado(a, b):
    try:
        r = (a // b) ** 2
    except ZeroDivisionError:
        return "El divisor no puede ser cero"
    else:
        return r


def convierte_a_decimal_y_multiplica(a, b):
    try:
        r = float(a) * b
    except ValueError:
        return "El parámetro debe ser un número válido"
    else:
        return r


def es_alphanumerico(a):
    return a.isalnum()


def tuplas(*args):
    return args


def dicctionario(*args):
    i = iter(args)
    d = dict(list(zip(i, i)))
    return d


def conjunto(*args):
    return set(args)


def usar_if(a):
    if a < 10:
        return "menor a diez"
    elif a == 10:
        return "igual a diez"
    else:
        return "mayor a diez"


def iterar(p):
    if isinstance(p, list) or isinstance(p, tuple):
        return [a ** 2 for a in p if a % 2 == 0]
    elif isinstance(p, dict):
        return [a ** 2 for a in list(p.keys()) if a % 2 == 0]
