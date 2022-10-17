sueldo = int(input('Sueldo: '))
antiguedad = int(input('Antiguedad: '))
if antiguedad < 1:
    pagar = sueldo + sueldo * 0.05
else:
    if antiguedad < 2:
        pagar = sueldo + sueldo * 0.07
    else:
        if antiguedad < 5:
            pagar = sueldo + sueldo * 0.1
        else:
            if antiguedad < 10:
                pagar = sueldo + sueldo * 0.15
            else:
                pagar = sueldo + sueldo * 0.2
print('A pagar: ', pagar)