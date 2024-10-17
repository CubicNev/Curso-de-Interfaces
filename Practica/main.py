
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

def infoAdicional():
    messagebox.showinfo("Cabecera", "Informacion de la ventana")

def avisoLicencia():
    messagebox.showwarning("Titulo", "Descripcion del aviso")

def salirApp():
    #valor = messagebox.askquestion("Titulo", "Pregunta")
    #if valor == "yes":
    #    root.destroy()
    valor = messagebox.askokcancel("Titulo", "Pregunta")

    if valor == True:
        root.destroy()

def cerrarDocumento():
    valor=messagebox.askretrycancel("Reintentar", "No es posible cerrar. Documento en uso")
    if valor==True:
        root.destroy()

def abreFichero():
    fichero = filedialog.askopenfilename(title="Abrir", initialdir="C:", filetypes=(
        ("Ficheros de Exel", "*.xlsx"), ("Ficheros de texto", "*.txt"), ("Todos los ficheros", "*.*")))
    # filetypes selecciona que tipo de archivos mostrar, se debe dar almenos dos opciones
    #print(fichero)  # Imprime la ruta del archivo del archivo
    ruta = str(fichero)
    miLabel.configure(text=ruta)

if __name__ == '__main__':
    root=Tk()

    barraMenu = Menu(root)
    root.config(menu=barraMenu, width=600, height=300)

    archivoMenu = Menu(barraMenu, tearoff=0) # tearoff quita la primera opcion default
    archivoMenu.add_command(label="Abrir",command=abreFichero)
    archivoMenu.add_separator()
    archivoMenu.add_command(label="Cerrar", command=cerrarDocumento)
    archivoMenu.add_command(label="Salir", command=salirApp)

    archivoAyud = Menu(barraMenu, tearoff=0)
    archivoAyud.add_command(label="Licencia", command=avisoLicencia)
    archivoAyud.add_command(label="Acerca de...", command=infoAdicional)

    barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
    barraMenu.add_cascade(label="Ayuda", menu=archivoAyud)

    # --------- Frame contenedor ---------- #
    frame = Frame(root)
    frame.pack()

    # --------- Label ---------- #
    miLabel = Label(frame, text="Abre un archivo")
    miLabel.grid(row=0, column=0, padx=50, pady=50)

    root.mainloop()