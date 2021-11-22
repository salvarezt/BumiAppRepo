class Usuario:
    def __init__(self,id,nombre,rol,contrasena,
    correo,ciudad,direccion,telefono,zip,pedidos):
        self.id = id
        self.nombre = nombre
        self.rol = rol
        self.contrasena = contrasena
        self.correo = correo
        self.ciudad = ciudad
        self.direccion = direccion
        self.telefono = telefono
        self.zip = zip
        self.pedidos = pedidos
    
class Cliente(Usuario):
    def __init__(self, id, nombre, contrasena, 
    correo, ciudad, direccion, telefono, zip):
        pedidos = ""
        super().__init__(id, nombre, "usuario", contrasena,
        correo, ciudad, direccion, telefono, zip, pedidos)

class Funcionario(Usuario):
    def __init__(self, id, nombre,  contrasena, 
    correo, ciudad, direccion, telefono, zip):
        pedidos = ""
        super().__init__(id, nombre, "funcionario", contrasena,
        correo, ciudad, direccion, telefono, zip, pedidos)