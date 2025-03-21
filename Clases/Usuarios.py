class Usuarios:
    def __init__(self):
        self.usuarios = []

    def guardarUsuario(self, nombre, nickname, clave):
        self.usuarios.append({"nombre": nombre, "nickname": nickname, "clave": clave})

    def listarUsuarios(self):
        return self.usuarios