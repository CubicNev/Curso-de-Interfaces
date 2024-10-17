from tkinter import *

# UI
root = Tk()

root.title("Ejemplo")

# Para funcionalidad
playa = IntVar()
mointain = IntVar()
turismoR = IntVar()

def opcionesViaje():
    opcionEscogida=""
    if(playa.get()==1):
        opcionEscogida += "Playa"
    
    if(mointain.get()==1):
        opcionEscogida += "Montaña"
    
    if(turismoR.get()==1):
        opcionEscogida += "Turismo Rural"

    textoFinal.config(text=opcionEscogida)

# UI

foto=PhotoImage(file="xd.png")
Label(root, image=foto).pack()

frame = Frame(root)
frame.pack()

Label(frame)

Label(frame, text="Elige destinos", width=50).pack()

Checkbutton(frame, text="Playa", variable=playa, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame, text="Montaña", variable=mointain, onvalue=1, offvalue=0, command=opcionesViaje ).pack()
Checkbutton(frame, text="Turismo rural", variable=turismoR, onvalue=1, offvalue=0, command=opcionesViaje).pack()
# Con onvalue y offvalue cambia los valores de la variable cuando se selecciona o se deselecciona

textoFinal = Label(frame)
textoFinal.pack()


root.mainloop()
