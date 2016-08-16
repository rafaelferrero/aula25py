# -*- coding: utf-8 -*-

from funciones import *
from decimal import *

print(divide_enteros_y_al_cuadrado(42, 3) == 196)
print(divide_enteros_y_al_cuadrado(42, 5.5) == 49)
print(divide_enteros_y_al_cuadrado(42, 0.5) == 7056)

print(convierte_a_decimal_y_multiplica('4.5', 2) == Decimal('9.0'))
print(convierte_a_decimal_y_multiplica('0.1', 10) == Decimal('1.0'))
print(convierte_a_decimal_y_multiplica('0.3', 10) == Decimal('3.0'))

print(es_alphanumerico('4') == True)
print(es_alphanumerico('m') == True)
print(es_alphanumerico('') == False)

print(tuplas(1, 2, 3) == (1, 2, 3))
print(tuplas(None, [], (1, 2, 3)) == (None, [], (1, 2, 3)))

print(dicctionario('a', 1, 'b', 2) == {'a': 1, 'b': 2})
print(dicctionario((1,), [1], (1,2), [1,2]) == {(1,): [1], (1, 2): [1,2]})

print(conjunto(1.1, 1.2, 1.3, 1.3) == {1.1, 1.2, 1.3})
print(conjunto(None, True, True, True, False, False, None) == {None, True, False})

print(usar_if(3) == "menor a diez")
print(usar_if(13) == "mayor a diez")
print(usar_if(10) == "igual a diez")

print(iterar([1, 2, 3, 4, 5, 6, 7, 8]) == [4, 16, 36, 64])
print(iterar((90, 80, 70, 60, 50)) == [8100, 6400, 4900, 3600, 2500])
print(iterar({23: 'a', 44: '44', 55: '8', 90: '', 21: ''}) == [8100, 1936])
print(iterar([21, 31, 45, 67, 81]) == [])