valor_hora = int(input('Valor Hora: '))
horas_trabajadas = int(input('Horas Trabajadas: '))
if horas_trabajadas > 40 :
    extras = horas_trabajadas - 40
else:
    extras = 0
if extras > 8:
    adicional = extras - 8
else: 
    adicional = 0
if horas_trabajadas <= 40:
    sueldo = horas_trabajadas* valor_hora
else:
    if extras <= 8:
        sueldo = 40 * valor_hora + extras * 2* valor_hora
    else:
        sueldo = 40 * valor_hora + 8*2*valor_hora + (extras-8)*3*valor_hora
print('Sueldo: ', sueldo)

