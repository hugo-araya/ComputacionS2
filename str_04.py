# Elaborar un programa que lea un string e indique la cantidad 
# de vocales que tiene.
cadena = input('Ingrese una cadena: ')
vocales = 'aeiouAEIOU'
cont = 0
largo = len(cadena)
i = 0
while i < largo:
    if cadena[i] in vocales:
        cont = cont + 1
    i = i + 1
mensaje = 'El string: '+cadena+' tiene '+str(cont)+' caracteres.'
print(mensaje)
