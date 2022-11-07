ent = open('archivo.txt')
sal = open('salida1.txt', 'a')

for linea in ent:
    linea = linea.rstrip('\n')
    linea = linea.upper()
    sal.write(linea+'\n')

ent.close()
sal.close()

