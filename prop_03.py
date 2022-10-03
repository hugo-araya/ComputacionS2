"""Calcular el número de pulsaciones que debe tener una persona 
por cada 10 segundos de ejercicio aeróbico; la fórmula que se 
aplica cuando el sexo es femenino es:
numero pulsaciones = (220 - edad) /10 
y si el sexo es masculino:
numero pulsaciones = (210 - edad) /10"""
edad = int(input('Su edad: '))
print('Digite M para genero Masculino y F para genero Femenino')
genero = input('Genero: ')
if genero == 'F':
    pulsaciones = (220 - edad)/10
else:
    pulsaciones = (210 - edad)/10
print('Pulsaciones: ', pulsaciones)
