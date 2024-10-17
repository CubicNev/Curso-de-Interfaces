# Formulario más avanzado
# Text - Mucho texto
# Boton - interactuar

from tkinter import *

# ---------- Ventana ---------- #
v = Tk()

# --------- Frame contenedor ---------- #
fr = Frame(v, width=1200, height=600) 
fr.pack()

miNombre = StringVar() # Variable de tipo string

# --------- Entry ---------- #
nomE = Entry(fr, textvariable=miNombre) # Asocio una variable para el contenido del cuadro
nomE.grid(row=0, column=1, padx=10, pady=10)
nomE.config(fg="red", justify="center")

apeE = Entry(fr)
apeE.grid(row=1, column=1, padx=10, pady=10)

dirE = Entry(fr)
dirE.grid(row=2, column=1, padx=10, pady=10)

passE = Entry(fr)
passE.grid(row=3, column=1, padx=10, pady=10)
passE.config(show="*") # Sustituye lo que se muestra por el caracter especificado

# --------- Text ---------- #

comText = Text(fr, width=16, height=5)
comText.grid(row=4, column=1, padx=10, pady=10)

#Agrego una scrollbar vertical al text
scrollVert = Scrollbar(fr, command=comText.yview)
# scrollVert.grid(row=4, column=2) # La coloca alado del text segun el grid
scrollVert.grid(row=4, column=2, sticky="nsew") # Adapta a las dimensiones del text (widget al que pertenece)
# Para indicar al usuario en donde se encuentra dentro del Text
comText.config(yscrollcommand=scrollVert.set)

# --------- Label ---------- #
nomL = Label(fr, text="Nombre:")
nomL.grid(row=0,column=0, sticky="e", padx=10, pady=10)

apeL = Label(fr, text="Apellido:")
apeL.grid(row=1,column=0, sticky="e", padx=10, pady=10)

dirL = Label(fr, text="Direccion:")
dirL.grid(row=2,column=0, sticky="e", padx=10, pady=10)

passL = Label(fr, text="Password:")
passL.grid(row=3,column=0, sticky="e", padx=10, pady=10)

comL = Label(fr, text="Comentarios:")
comL.grid(row=4,column=0, sticky="e", padx=10, pady=10)

# --------- Button ---------- #
# Funcion del bton
def codigoBoton():
    miNombre.set("Carlos") # Pone texto en el cuadro (Entry) nomE
    # Con set se establece un valor a una variable, y paralelamente se usa get para traer el valor de una variable

# Maquetado
btnEnv = Button(v, text="Enviar", command=codigoBoton)
# Con command le asocio una funcion al boton
btnEnv.pack()


# --------- bucle ---------- #
v.mainloop()
