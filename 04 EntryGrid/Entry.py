"""
Entry = widget para introducir texto
Es como usar labels, tienen la misma sintaxis y casi las mismas opciones
"""
from tkinter import *

# ---------- Ventana ---------- #
v = Tk()

# --------- Frame contenedor ---------- #
fr = Frame(v, width=1200, height=600) 
fr.pack()

# --------- Entry ---------- #
CT = Entry(fr)
CT.place(x=100,y=100)

# --------- bucle ---------- #
v.mainloop()
