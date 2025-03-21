import tkinter as tk
from tkinter import messagebox
from Clases.Usuarios import Usuarios

def guardar_usuario():
    nombre = entry_nombre.get()
    nickname = entry_nickname.get()
    clave = entry_clave.get()
    
    if nombre and nickname and clave:
        usuario = Usuarios()
        usuario.guardarUsuario(nombre, nickname, clave)
        messagebox.showinfo("Éxito", "Usuario guardado correctamente")
        entry_nombre.delete(0, tk.END)
        entry_nickname.delete(0, tk.END)
        entry_clave.delete(0, tk.END)
    else:
        messagebox.showwarning("Error", "Todos los campos son obligatorios")

def listar_usuarios():
    usuario = Usuarios()
    lista = usuario.listarUsuarios()
    panel_usuarios.config(state=tk.NORMAL)
    panel_usuarios.delete(1.0, tk.END)
    for u in lista:
        panel_usuarios.insert(tk.END, f"Nombre: {u['nombre']}, Nickname: {u['nickname']}, Clave: {u['clave']}\n")
    panel_usuarios.config(state=tk.DISABLED)


root = tk.Tk()
root.title("Gestión de Usuarios")


tk.Label(root, text="Nombre:").pack()
entry_nombre = tk.Entry(root)
entry_nombre.pack()

tk.Label(root, text="Nickname:").pack()
entry_nickname = tk.Entry(root)
entry_nickname.pack()

tk.Label(root, text="Clave:").pack()
entry_clave = tk.Entry(root, show="*")
entry_clave.pack()


btn_guardar = tk.Button(root, text="Guardar Usuario", command=guardar_usuario)
btn_guardar.pack()

btn_listar = tk.Button(root, text="Listar Usuarios", command=listar_usuarios)
btn_listar.pack()


panel_usuarios = tk.Text(root, height=10, width=50, state=tk.DISABLED)
panel_usuarios.pack()


root.mainloop()