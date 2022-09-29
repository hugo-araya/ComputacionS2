i = 0
suma = 0
n = int(input('Indique la cantidad de notas: '))
while i < n:
    mensaje = 'Ingrese nota'+str(i+1)+': '
    nota = float(input(mensaje))
    suma = suma + nota
    i = i + 1
promedio = suma / n
print('Promedio : ', promedio)
