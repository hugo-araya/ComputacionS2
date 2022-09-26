nota1 = float(input('Notas 1: '))
por1 = float(input('Porcentaje nota 1: '))
nota2 = float(input('Notas 2: '))
por2 = float(input('Porcentaje nota 2: '))
nota3 = float(input('Notas 3: '))
por3 = float(input('Porcentaje nota 3: '))
nota4 = float(input('Notas 4: '))
por4 = float(input('Porcentaje nota 4: '))
promedio = nota1*por1+nota2*por2+nota3*por3+nota4*por4
if promedio >= 4:
    mensaje = 'Alumno aprobado'
else:
    mensaje = 'Alumno reprobado'
print('Estado: ', mensaje, 'con nota: ', promedio)
