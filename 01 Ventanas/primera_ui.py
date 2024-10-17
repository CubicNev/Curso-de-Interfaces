# Construccion de una ventana
from tkinter import *

# Declaracion de la ventana
ventana = Tk()

#----------- Configuracion de la ventana -----------#
ventana.title("Ventana de pruebas") # Titulo de la ventana

ventana.resizable(1,0) # Activa/Desactiva el cambiar el tamaño manualmente
#   (ancho=0, alto=0) no se puede redimencionar en ninguna dimension
#   o (False, False)

ventana.iconbitmap("Twitter.ico") # Cambiar el icono de la ventana

ventana.geometry("650x350") # Cambia tamaño por defecto de la ventana Ancho x Alto

# El metodo config sirve para varias cosas
ventana.config(bg="black") # Ej: Cambiar el color de fondo

# La ventana debe estar en un bucle infinito para ejecutarse y 100pre al ultimo
ventana.mainloop()

# Nota si se cambia la extension del archivo de .py a .pyw solo se abre la ventana y no la consola
