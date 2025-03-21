import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()

ventana.title("Unitecnar APP")
ventana.geometry("800x600")
ventana.resizable(True, True)

titulo = tk.Label(ventana, text="Login", font=("Times new roman", 22), fg="red")
titulo.pack()

nombre = tk.Label(ventana, text="Nombre").place(x=20, y=60)
txtNombre = tk.Entry(ventana)
txtNombre.place(x=130, y=60)

nickname = tk.Label(ventana, text="Nickname").place(x=20, y=100)
txtNickname = tk.Entry(ventana)
txtNickname.place(x=130, y=100)

clave = tk.Label(ventana, text="Clave").place(x=20, y=140)
txtClave = tk.Entry(ventana, show="*")
txtClave.place(x=130, y=140)


def registrar_usuario():
    nombre = txtNombre.get()
    nickname = txtNickname.get()
    clave = txtClave.get()
    
    if nombre and nickname and clave:
        messagebox.showinfo("Registro exitoso", f"Usuario {nickname} registrado correctamente")
        txtNombre.delete(0, tk.END)
        txtNickname.delete(0, tk.END)
        txtClave.delete(0, tk.END)
    else:
        messagebox.showwarning("Error", "Todos los campos son obligatorios")


btnRegistro = tk.Button(ventana, text="Registrarse", command=registrar_usuario)
btnRegistro.place(x=80, y=200)

ventana.mainloop()