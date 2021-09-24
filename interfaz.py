from multiproceso import procesarListaLink as Procesar
import os
from tkinter import Entry, Button, Label, Tk, Text, StringVar


ventana = Tk()
mensajeTxt = Text(ventana, width=30, height=10)

def enviarDatos():
    global mensajeTxt
    mensaje = mensajeTxt.get(1.0,"end-1c")
    print(mensaje)
    links = mensaje.split()
    print(links)
    Procesar(links)

ventana.title("Proyecto Ricoloso")
Label(text="Ingrese links de Youtube", fg="gray", font=("Verdana", 12)).grid(row=0, column=0, sticky="e",padx=5,pady=10)
mensajeTxt.grid(row=1, column=0)
botonEnviar = Button(ventana, text="Enviar Datos", fg="black", font=("Verdana", 14), command=enviarDatos)
botonEnviar.grid(row=7,column=0,padx=20,pady=20)

def Ventana(is_child):
    global ventana
    ventana.mainloop()
    ventana.destroy()

""" 
Ventana(False)

i = 0
while i < len(links):
    print(links[i])
    i = i + 1 """
'''
links = []

link = input("Ingrese el link (Si no desea ingresar mas presione ''salir''): ")
while link != "salir":
    links.append(link)
    link = input("Ingrese el link (Si no desea ingresar mas presione ''salir''): ")

'''