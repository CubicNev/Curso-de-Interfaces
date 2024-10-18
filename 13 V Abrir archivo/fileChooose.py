from tkinter import *
from tkinter import filedialog

root = Tk()
ruta = StringVar()

def abreFichero():
    fichero = filedialog.askopenfilename(title="Abrir", initialdir="C:", filetypes=(
        ("Ficheros de Exel", "*.xlsx"), ("Ficheros de texto", "*.txt"), ("Todos los ficheros", "*.*")))
    # filetypes selecciona que tipo de archivos mostrar, se debe dar almenos dos opciones
    print(fichero)  # Imprime la ruta del archivo del archivo
    ruta = str(fichero)
    miLabel.configure(text=ruta)


# --------- Frame contenedor ---------- #
frame = Frame(root, width=500, height=400) # Frame de 500x400 que esta dentro de una ventana
frame.pack()
# --------- Label ---------- #
miLabel = Label(frame, text="No hay archivos")
miLabel.place()
Button(root, text="Abrir fichero", command=abreFichero).pack()

root.mainloop()
