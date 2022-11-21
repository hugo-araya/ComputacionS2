# Conjetura de Collatz
# Si el número es par, se divide entre 2.
# Si el número es impar, se multiplica por 3 y se le suma 1.

def conjetura(n):
    lista = [n]
    while n != 1:
        if (n % 2) == 0:
            n = n // 2
        else:
            n = 3*n + 1
        lista.append(n)
    return lista

if __name__ == '__main__':
    n = int(input('Numero a evaluar la conjetura: '))
    lista = conjetura(n)
    print(lista)