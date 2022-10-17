nro1 = int(input('Numero 1: '))
nro2 = int(input('Numero 2: '))
if nro1 == nro2 :
    resultado = nro1 * nro2
else:
    if nro1 > nro2:
        resultado = nro1 - nro2
    else:
        resultado = nro1 + nro2
print('Resultado: ', resultado)
