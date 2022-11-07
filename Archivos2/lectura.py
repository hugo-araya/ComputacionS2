archivo = open('archivo.txt')
linea = archivo.readline()
while linea != '':
    linea = linea.rstrip('\n')
    print(linea)
    linea=archivo.readline()
archivo.close()
archivo = open('archivo.txt')
for linea in archivo:
    linea = linea.rstrip('\n')
    print(linea)
    