#Utilizacion de widget menu para hacer una barra de menú

from tkinter import *
from tkinter import messagebox

root=Tk()

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

barraMenu = Menu(root)
root.config(menu=barraMenu, width=300, height=300)

archivoMenu = Menu(barraMenu, tearoff=0) # tearoff quita la primera opcion default
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar como")
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar", command=cerrarDocumento)
archivoMenu.add_command(label="Salir", command=salirApp)

archivoEdic = Menu(barraMenu, tearoff=0)
archivoEdic.add_command(label="Copiar")
archivoEdic.add_command(label="Cortar")
archivoEdic.add_command(label="Pegar")

archivoHerr = Menu(barraMenu, tearoff=0)

archivoAyud = Menu(barraMenu, tearoff=0)
archivoAyud.add_command(label="Licencia", command=avisoLicencia)
archivoAyud.add_command(label="Acerca de...", command=infoAdicional)

barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Edicion", menu=archivoEdic)
barraMenu.add_cascade(label="Herramientas", menu=archivoHerr)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyud)

root.mainloop()
