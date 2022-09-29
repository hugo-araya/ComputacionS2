i = 0
c_pos = 0
c_neg = 0
c_neu = 0
while i < 20:
    numero = int(input('Numero: '))
    if numero > 0:
        c_pos = c_pos + 1
    else:
        if numero < 0:
            c_neg = c_neg + 1
        else:
            c_neu = c_neu + 1
    i = i + 1
print('Positivos = ', c_pos)
print('Negativos = ', c_neg)
print('Neutros   = ', c_neu)