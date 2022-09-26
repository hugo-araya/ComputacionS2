nota1 = float(input('Nota 1: '))
por1 = int(input('Porcentaje nota 1: '))
nota2 = float(input('Nota 2: '))
por2 = int(input('Porcentaje nota 2: '))
nota3 = float(input('Nota 3: '))
por3 = int(input('Porcentaje nota 3: '))
nota4 = float(input('Nota 4: '))
por4 = int(input('Porcentaje nota 4: '))
nota5 = float(input('Nota 5: '))
por5 = int(input('Porcentaje nota 5: '))
promedio = nota1*por1/100 + nota2*por2/100 + nota3*por3/100 + nota4*por4/100 + nota5*por5/100
if promedio >= 4.0:
    mensaje = 'Alumno aprobado'
else:
    mensaje = 'Alumno reprobado'
print('Estado: ', mensaje, 'con nota : ', promedio)

