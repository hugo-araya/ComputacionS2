# Leer p_interes, cap_inv
# saldo = cap_inv
# interes_calculado = cap_inv * p_interes 
# SI interes_calculado > 7000 entonces
# saldo = cap_inv + interes_calculado 
# Fin Si
# Escribir saldo
cap_inv = int(input('Capital a invertir: '))
p_interes = float(input('Interes: '))
interes_calculado = cap_inv * p_interes
if interes_calculado > 7000:
    saldo = cap_inv + interes_calculado
else:
    saldo = cap_inv
print('Saldo: ', saldo)