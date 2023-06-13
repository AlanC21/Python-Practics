
import tkinter as tk
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.label1=ttk.Label(self.ventana1, text="Ingrese su nombre: ")
        self.label1.grid(column=0, row=0)
        self.nombre=tk.StringVar()
        self.entry1=ttk.Entry(self.ventana1, width=20, textvariable=self.nombre)
        self.entry1.grid(column=0, row=1)
        self.label2=ttk.Label(self.ventana1, text="Seleccione un país:")
        self.label2.grid(column=0, row=2)
        self.opcion=tk.StringVar()
        paises=("Argentina","Chile","Brasil","Uruguay","Colombia","Bolivia","Peru")
        self.combobox1=ttk.Combobox(self.ventana1, 
                                  width=10, 
                                  textvariable=self.opcion, 
                                  values=paises)
        self.combobox1.current(0)
        self.combobox1.grid(column=0, row=3)
        self.boton1=tk.Button(self.ventana1, text="Recuperar", command=self.recuperar)
        self.boton1.grid(column=0, row=4)
        self.label3=ttk.Label(self.ventana1, text="Día seleccionado:")
        self.label3.grid(column=0, row=5)
        self.ventana1.mainloop()

    def recuperar(self):
        self.label3.configure(text=self.nombre.get() + "-" + self.opcion.get())

aplicacion1=Aplicacion()