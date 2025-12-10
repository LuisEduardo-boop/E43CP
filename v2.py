import tkinter as tk
# aqui definimos las funciones 
def mostrar_ventana2():
    ventana1.withdraw() # oculte la pantalla 1
    ventana2.deiconify()# muestre la pantalla 2

def regresar():
    ventana2.withdraw() # oculte ventana  2
    ventana1.deiconify()# muestra ventana 1
#creacion de ventana 1
ventana1=tk.Tk()
label1=tk.Label( ventana1, text="ESTA ES MI VENTANA 1")
ventana1.geometry("600x400")
btn1=tk.Button(ventana1,text="IR A VENTANA 2 ")
btn1.pack()


#creacion de ventana 2
ventana2=tk.Tk()
label2=tk.Label( ventana2, text="ESTA ES MI VENTANA 2", command=regresar)
ventana2.geometry("600x400")
label2.pack()
btn2=tk.Button(ventana2,text="IR A VENTANA 1 ")
btn2.pack()

#creacion de la ventana 
ventana1.mainloop()