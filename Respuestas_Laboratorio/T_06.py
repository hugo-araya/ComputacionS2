valor = int(input('Precio kilo manzana: '))
kilos = int(input('Kilos comprados: '))
pagar = valor * kilos
if kilos <= 2:
    pagar = valor * kilos
else:
    if kilos <=5:
        pagar = (valor*kilos)*0.9
    else:
        if kilos <= 10:
            pagar = (valor*kilos)*0.85
        else:
            pagar = (valor*kilos)*0.8
print('A pagar: ', pagar)
