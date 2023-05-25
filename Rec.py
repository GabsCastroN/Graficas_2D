from tkinter import *

BASE = 460
ALTURA = 220

#Ventana principal

ventana_principal = Tk()
ventana_principal.title("Graficas 2D")
ventana_principal.resizable(False,False)
ventana_principal.geometry("500x500")
ventana_principal.config(bg="white")


#Frame Graficacion

frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg="green", width=480, height=240)
frame_graficacion.place(x=10,y=10)

#Canvas

c = Canvas(frame_graficacion, width=BASE, height=ALTURA)
c.config(bg="black")
c.place(x=10,y=10)

frame_controles = Frame(ventana_principal)
frame_controles.config(bg="green", width=480, height=230)
frame_controles.place(x=10, y=260)

Rec1 = c.create_rectangle(0, 0, BASE/4, ALTURA/2, fill="orange", outline="blue")
Rec2 = c.create_rectangle(BASE/4, ALTURA/2, 0, ALTURA, fill="white", outline="blue")
Rec3 = c.create_rectangle(BASE/4, ALTURA/2, BASE/2, ALTURA, fill="Purple", outline="blue")
Rec4 = c.create_rectangle(BASE/4, ALTURA/2, BASE/2, 0, fill="red", outline="blue")
Rec5 = c.create_rectangle(BASE/2, ALTURA/2, 3*BASE/4, ALTURA, fill="yellow", outline="blue")
Rec6 = c.create_rectangle(BASE/2, 0, 3*BASE/4, ALTURA/2, fill="blue", outline="purple")
Rec7 = c.create_rectangle(3*BASE/4, ALTURA/2, BASE, ALTURA, fill="Green", outline="Green")
Rec6 = c.create_rectangle(3*BASE/4, 0, BASE, ALTURA/2, fill="Purple", outline="purple")
ventana_principal.mainloop()