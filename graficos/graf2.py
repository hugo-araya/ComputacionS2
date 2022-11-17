import matplotlib.pyplot as plt
x = [1,2,3,4,5,6,7,8,9]
y = [3,6,11,18,27,38,51,66,83]
plt.bar(x, y)
plt.title('Grafico de ejemplo')
plt.xlabel('Eje x')
plt.ylabel('Cuadrado')
plt.grid()
plt.show()