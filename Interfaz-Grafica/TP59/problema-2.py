import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.label1=tk.Label(self.ventana1,text="Ingrese un usuario:")
        self.label1.grid(column=0, row=0)
        self.dato1=tk.StringVar()
        self.entry1=tk.Entry(self.ventana1, width=10, textvariable=self.dato1)
        self.entry1.grid(column=0, row=1)
        self.label2=tk.Label(self.ventana1,text="Ingrese una contraseña:")
        self.label2.grid(column=0, row=2)
        self.dato2=tk.StringVar()
        self.entry2=tk.Entry(self.ventana1, width=10, textvariable=self.dato2, show="*")
        self.entry2.grid(column=0, row=3)
        self.boton1=tk.Button(self.ventana1, text="Ingresar", command=self.ingresar)
        self.boton1.grid(column=0, row=4)
        self.label3=tk.Label(self.ventana1,text="")
        self.label3.grid(column=0, row=5)
        self.ventana1.mainloop()

    def ingresar(self):
        if(self.dato1.get()=="Juan" and self.dato2.get()=="1234"):
            self.label3.configure(text="Correcto")
        else:
            self.label3.configure(text="Incorrecto")
aplicacion1=Aplicacion()