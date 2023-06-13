import tkinter as tk
import sys

class Aplication:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.title("Varon o Mujer")
        self.label1=tk.Label(self.ventana1, text="Elija una opcion")
        self.label1.grid(column=0, row=0)
        self.label1.configure(foreground="blue")
        self.boton1=tk.Button(self.ventana1, text="Varon", command=self.varon)
        self.boton1.grid(column=0, row=1)
        self.boton2=tk.Button(self.ventana1, text="Mujer", command=self.mujer)
        self.boton2.grid(column=0, row=2)
        self.boton3=tk.Button(self.ventana1, text="Salir", command=self.salir)
        self.boton3.grid(column=0, row=3)
        self.ventana1.mainloop()

    def varon(self):
        self.ventana1.title("Varon")

    def mujer(self):
        self.ventana1.title("Mujer")

    def salir(self):
        self.label1.configure(text="Adios")
        sys.exit()

Aplicacion1=Aplication()