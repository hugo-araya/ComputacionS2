ar = open('entrada.txt')
linea = ar.readline()
while linea != '':
    linea = linea.rstrip('\n')
    print(linea)
    linea = ar.readline()
ar.close()
