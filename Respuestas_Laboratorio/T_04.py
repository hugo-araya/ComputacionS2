edad = int(input('Edad: '))
antiguedad = int(input('Antiguedad: '))
if edad >= 60 and antiguedad < 25:
    print('Jubilacion por edad')
if edad < 60 and antiguedad <= 25:
    print('Jubilacion antiguedad joven' )
if edad >= 60 and antiguedad >= 25:
    print('Jubilacion antiguedad adulta')
    