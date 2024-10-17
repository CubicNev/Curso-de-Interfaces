"""
Formulario con Grid
"""
from tkinter import *

# ---------- Ventana ---------- #
v = Tk()

# --------- Frame contenedor ---------- #
fr = Frame(v, width=1200, height=600) 
fr.pack()

# --------- Entry ---------- #
nomE = Entry(fr)
nomE.grid(row=0, column=1)
nomE.config(fg="red", justify="center")

apeE = Entry(fr)
apeE.grid(row=1, column=1)

dirE = Entry(fr)
dirE.grid(row=2, column=1)

passE = Entry(fr)
passE.grid(row=3, column=1)
passE.config(show="*") # Sustituye lo que se muestra por el caracter especificado

# --------- Label ---------- #
nomL = Label(fr, text="Nombre:")
nomL.grid(row=0,column=0, sticky="w", padx=10, pady=10)

apeL = Label(fr, text="Apellido:")
apeL.grid(row=1,column=0, sticky="w", padx=10, pady=10)

dirL = Label(fr, text="Direccion:")
dirL.grid(row=2,column=0, sticky="w", padx=10, pady=10)

passL = Label(fr, text="Password:")
passL.grid(row=3,column=0, sticky="w", padx=10, pady=10)
"""
sticky - Metodo para alinear elementos
Trabaja con puntos cardinales:
 N
W E
 S
y tiene puntos untermedios
nw N ne
W     E
sw S se

pad = padding - Para dar espacio entre elementos
    pady - padding vertical
    padx - ádding horizontal

"""

# --------- bucle ---------- #
v.mainloop()
