# Creacion de la interfaz grafica de una calculadora
from tkinter import *

# ------------------------ Ventana ------------------------ #
VentRaiz = Tk()

# ------------------------ Frame contenedor ------------------------ #
FrameConte = Frame(VentRaiz)
FrameConte.pack() # Recordar que con el empaquetado el tamaño se adapta a lo que contiene

# ------------------------ Componentes ------------------------ #
# ---------- Pantalla ---------- #
pantalla = Entry(FrameConte)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(background="gray", fg="white", justify="right")
# columnspan para que la columna ocupe varias columnas en el Grid

#---------- Fila 1 de botones ---------- #
btn7 = Button(FrameConte, text="7", width=3)
btn7.grid(row=2, column=1)
btn8 = Button(FrameConte, text="8", width=3)
btn8.grid(row=2, column=2)
btn9 = Button(FrameConte, text="9", width=3)
btn9.grid(row=2, column=3)
btnDiv = Button(FrameConte, text="/", width=3)
btnDiv.grid(row=2, column=4)

#---------- Fila 2 de botones ---------- #
btn4 = Button(FrameConte, text="4", width=3)
btn4.grid(row=3, column=1)
btn5 = Button(FrameConte, text="5", width=3)
btn5.grid(row=3, column=2)
btn6 = Button(FrameConte, text="6", width=3)
btn6.grid(row=3, column=3)
btnMult = Button(FrameConte, text="x", width=3)
btnMult.grid(row=3, column=4)

#---------- Fila 3 de botones ---------- #
btn1 = Button(FrameConte, text="4", width=3)
btn1.grid(row=4, column=1)
btn2 = Button(FrameConte, text="2", width=3)
btn2.grid(row=4, column=2)
btn3 = Button(FrameConte, text="3", width=3)
btn3.grid(row=4, column=3)
btnRest = Button(FrameConte, text="-", width=3)
btnRest.grid(row=4, column=4)

#---------- Fila 4 de botones ---------- #
btnPunt = Button(FrameConte, text=".", width=3)
btnPunt.grid(row=5, column=1)
btn0 = Button(FrameConte, text="0", width=3)
btn0.grid(row=5, column=2)
btnIgu = Button(FrameConte, text="=", width=3)
btnIgu.grid(row=5, column=3)
btnSum = Button(FrameConte, text="+", width=3)
btnSum.grid(row=5, column=4)

# ------------------------ bucle ------------------------ #
VentRaiz.mainloop()
