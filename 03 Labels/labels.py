# Manipulacion de labels
# -- Sintaxis --
#   variableLabel=Label(contenedor, opciones)
#   Tambien pueden mostrar IMAGENES
from tkinter import *

# ---------- Ventana ---------- #
v = Tk()

# --------- Frame contenedor ---------- #
frame = Frame(v, width=500, height=400) # Frame de 500x400 que esta dentro de una ventana
frame.pack()

# --------- Label ---------- #
miLabel = Label(frame, text="Este es un label")
# miLabel.pack() # Al utilizar el pack con el label, adapta el contendor a las dimensiones del label
# Permite colocar el label en cualquier lugar de la interfaz mediante las coordenadas x e y
miLabel.place(x=100, y=200)
#   x-distancia desde la izquierda y-distancia desde el borde de arriba
# Abreviacion: Label(frame, text="Este es un label").place(x=100, y=200) si no ocupamos la variable


# --------- bucle ---------- #
v.mainloop()
