"""  Calcular el total que una persona debe pagar en una serviteca, si el 
precio de cada neumático es de $800 si se compran menos de 5 neumáticos 
y de $700 si se compran 5 o más. """

cant_neumaticos = int(input('Cantidad de neumaticos: '))
if cant_neumaticos < 5:
    a_pagar = cant_neumaticos * 800
else:
    a_pagar = cant_neumaticos * 700
print('A pagar: ', a_pagar)
