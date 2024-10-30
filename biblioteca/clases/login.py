from usuario import Usuario as usuario

class Login(usuario):
    def __init__(nombre_usuario, contrasena):
        super().__init__(nombre_usuario, contrasena)