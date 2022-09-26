nota1 = float(input('Notas 1: '))
por1 = float(input('Porcentaje nota 1: '))
nota2 = float(input('Notas 2: '))
por2 = float(input('Porcentaje nota 2: '))
nota3 = float(input('Notas 3: '))
por3 = float(input('Porcentaje nota 3: '))

por4 = float(input('Porcentaje nota 4: '))
acumulado = nota1*por1 + nota2*por2 + nota3*por3
falta = 4 - acumulado
nota = falta / por4
print('Necesito: ', nota)
