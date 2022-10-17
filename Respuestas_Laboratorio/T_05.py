precio = int(input('Precio: '))
marca = input('Marca: ')
if precio > 200000:
    precio = precio * 0.9
if marca == 'NOSY':
    precio = precio * 0.95
a_pagar = precio*1.19
print('A pagar: ', a_pagar)
