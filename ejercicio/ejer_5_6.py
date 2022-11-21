def lista_de_divisores(n):
    divisores = [1]
    di = 2
    while di <= n:
        if (n % di) == 0:
            divisores.append(di)
        di = di + 1
    return divisores 

if __name__ == '__main__':
    n1 = int(input('Primer numero a evaluar: '))
    n2 = int(input('Segundo numeroa evaluar: '))
    lista1 = lista_de_divisores(n1)
    lista2 = lista_de_divisores(n2)
    suma1 = sum(lista1)-n1
    suma2 = sum(lista2)-n2
    if n1 == suma2 and n2 == suma1:
        print("El", n1,'con el',n2,'son amigos')
    else:
        print("El", n1,'con el',n2,'"NO" son amigos')
