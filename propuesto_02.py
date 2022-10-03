""" En un supermercado se hace una promoción, mediante la cual el 
cliente obtiene un descuento dependiendo de un número que se escoge 
al azar. Si el número escogido es menor que 74 el descuento es 
del 15% sobre el total de la compra, si es mayor o igual a 74 el 
descuento es del 20%. Obtener cuánto dinero se le descuenta."""

""" En este enunciado el principal problema es como genero un numero
aleatorio, para esto se debe investigar como hacerlo, se debe importar una biblioteca 
que permite la generacion de numeros aleatorios

import random
azar = random.randint(0,140)
print('Azar: ', azar)

Este codigo genera numeros aleatorio entre dos valores enteros"""

import random
valor_inicial = int(input('Valor de lo comprado: '))
descuento_azar = random.randint(0,140)
if descuento_azar < 74:
    descuento = valor_inicial * 0.15
else:
    descuento = valor_inicial * 0.2
a_pagar = valor_inicial - descuento
print('Valor del descuento: ', descuento)
print("A pagar: ", a_pagar)
