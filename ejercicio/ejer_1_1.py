lista1 = [1,2,3,4,5]

#version 1
lista2 = []
suma = 0
for elem in lista1:
    suma = suma + elem
    lista2.append(suma)
print(lista2)

#version 2
lista3 = []
suma = 0
i = 0
while i < len(lista1):
    suma = suma + lista1[i]
    lista3.append(suma)
    i = i + 1
print(lista3)
