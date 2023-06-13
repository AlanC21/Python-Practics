import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.label1=tk.Label(self.ventana1, text="Ingrese un nombre")
        self.label1.grid(column=0, row=0)
        self.dato1=tk.StringVar()
        self.entry1=tk.Entry(self.ventana1, width=10, textvariable=self.dato1)
        self.entry1.grid(column=0, row=1)
        self.scroll1 = tk.Scrollbar(self.ventana1, orient=tk.VERTICAL)
        self.listbox1=tk.Listbox(self.ventana1, selectmode=tk.MULTIPLE, yscrollcommand=self.scroll1.set)
        self.listbox1.grid(column=0,row=2)
        self.scroll1.configure(command=self.listbox1.yview)         
        self.scroll1.grid(column=1, row=0, sticky='NS')        
        self.listbox1.insert(0,"Argentina")
        self.listbox1.insert(1,"Peru")
        self.listbox1.insert(2,"Bolivia")
        self.listbox1.insert(3,"Chile")
        self.listbox1.insert(4,"Brasil")
        self.listbox1.insert(5,"Uruguay")
        self.listbox1.insert(6,"Ecuador")
        self.listbox1.insert(7,"Colombia")
        self.boton1=tk.Button(self.ventana1, text="Recuperar", command=self.recuperar)
        self.boton1.grid(column=0, row=3)
        self.label2=tk.Label(self.ventana1,text="Seleccionado:")
        self.label2.grid(column=0, row=4)        
        self.ventana1.mainloop()

    def recuperar(self):
        if len(self.listbox1.curselection())!=0:
            todas=self.dato1.get()+' '
            for posicion in self.listbox1.curselection():
                todas+=self.listbox1.get(posicion)+"\n"
            self.label2.configure(text=todas)

aplicacion1=Aplicacion()    