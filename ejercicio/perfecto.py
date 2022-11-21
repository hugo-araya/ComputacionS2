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
    lista1 = lista_de_divisores(n1)
    suma1 = sum(lista1)-n1
    if n1 == suma1:
        print("El", n1,'es PERFECTO')
    else:
        print("El", n1,'"NO" es perfecto')
