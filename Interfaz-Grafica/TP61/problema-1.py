import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.seleccion1=tk.IntVar()
        self.seleccion2=tk.IntVar()
        self.seleccion3=tk.IntVar()
        self.label1=tk.Label(self.ventana1, text="Seleccione un navegador")        
        self.label1.grid(column=0, row=0)
        self.check1=tk.Checkbutton(self.ventana1, text="Google", variable=self.seleccion1)
        self.check1.grid(column=0, row=1)
        self.check2=tk.Checkbutton(self.ventana1, text="Brave", variable=self.seleccion2)
        self.check2.grid(column=0, row=2)
        self.check3=tk.Checkbutton(self.ventana1, text="Firefox", variable=self.seleccion3)
        self.check3.grid(column=0, row=3)
        self.label2=tk.Label(self.ventana1, text="")
        self.label2.grid(column=0, row=4)
        self.boton1=tk.Button(self.ventana1, text="Mostrar seleccionado", command=self.mostrarseleccionado)
        self.boton1.grid(column=0, row=5)
        self.ventana1.mainloop()


    def mostrarseleccionado(self):
        string = ''
        if self.seleccion1.get():
            string += "Google -"
        if self.seleccion2.get():
            string += "Brave -"
        if self.seleccion3.get():
            string += "Firefox -"
        self.label2.configure(text=string)

aplicacion1=Aplicacion()