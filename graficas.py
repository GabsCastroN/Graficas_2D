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

#linea
linea =c.create_line(BASE/2, ALTURA/2, BASE,0, fill="Purple", width=3)
linea2= c.create_line(BASE, ALTURA, BASE/2, ALTURA/2, fill="Orange")
linea3=c.create_line(0,ALTURA,BASE/2,ALTURA/2, fill="Blue")
linea4= c.create_line(0,0, BASE/2, ALTURA/2, fill="green",width=3)

linea5=c.create_line(BASE/2, ALTURA/2, BASE/2, ALTURA, fill="Yellow")
linea6=c.create_line(BASE/2, ALTURA/2, BASE, ALTURA/2, fill="red")
linea7=c.create_line(BASE/2, ALTURA/2, BASE/2, 0, fill="white")
linea8=c.create_line(BASE/2, ALTURA/2,0, ALTURA/2, fill="Pink")

#Dibujar texto
texto1=c.create_text(BASE/4, ALTURA/2, anchor="center", text="Sistemas :D", font=("Arial", 25, "bold"), fill="blue",activefill="Purple")

texto2=c.create_text(3*BASE/4, ALTURA/2, anchor="center", text="Colegio", font=("Arial", 25, "bold"), fill="blue",activefill="Purple")

texto3=c.create_text(BASE/2, ALTURA/4, anchor="center", text="Especialidad", font=("Arial", 25, "bold"), fill="blue",activefill="Purple")

texto3=c.create_text(BASE/2, 3*ALTURA/4, anchor="center", text="Guanenta", font=("Arial", 25, "bold"), fill="blue",activefill="Purple")

#Dibujar Rectangulo
Recan=c.create_rectangle(BASE/2,ALTURA/2,BASE,ALTURA,fill="Yellow", outline="Blue")
ventana_principal.mainloop()

