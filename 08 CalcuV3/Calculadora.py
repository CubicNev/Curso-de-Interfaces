# Creacion de la interfaz grafica de una calculadora con funcionalidad
# Se ocupan llamadas a funciones
# Funciones lambda
from tkinter import *

# ------------------------ Ventana ------------------------ #
VentRaiz = Tk()

# ------------------------ Frame contenedor ------------------------ #
FrameConte = Frame(VentRaiz)
FrameConte.pack() # Recordar que con el empaquetado el tamaño se adapta a lo que contiene

# Variables globales
operacion=""
resultado=0

# ------------------------ Componentes ------------------------ #
# ---------- Pantalla ---------- #
numeroPantalla=StringVar()

pantalla = Entry(FrameConte, textvariable=numeroPantalla)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(background="gray", fg="white", justify="right")

# ---------- Funcion para el numero que se presiono ---------- #
def numeroPulsado(num):
    global operacion # Trabajo con la variable glogal operacion
    if operacion != "": # Si ha presioado un operador
        operacion = "" 
        numeroPantalla.set(num) # no concatena
    else:# Si no se ha presionado un operador
        numeroPantalla.set(numeroPantalla.get() + num) 

# ---------- Funcion para hacer una suma  ---------- #
def suma(num):
    global operacion
    global resultado

    resultado += int(num)
    operacion = "suma" # Digo que se esta haciendo suma

    numeroPantalla.set(resultado)

# ----------  Funcion para igual  ---------- #
def igual():
    global resultado
    numeroPantalla.set(resultado+int(numeroPantalla.get()))
    resultado = 0 # Reinicia el resultado

#---------- Fila 1 de botones ---------- #
btn7 = Button(FrameConte, text="7", width=3, command=lambda:numeroPulsado("7"))
btn7.grid(row=2, column=1)
btn8 = Button(FrameConte, text="8", width=3, command=lambda:numeroPulsado("8"))
btn8.grid(row=2, column=2)
btn9 = Button(FrameConte, text="9", width=3, command=lambda:numeroPulsado("9"))
btn9.grid(row=2, column=3)
btnDiv = Button(FrameConte, text="/", width=3)
btnDiv.grid(row=2, column=4)

#---------- Fila 2 de botones ---------- #
btn4 = Button(FrameConte, text="4", width=3, command=lambda:numeroPulsado("4"))
# con command=numeroPulsado("4") hace la llamada de funcion automaticamente, no se llama cuando quiero
btn4.grid(row=3, column=1)
btn5 = Button(FrameConte, text="5", width=3, command=lambda:numeroPulsado("5"))
btn5.grid(row=3, column=2)
btn6 = Button(FrameConte, text="6", width=3, command=lambda:numeroPulsado("6"))
btn6.grid(row=3, column=3)
btnMult = Button(FrameConte, text="x", width=3)
btnMult.grid(row=3, column=4)

#---------- Fila 3 de botones ---------- #
btn1 = Button(FrameConte, text="1", width=3, command=lambda:numeroPulsado("1"))
btn1.grid(row=4, column=1)
btn2 = Button(FrameConte, text="2", width=3, command=lambda:numeroPulsado("2"))
btn2.grid(row=4, column=2)
btn3 = Button(FrameConte, text="3", width=3, command=lambda:numeroPulsado("3"))
btn3.grid(row=4, column=3)
btnRest = Button(FrameConte, text="-", width=3)
btnRest.grid(row=4, column=4)

#---------- Fila 4 de botones ---------- #
btnPunt = Button(FrameConte, text=".", width=3, command=lambda:numeroPulsado("."))
btnPunt.grid(row=5, column=1)
btn0 = Button(FrameConte, text="0", width=3, command=lambda:numeroPulsado("0"))
btn0.grid(row=5, column=2)
btnClr = Button(FrameConte, text="CLR", width=3)
btnClr.grid(row=5, column=3)
btnSum = Button(FrameConte, text="+", width=3, command=lambda:suma(numeroPantalla.get()))
btnSum.grid(row=5, column=4)

#---------- Fila 5 BTN IGUAL ---------- #
btnIgu = Button(FrameConte, text="=", width=3, command=lambda:igual())
btnIgu.grid(row=6, column=1, columnspan=4, sticky="nsew")

# ------------------------ bucle ------------------------ #
VentRaiz.mainloop()
