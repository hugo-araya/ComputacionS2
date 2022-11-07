import matplotlib.pyplot as plt

ar = open('TotalesNacionalesResumen.csv')
linea1 = ar.readline()
linea1 = linea1.rstrip('\n')
lista1 = linea1.split(',')
listaX = []
for elem in lista1:
    l = elem.split('-')
    listaX.append(int(l[1]))
print(listaX)
linea2 = ar.readline()
linea2 = linea2.rstrip('\n')
lista2 = linea2.split(',')
ar.close()
listaY = []
for elem in lista2:
    listaY.append(float(elem))
#print(listaY)
plt.plot(listaX, listaY)
plt.title('Contagios')
plt.show()
