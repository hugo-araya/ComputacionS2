def es_palindromo(palabra):
    palabra2 = ""
    i = -1
    while i >= -len(palabra):
        palabra2 = palabra2 + palabra[i]
        i =i - 1
    if palabra == palabra2:
        ok = True
    else:
        ok = False
    return ok

if __name__ == '__main__':
    palabra = 'reconocer'
    retorno = es_palindromo(palabra)
    if retorno == True:
        print('La palabra es palindroma')
    else:
        print('No es palindroma')

