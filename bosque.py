hectareas = int(input('Cantidad de hectareas: '))
m2 = hectareas * 10000
if m2 <= 1000000:
    mp = m2 * 0.5
    me = m2 * 0.3
    mr = m2 * 0.2
else:
    mp = m2 * 0.7
    me = m2 * 0.2
    mr = m2 * 0.1
cp = mp * 8 / 10
ce = me * 15 / 15
cr = mr * 10 / 18
print('Cantidad de pinos     : ', int(cp))
print('Cantidad de eucaliptus: ', int(ce))
print('Cantidad de rauli     : ', int(cr))