import tkinter as tk
import sys

class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk()

        self.label1 = tk.Label(self.ventana1, text="Valor 1:")
        self.label1.grid(column=0, row=0)
        self.entry1 = tk.Entry(self.ventana1)
        self.entry1.grid(column=0, row=1)

        self.label2 = tk.Label(self.ventana1, text="Valor 2:")
        self.label2.grid(column=0, row=2)
        self.entry2 = tk.Entry(self.ventana1)
        self.entry2.grid(column=0, row=3)

        self.boton_cambiar_tamano = tk.Button(self.ventana1, text="Cambiar tamaño", command=self.cambiar_tamano)
        self.boton_cambiar_tamano.grid(column=0, row=4)

        self.boton_salir = tk.Button(self.ventana1, text="Salir", command=self.salir)
        self.boton_salir.grid(column=0, row=5)

        self.ventana1.mainloop()

    def cambiar_tamano(self):
        valor1 = int(self.entry1.get())
        valor2 = int(self.entry2.get())
        self.ventana1.geometry(f"{valor1}x{valor2}")

    def salir(self):
        sys.exit()
        
aplicacion = Aplicacion()
