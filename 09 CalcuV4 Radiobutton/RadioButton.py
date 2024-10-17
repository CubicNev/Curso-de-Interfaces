from tkinter import *

root = Tk()

varOpcion = IntVar()

# Cambio dinamico de un label
def imprimir():
    # print(varOpcion.get())
    if varOpcion.get() == 1:
        etiqueta.config(text="Haz elegido maculino")
    elif varOpcion.get() == 2:
        etiqueta.config(text="Haz elegido femenino")
    else:
        etiqueta.config(text="Haz elegido otra opcion")


Label(root, text="Género:").pack()
Radiobutton(root, text="Masculino", variable=varOpcion,
            value=1, command=imprimir).pack()
Radiobutton(root, text="Femenino", variable=varOpcion,
            value=2, command=imprimir).pack()
Radiobutton(root, text="Otro", variable=varOpcion,
            value=3, command=imprimir).pack()

etiqueta = Label(root)
etiqueta.pack()

root.mainloop()
