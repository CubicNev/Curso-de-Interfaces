# Creacion y configuración de frames
from tkinter import *

# Declaracion de la ventana
ventana = Tk()

#----------- Configuracion de la ventana -----------#
ventana.title("Ventana de pruebas") # Titulo 
ventana.iconbitmap("Twitter.ico") # Icono
# ventana.geometry("650x350") # La raiz se adapta al tamaño de su contenedor interno (frame)
ventana.config(bg="black") # Color de fondo

#----------- Frame -----------#
miF = Frame() # Creacion

# Empaquetado = meter dentro de algo
miF.pack() # Lo meto dentro de la raiz
#   con .pack(side=right) se ancla a la parte derecha de la ventana
#       bottom, left, top
#   agragando tambien el param "anchor" podemos especificar dos lados a los cuales anclar
#       North, South, East, West
# miF().pack(side="left", anchor="n") # Arriba a la izquierda
# Para redimensionar junto con la ventana hacer el empaqutado asi: miF.pack(fill="x")
#  se adapta solo en x.
#       x-horizontal, y-vertical [pero junto con expand=true en el segundo parametro]
#       both-ambos lados pero se debe usar expand
# miF.pack(fill="both", expand="True")

miF.config(bg="gray") # Le doy color pero no se muestra porque no tiene tamaño
miF.config(width="650", height="350") # Un frame tiene un tamaño fijo por default
miF.config(bd=35)# Cambio el grosor del borde. El default es 0
miF.config(relief="sunken")# Le cambio el tipo de borde
miF.config(cursor="pirate")# Cambio el cursor cuando esta sobre el frame

# Nota todo lo aplicado al frame con config se le puede aplicar tambien a la raiz,
# No tiene sentido cambiarle el ancho y largo porque se adapta al contenido
# ventana.config(bd=45)
# ventana.config(relief="groove")
# ventana.config(cursor="hand2")

#----------- Ejecucion continua -----------#
ventana.mainloop() 

