import tkinter as tk 

ventana = tk.Tk()

def teclado(evento):
    print(f"tecla presionada: {evento.keysym}")
    
ventana.bind("<KeyPress>", teclado)

ventana.mainloop()

# esto es una prueba de eventos en tkinter no influye en la calculadora