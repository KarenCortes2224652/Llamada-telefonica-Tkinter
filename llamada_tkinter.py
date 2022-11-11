# Se importa libreria tkinter con todas sus funciones

from tkinter import *
from tkinter import messagebox

# Funciones de la app

def Tiempo():
    messagebox.showinfo("Tiempo de duración de la llamada", "Hizo clic en el botón Tiempo...")
    z = int(x.get()) + int(y.get())
    t_resultados.insert(INSERT, "La suma de " + x.get()+ " + " +y.get()+" casi siempre es "+str(z)+"\n")

def Borrar():
    messagebox.showinfo("Suma 1.0", "Los datos serán borrados...")
    x.set("")
    y.set("")
    t_resultados.delete("1.0","end")

def Salir():
    messagebox.showinfo("Suma 1.0", "La app se cerrará...")
    ventana_principal.destroy()

# Variables globales 

# Ventana principal

# Se crea una variable llamada ventana_principal, que adquiere las caracteristiccas de un objeto Tk
ventana_principal = Tk()

# Título de la ventana
ventana_principal.title("TIEMPO LLAMADA TELEFÓNICA")

# Tamaño de la ventana, ancho y alto
ventana_principal.geometry("500x500")

# Deshabilitar el boton de maximizar
ventana_principal.resizable(0,0)

# Color de la ventana
ventana_principal.config(bg="black")

x = StringVar()
y = StringVar()

#--------------------
# Frame entrada datos
#--------------------

frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg = "aquamarine2", width = 480 , height = 240)
frame_entrada.place(x = 10, y = 10)

# Logo de la App
logo = PhotoImage(file="img/llamada.png")
lb_logo = Label(frame_entrada, image=logo)
lb_logo.place(x=10, y=10)

# Etiquetas par el titulo de app
titulo = Label(frame_entrada, text = "CALCULAR DURACIÓN EN UNA LLAMADA")
titulo.config(bg = "aquamarine2", fg = "black", font = ("Arial",16))
titulo.place(x = 30, y = 10)

# Etiqueta para tiempo
lb_x = Label(frame_entrada, text = "Duración: ")
lb_x.config(bg="aquamarine2", fg="black", font=("Arial",16))
lb_x.place(x=220, y=70, width=115, height=30)

# Entry para tiempo
entry_x = Entry(frame_entrada, textvariable=x)
entry_x.config(font=("Arial",25), justify=LEFT,fg="black")
entry_x.focus_set()
entry_x.place(x=330, y=70, width=115, height=30)

#--------------------
# Frame operaciones
#--------------------

frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg = "aquamarine2", width = 480 , height = 120)
frame_operaciones.place(x = 10, y = 260)

# Botón para sumar
bt_tiempo = Button(frame_operaciones, text="TIEMPO", command=Tiempo)
bt_tiempo.place(x=45, y=45, width=100, height=30)

# Botón borrar
bt_tiempo = Button(frame_operaciones, text="BORRAR",command=Borrar)
bt_tiempo.place(x=190, y=45, width=100, height=30)

# Botón salir
bt_salir = Button(frame_operaciones, text="SALIR",command=Salir)
bt_salir.place(x=335, y=45, width=100, height=30)

# Frame resultados
frame_resultados = Frame(ventana_principal)
frame_resultados.config(bg="aquamarine2", width=480, height=100)
frame_resultados.place(x=10, y = 390)

# Área de texto para resultados
t_resultados = Text(frame_resultados)
t_resultados.config(bg="SlateGray1", fg="black", font=("Arial",20))
t_resultados.place(x=10,y=10, width=460, height= 80)

ventana_principal.mainloop()