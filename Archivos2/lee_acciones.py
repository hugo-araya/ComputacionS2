accion = open('acciones.txt','r')
listaTotal = []
for linea in accion:
    linea = linea.rstrip('\n')
    lista = linea.split(',')
    listaTotal.append(lista)
print(listaTotal)
accion.close()

resumen = open('resumen.txt', 'w')
for lista in listaTotal:
    promedio = (float(lista[2]) + float(lista[3]))/2
    resumen.write(lista[0]+','+str(promedio)+'\n')
resumen.close()
