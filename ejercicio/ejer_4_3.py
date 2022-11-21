def esta_ordenada(lista):
    ok = True
    i = 0
    largo = len(lista)
    while i < largo-1:
        if lista[i]>lista[i+1]:
            ok = False
        i = i + 1
    return ok

if __name__ == '__main__':
    lista = [1,2,3,4,5,6,7,1]
    retorno = esta_ordenada(lista)
    if retorno == True:
        print("La lista esta ordenada")
    else:
        print("La lista No esta ordenada")
