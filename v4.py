#importar las bibliotecas
import tkinter as tk
from tkinter import ttk


#configuracion de todos los frames 
COLOR_FONDO = "#5A53BC"  
COLOR_MENU="#30458B"
COLOR_TEXTO="#FFFFFFD9"
FUENTE_TITULO=("Arial",16,"bold")
FUENTE_TEXTO=("Arial",12)

# ventana principal
root=tk.Tk()
root.title("software de deteccion de adicciones")
root.geometry("900x500")
root.config(bg=COLOR_FONDO)

#CONFIGURAMOS EL FRAME DEL MENU LATERAL
menu_frame=tk.Frame(root,bg=COLOR_MENU,width=200)
menu_frame.pack(side="left", fill="y")

#contenido del frame de la izquierda
contenido_frame=tk.Frame(root,bg=COLOR_FONDO)
contenido_frame.pack(side="right", fill="both", expand=True)
#funcion para cambiar a las siguientes ventanas 

def mostrar_pagina(nombre):
    for witget in contenido_frame.winfo_children():
        witget.destroy()
    paginas[nombre]()

#pagina bienvenida
def pagina_bienvenida():
    tk.Label(contenido_frame, text=" Bienvenido a la deteccion de adiccion a TIK TOK ",font=FUENTE_TITULO, bg=COLOR_FONDO).pack(pady=30)
    tk.Label(contenido_frame, text="Nos alegra darte la bienvenida a la detección de adicción a TikTok, es una herramienta para ayudarte a analizar y reducir tu adicción", bg=COLOR_FONDO, font=FUENTE_TEXTO).pack(pady=5)
    tk.Label(contenido_frame,text="Info : La adiccion a tiktok se refiere al uso execivo y compulsivo de la plataforma, que puede afectar negativamente la vida diaria , las relaciones y la salud mental de los usuarios ", bg=COLOR_FONDO, font=FUENTE_TEXTO).pack(pady=3)
#pagina de registro
def pagina_registro():
    tk.Label(contenido_frame, text="registro de usuario", font=FUENTE_TITULO, bg=COLOR_FONDO).pack(pady=20)
    for campo in ["nombre", "apellido", "fecha de nacimiento", "correo", "genero","numero telefonico"]:
        tk.Label(contenido_frame, text=f"{campo}:",bg=COLOR_FONDO, font=FUENTE_TEXTO).pack()
        tk.Entry(contenido_frame, width=40).pack(pady=20)
#pagina de test
def pagina_test():
    tk.Label(contenido_frame, text="test de adicciones", font=FUENTE_TITULO, bg=COLOR_FONDO).pack(pady=20)
    tk.Label(contenido_frame, text="responder las siguientes preguntas para conocer si tienes adiccion a tiktok", wraplength=600, bg=COLOR_FONDO).pack(pady=10)
    ttk.Button(contenido_frame, text="iniciar test").pack(pady=20)

#diccionario de las paginas

paginas={
"Bienvenida": pagina_bienvenida,
"Registro": pagina_registro,


"Test": pagina_test, 

}           

#botones de menu lateral
for nombre in paginas:
    ttk.Button(menu_frame, text=nombre, command=lambda n=nombre: mostrar_pagina(n)).pack(fill="x", pady=5, padx=10)

ttk.Button(menu_frame, text="salir", command=root).pack(side="bottom", pady=10)
#mandamos a llamar a la ventana
pagina_bienvenida()

root.mainloop()
