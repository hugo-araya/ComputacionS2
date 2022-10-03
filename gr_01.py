from tkinter import *

def lee_puntos(nombre):
    ar = open(nombre,"r")
    cantidad = int(ar.readline())
    puntos = []
    for i in range(cantidad):
        linea = ar.readline()
        punto = linea.split()
        puntos.append(punto)
    return puntos

def dibuja_nube_puntos(canvas, puntos):
    for i in range(len(puntos)):
            canvas.create_oval(int(puntos[i][0])-2, int(puntos[i][1])-2,int(puntos[i][0])+2, int(puntos[i][1])+2, width=1, fill='red')    

def dibuja_lineas(canvas, puntos):
    for i in range(len(puntos)-1):
        for j in range(i, len(puntos)):
            canvas.create_line(int(puntos[i][0]), int(puntos[i][1]),int(puntos[j][0]), int(puntos[j][1]), width=1, fill='blue')

def empezar():
    puntos = lee_puntos("puntos.txt")

    dibuja_nube_puntos(canvas, puntos)
    dibuja_lineas(canvas, puntos)    

if __name__ == "__main__": 
    ventana = Tk()
    ventana.title('Nube de Puntos')
    ventana.geometry("550x550+30+30")
    f1 = Frame(ventana)
    f2 = Frame(ventana)
    b1 = Button(f1, text="Ejecutar", bg="yellow", command=empezar, cursor = 'man')
    b1.pack(side="left")
    f1.pack(side="left")
    canvas = Canvas(f2, width=500, height=500, bg='white', cursor = 'trek')
    canvas.pack(expand=YES, fill=BOTH)
    f2.pack(side="left")
    ventana.mainloop()