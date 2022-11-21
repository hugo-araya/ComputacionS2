#Escribir un algoritmo que calcule (evalúe) el valor de la 
# función f(x)=x2- 2x-1 para valores que se encuentren en el 
# intervalo [1, 5] con un incremento de 0.5.
import math
def f1(x):
    y = x*x - 2*x - 1
    return y

def f2(x):
    y = math.pow(x,2) - 2*x - 1
    return y

def version1(inicio, fin, incremento):
    lista = []
    x = inicio
    while x <= fin:
        lista.append(f1(x))
        x = x + incremento
    return lista

def version2(inicio, fin, incremento):
    lista = []
    x = inicio
    while x <= fin:
        lista.append(f2(x))
        x = x + incremento
    return lista

if __name__ == '__main__':
    lista1 = version1(1,5,0.5)
    lista2 = version2(1,5,0.5)
    print(lista1)
    print(lista2)