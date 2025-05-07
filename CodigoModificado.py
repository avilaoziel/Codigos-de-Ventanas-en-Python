import tkinter as tk
def saludar():
 nombre = entrada.get()
 edad = entrada2.get()
 etiqueta_resultado.config(text=f"Hola {nombre} tienes {edad}")
 


ventana = tk.Tk()
ventana.title("Mi primera app grafica por Oziel")
ventana.geometry("400x200")

etiqueta = tk.Label(ventana, text="Ingresa tu nombre:")
etiqueta.pack()
entrada = tk.Entry(ventana)
entrada.pack()

etiqueta2 = tk.Label(ventana, text="ingresa tu edad:")
etiqueta2.pack()
entrada2 = tk.Entry(ventana)
entrada2.pack()

boton = tk.Button(ventana, text="Mostar saludo", command=saludar)
boton.pack()
etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.pack()

ventana.mainloop()