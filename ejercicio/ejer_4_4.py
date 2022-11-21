#A - Escribe una función llamada "duplicado" que 
#tome una lista y devuelva True si tiene algún elemento duplicado. 
#La función no debe modificar la lista.

def duplicado1(lista):
    ok = False
    i = 0
    while i < len(lista)-1:
        j = i + 1
        while j < len(lista):
            if lista[i] == lista[j]:
                ok = True
            j = j + 1
        i = i + 1
    return ok

def duplicado2(lista):
    ok = False
    for elem in lista:
        if lista.count(elem) != 1:
            ok = True
    return ok

if __name__ == '__main__':
    lista = [1,2,3]
    # Version 1
    print(duplicado1(lista))
    # Version 2
    print(duplicado2(lista))