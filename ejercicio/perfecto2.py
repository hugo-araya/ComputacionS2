def lista_de_divisores(n):
    divisores = [1]
    di = 2
    while di <= n:
        if (n % di) == 0:
            divisores.append(di)
        di = di + 1
    return divisores 

if __name__ == '__main__':
    maximo = int(input('Limite superior para numeros perfectos:'))
    perfectos = []
    n1 = 2
    while n1 < maximo:
        lista1 = lista_de_divisores(n1)
        suma1 = sum(lista1)-n1
        if n1 == suma1:
            perfectos.append(n1)
        n1 = n1 + 1
    print(perfectos)
