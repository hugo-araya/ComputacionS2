'''Calcular el total que una persona debe pagar en una serviteca, 
si el precio de cada neumático es de $800 si se compran menos de 5 
neumáticos y de $700 si se compran 5 o más.'''

cantidad_neumaticos = int(input('Cantidad de neumaticos: '))
if cantidad_neumaticos < 5:
    total = cantidad_neumaticos * 800
else:
    total = cantidad_neumaticos * 700
print('Monto a pagar: ', total)


