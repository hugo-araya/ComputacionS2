# Elaborar un programa que lea un string e indique la cantidad 
# de vocales que tiene.
cadena = input('Ingrese una cadena: ')
cont = 0
largo = len(cadena)
i = 0
while i < largo:
    if cadena[i] == 'a' or cadena[i] == 'e' or cadena[i] == 'i' or cadena[i] == 'o' or cadena[i] == 'u':
        cont = cont + 1
    i = i + 1
mensaje = 'El string: '+cadena+' tiene '+str(cont)+' caracteres.'
print(mensaje)
