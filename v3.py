import tkinter as tk 
from tkinter import messagebox

class VentanaInicio:
    def __init__(self):
        self.ventana=tk.Tk()
        self.ventana.title("Bienvenidos a el test de adicción a TikTok")
        self.ventana.geometry("600x800")

        etiqueta= tk.Label(self.ventana,text="Bienvenido al sistema de registro y test")
        etiqueta.pack()

        boton_registro= tk.Button(self.ventana, text="registro",command=self.abrir_ventana_registro)
        boton_registro.pack()

        boton_test= tk.Button(self.ventana, text="test",command=self.abrir_test)
        boton_test.pack()

    def abrir_ventana_registro(self):
        self.ventana.destroy()
        Ventana_Registro=Ventana_Registro()
        