print('CONVERTIDOR DE CENTIMETROS A KENS Y SHAKUs')
cm = int(input('Escriba la cantidad de centimetros: '))
shakus = cm / 30.3
kens = int(shakus / 6)
shakus = shakus - 6*kens
print(cm,'son',kens,'ken(s) y', shakus,'shaku(s)')
