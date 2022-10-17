saldo = int(input('Saldo: '))
if saldo < 0:
    n_saldo = 10000000 + saldo *(-1)
if saldo >= 0 and saldo <= 10000000:
    n_saldo = 20000000 - saldo
if saldo > 20000000:
    n_saldo = saldo
print('Nuevo saldo: ', n_saldo)
e_computo = n_saldo - 5000000
n_saldo = n_saldo - 5000000
mobiliario = n_saldo - 2000000
n_saldo = n_saldo - 2000000
insumos = n_saldo / 2
personal = n_saldo / 2
print('Insumos: ', insumos)
print('Personal: ', personal)
