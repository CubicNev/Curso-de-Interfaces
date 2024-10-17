# Labels con imagenes
# Para manejar imagenes, utilizar png y gif
from tkinter import *

# ---------- Ventana ---------- #
v = Tk()

# --------- Frame contenedor ---------- #
frame = Frame(v, width=500, height=400) 
frame.pack()

# --------- Labels ---------- #
miImagen = PhotoImage(file="/6.png") # Clase para traer y manipular imagenes

Label(frame, image=miImagen).place(x=100, y=200)

# --------- bucle ---------- #
v.mainloop()
