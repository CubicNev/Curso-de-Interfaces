"""
Manejo del Grid para acomodar la interfaz en casillas ordenadas
Grid:
 _ _
|_|_| -> 00 | 01
|_|_|    10 | 11
"""
from tkinter import *

# ---------- Ventana ---------- #
v = Tk()

# --------- Frame contenedor ---------- #
fr = Frame(v, width=1200, height=600) 
fr.pack()

# --------- Entry ---------- #
CT = Entry(fr)
CT.grid(row=0, column=1) # Cambio place por grid(fila, columna)

# --------- Label ---------- #
nombre = Label(fr, text="Nombre:")
nombre.grid(row=0,column=0)

"""
Va a ocurrir lo mismo que con pack, no va arespetar las dimensiones de la interfaz
"""
# --------- bucle ---------- #
v.mainloop()
