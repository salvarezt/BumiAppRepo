class Usuario:
    def __init__(self,id,nombres,apellidos,rol,contrasena,
    correo,ciudad,direccion,telefono,zip,pedidos):
        self.id = id
        self.nombres = nombres
        self.apellidos = apellidos
        self.rol = rol
        self.contrasena = contrasena
        self.correo = correo
        self.ciudad = ciudad
        self.direccion = direccion
        self.telefono = telefono
        self.zip = zip
        self.pedidos = pedidos
    
class Cliente(Usuario):
    def __init__(self, id, nombres, apellidos, contrasena, 
    correo, ciudad, direccion, telefono, zip):
        pedidos = ""
        super().__init__(id, nombres, apellidos,"usuario", contrasena,
        correo, ciudad, direccion, telefono, zip, pedidos)

class Funcionario(Usuario):
    def __init__(self, id, nombres, apellidos, contrasena, 
    correo, ciudad, direccion, telefono, zip):
        pedidos = ""
        super().__init__(id, nombres, apellidos,"funcionario", contrasena,
        correo, ciudad, direccion, telefono, zip, pedidos)