# Manipulacion de labels
from tkinter import *

# ---------- Ventana ---------- #
v = Tk()

# --------- Frame contenedor ---------- #
frame = Frame(v, width=500, height=400)
frame.pack()

# --------- Label ---------- #
Label(frame, text="Este es un label", fg="red", font=("Comic Sans MS", 18)).place(x=100, y=200)

# --------- bucle ---------- #
v.mainloop()
