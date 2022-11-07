def funcion1(x):
    resultado = 2*x + 1
    return resultado

def funcion2(x):
    resultado = x * x
    return resultado

y = funcion2(funcion1(7))
print(y)

