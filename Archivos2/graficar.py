import matplotlib.pyplot as plt

ar = open('TotalesNacionalesActualizado.csv')
linea1 = ar.readline()
linea1 = linea1.rstrip('\n')
listaX = linea1.split(',')
linea2 = ar.readline()
linea2 = linea2.rstrip('\n')
lista2 = linea2.split(',')
ar.close()
listaY = []
for elem in lista2:
    listaY.append(float(elem))
#print(listaY)
plt.plot(listaY)
plt.title('Contagios')
plt.show()
