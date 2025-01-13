"""
To-Do App v1
Autor: Carlos Nevárez - CubicNev
Fecha de creación: Thu 14-Nov-2024

Aplicación de escritorio que basada en objetos
"""

import tkinter as tk

class ToDo(tk.Tk):
    # Constructor: Crea la ventana y los contenedores
    def __init__(self, taks=None):
        super().__init__()

        # Inicializa una lista de tareas
        if not tasks:
            self.tasks = []
        else:
            self.tasks = taks
        # --- Configurando ventana ---
        self.title("To-Do App v1")
        self.geometry("300x400")

        # -- Componentes --
        # Tarea default (un poco asthetic)
        todo1 = tk.Label(self, text="--- Agrega tareas aqui ---" , bg="lightgrey", fg="black", pady=10)
        self.tasks.append(todo1)
        # Ciclo para empacar/agregar el elemento en la parte de arriba de la ventana, con un relleno horizontal (X)
        for task in self.tasks:
            task.pack(side=tk.TOP, fill=tk.X)

        # Cuadro de texto para escribir tareas (asthetic)
        self.task_create = tk.Text(self, height=3, bg="white", fg="black")
        # Se empaca en el fondo de la ventana rellenando horizontalmente
        self.task_create.pack(side=tk.BOTTOM, fill=tk.X)
        # Configura que el cursor este en el cuadro de texto al abrir la ventana
        self.task_create.focus_set()

        # Se vincula la tecla ENTER a la funcion add_item
        self.bind("<Return>", self.add_task)

    # Componente: Tarea
    def add_task(self, event=None):
        task_text = self.task

if __name__ == "__main__":
    root = ToDo()
    root.mainloop()