import tkinter as tk
def funcion():
 nombre = entrada.get()
 edad = entrada2.get()
 eti_resultado.config(text=f"Hola {nombre} bienvenido, tienes {edad}")

ventana = tk.Tk()
ventana.title("Ventana Lectora de Nombre y Edad")
ventana.geometry("600x300")
ventana.config(bg="gray")


eti1 = tk.Label(ventana, text="Introduce tu usuario:")
eti1.pack()
entrada = tk.Entry(ventana)
entrada.pack()

eti2 = tk.Label(ventana, text="Tu edad es:")
eti2.pack()
entrada2 = tk.Entry(ventana)
entrada2.pack()

boton = tk.Button(ventana, text="Iniciar", command=funcion)
boton.pack()

eti_resultado = tk.Label (ventana, text="")
eti_resultado.pack()

marca= tk.Label(ventana, text="Derechos de autor para Oziel Avila Guerra")
marca.pack(side="bottom",fill="x")

ventana.mainloop()