from tkinter import *

root = Tk()
root.geometry("900x500")  # Establecer el tamaño de la ventana

etiqueta = Label(root, text="Programado por Simón Castaño Correa.")
etiqueta.grid(row=1, column=0)

entry = Entry(root)
entry.grid(row=0, column=0)

def click_boton():
    texto = Label(root, text="No vuelvas a presionar el botón")
    texto.grid(row=1, column=1)
    entrada = entry.get()

    with open("datos.txt", "w") as archivo:
        archivo.write(entrada)

boton = Button(root, text="Presioname", bg="blue", padx=100, pady=25, command=click_boton)
boton.grid(row=0, column=2)

root.mainloop()
