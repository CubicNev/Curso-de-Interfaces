#Utilizacion de widget menu para hacer una barra de menú

from tkinter import *

root=Tk()

barraMenu = Menu(root)
root.config(menu=barraMenu, width=300, height=300)

archivoMenu = Menu(barraMenu, tearoff=0) # tearoff quita la primera opcion default
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar como")
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar")
archivoMenu.add_command(label="Salir")

archivoEdic = Menu(barraMenu, tearoff=0)
archivoEdic.add_command(label="Copiar")
archivoEdic.add_command(label="Cortar")
archivoEdic.add_command(label="Pegar")

archivoHerr = Menu(barraMenu, tearoff=0)

archivoAyud = Menu(barraMenu, tearoff=0)
archivoAyud.add_command(label="Licencia")
archivoAyud.add_command(label="Acerca de...")

barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Edicion", menu=archivoEdic)
barraMenu.add_cascade(label="Herramientas", menu=archivoHerr)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyud)

root.mainloop()
