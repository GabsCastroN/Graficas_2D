from tkinter import *

BASE = 720
ALTURA = 480

#Ventana principal

ventana_principal = Tk()
ventana_principal.title("Graficas 2D")
ventana_principal.resizable(False,False)
ventana_principal.geometry("760x520")
ventana_principal.config(bg="white")


#Frame Graficacion

frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg="green", width=740, height=500)
frame_graficacion.place(x=10,y=10)

#Canvas

c = Canvas(frame_graficacion, width=BASE, height=ALTURA)
c.config(bg="black")
c.place(x=10,y=10)

linea5=c.create_line(BASE/2, ALTURA/2, BASE/2, ALTURA, fill="White")
linea6=c.create_line(BASE/2, ALTURA/2, BASE, ALTURA/2, fill="White")
linea7=c.create_line(BASE/2, ALTURA/2, BASE/2, 0, fill="white")
linea8=c.create_line(BASE/2, ALTURA/2, 0, ALTURA/2, fill="White")



CuerpoTren = c.create_rectangle(BASE/2-100, ALTURA/2-50, BASE/2+125, ALTURA/2+50, fill="Purple")
Rue1 = c.create_oval(BASE/2-100, ALTURA/2+25, BASE/2-25, ALTURA/2+100, fill= "red")
Rue2 = c.create_oval(BASE/2-25, ALTURA/2+25, BASE/2+50, ALTURA/2+100, fill="blue")
Rue3 = c.create_oval(BASE/2+50, ALTURA/2+25, BASE/2+125, ALTURA/2+100, fill="green")
IniT = c.create_rectangle(BASE/2-120, ALTURA/2-40, BASE/2-100,ALTURA/2+45, fill="Orange")
FinT = c.create_rectangle(BASE)

ventana_principal.mainloop()