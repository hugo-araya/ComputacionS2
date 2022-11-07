ent = open('entrada.txt')
sal = open('salida.txt', 'w')
for linea in ent:
    linea2 = linea.upper()
    sal.write(linea2)
ent.close()
sal.close()
