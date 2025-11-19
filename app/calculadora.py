import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# creacion de la ventana
ventana = tk.Tk()
ventana.title("Calculadora Básica")
ventana.config(bg="black")
ventana.geometry("383x280+250+100")
ventana.resizable(False, False)
ventana.iconbitmap("image/imagen_calculadora.ico")

# funcion para calcular
def calcular():
    try:
        resultado = eval(entrada.get()) # toma el texto de entrada eval resuelve la operacion
        entrada.delete(0, tk.END) # borra el texto de entry
        entrada.insert(tk.END, str(resultado)) # inserta el resultado
    except Exception as e:
        messagebox.showerror("Error", str(e))
        
ventana.bind("<Return>", lambda event: calcular())

# funcion para borrar con backspace
def  borrar_tecla(event):
    entrada.delete(len(entrada.get())-1, tk.END)
    
ventana.bind("<BackSpace>", lambda event: borrar_tecla(event))

# funcion de punto decimal
def punto_decimal(event):
        entrada.insert(tk.END, ".")
        
ventana.bind("<period>", lambda event: punto_decimal(event))

# funcion de resta
def resta(event):
    entrada.insert(tk.END, "-")

ventana.bind("<minus>", lambda event: resta(event))

# funcion de miltiplicacion
def multiplicacion(event):
    entrada.insert(tk.END, "*")
    
ventana.bind("<*>", lambda event: multiplicacion(event))

# funcion de suma
def suma(event):
    entrada.insert(tk.END, "+")
    
ventana.bind("<+>", lambda event: suma(event))

# fumcion de division
def division(event):
    entrada.insert(tk.END, "/")
    
ventana.bind("<slash>", lambda event: division(event))

# funciones de evento
def presionar_tecla(event):
    if event.char in "0123456789":
        entrada.insert(tk.END, event.char)

ventana.bind("<Key>", presionar_tecla)
# Entrada de texto
entrada = tk.Entry(ventana, width=40, relief="sunken", font=("arial black", 10))
entrada.grid(row=0, column=0, columnspan=4)

# Botones
boton_1 = ttk.Button(ventana, text="*", width=10, command=lambda: entrada.insert(tk.END, "*"))
boton_1.grid(row=1, column=0, padx=5, pady=5, ipadx=8, ipady=10)

boton_2 = ttk.Button(ventana, text="+", width=10, command=lambda: entrada.insert(tk.END, "+"))
boton_2.grid(row=1, column=1, padx=5, pady=5, ipadx=8, ipady=10)

boton_3 = ttk.Button(ventana, text="0", width=10, command=lambda: entrada.insert(tk.END, "0"))
boton_3.grid(row=1, column=2, padx=5, pady=5, ipadx=8, ipady=10)

boton_4 = ttk.Button(ventana, text="<-", width=10, command=lambda: entrada.delete(len(entrada.get())-1,tk.END))
boton_4.grid(row=1, column=3, padx=5, pady=5, ipadx=8, ipady=10)

boton_5 = ttk.Button(ventana, text="7", width=10, command=lambda: entrada.insert(tk.END, "7"))
boton_5.grid(row=2, column=0, padx=5, pady=5, ipadx=8, ipady=10)

boton_6 = ttk.Button(ventana, text="8", width=10, command=lambda: entrada.insert(tk.END, "8"))
boton_6.grid(row=2, column=1, padx=5, pady=5, ipadx=8, ipady=10)

boton_7 = ttk.Button(ventana, text="9", width=10, command=lambda: entrada.insert(tk.END, "9"))
boton_7.grid(row=2, column=2, padx=5, pady=5, ipadx=8, ipady=10)

boton_8 = ttk.Button(ventana, text="-", width=10, command=lambda: entrada.insert(tk.END, "-"))
boton_8.grid(row=2, column=3, padx=5, pady=5, ipadx=8, ipady=10)

boton_9 = ttk.Button(ventana, text="4", width=10, command=lambda: entrada.insert(tk.END, "4"))
boton_9.grid(row=3, column=0, padx=5, pady=5, ipadx=8, ipady=10)

boton_10 = ttk.Button(ventana, text="5", width=10, command=lambda: entrada.insert(tk.END, "5"))
boton_10.grid(row=3, column=1, padx=5, pady=5, ipadx=8, ipady=10)

boton_11 = ttk.Button(ventana, text="6", width=10, command=lambda: entrada.insert(tk.END, "6"))
boton_11.grid(row=3, column=2, padx=5, pady=5, ipadx=8, ipady=10)

boton_12 = ttk.Button(ventana, text="/", width=10, command=lambda: entrada.insert(tk.END, "/"))
boton_12.grid(row=3, column=3, padx=5, pady=5, ipadx=8, ipady=10)

boton_13 = ttk.Button(ventana, text="1", width=10, command=lambda: entrada.insert(tk.END, "1"))
boton_13.grid(row=4, column=0, padx=5, pady=5, ipadx=8, ipady=10)

boton_14 = ttk.Button(ventana, text="2", width=10, command=lambda: entrada.insert(tk.END, "2"))
boton_14.grid(row=4, column=1, padx=5, pady=5, ipadx=8, ipady=10)

boton_15 = ttk.Button(ventana, text="3", width=10, command=lambda: entrada.insert(tk.END, "3"))
boton_15.grid(row=4, column=2, padx=5, pady=5, ipadx=8, ipady=10)

boton_16 = ttk.Button(ventana, text="=", width=10, command=calcular)
boton_16.grid(row=4, column=3, padx=5, pady=5, ipadx=8, ipady=10)

boton_17 = ttk.Button(ventana, text=".", width=10, command=lambda: entrada.insert(tk.END, "."))
boton_17.grid(row=5, column=1, ipadx=8, ipady=10)

boton_18 = ttk.Button(ventana, text="C", width=10, command=lambda: entrada.delete(0, tk.END))
boton_18.grid(row=5, column=0, ipadx=8, ipady=10)

ventana.mainloop()

# gracias por usar mi calculadora :)
