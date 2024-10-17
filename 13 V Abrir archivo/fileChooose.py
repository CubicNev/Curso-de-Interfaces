from tkinter import *
from tkinter import filedialog

root = Tk()


def abreFichero():
    fichero = filedialog.askopenfilename(title="Abrir", initialdir="C:", filetypes=(
        ("Ficheros de Exel", "*.xlsx"), ("Ficheros de texto", "*.txt"), ("Todos los ficheros", "*.*")))
    # filetypes selecciona que tipo de archivos mostrar, se debe dar almenos dos opciones
    print(fichero)  # Imprime la ruta del archivo del archivo


Button(root, text="Abrir fichero", command=abreFichero).pack()

root.mainloop()
