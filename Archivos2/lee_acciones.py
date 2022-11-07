accion = open('acciones.txt','r')
listaTotal = []
for linea in accion:
    linea = linea.rstrip('\n')
    lista = linea.split(',')
    listaTotal.append(lista)
print(listaTotal)
accion.close()
ordenada = sorted(listaTotal, key = lambda: listaTotal[5])
print(ordenada)
resumen = open('resumen4.txt', 'w')
for lista in listaTotal:
    resumen.write(lista[0]+','+lista[5]+'\n')
resumen.close()
