#from flask import jsonify

class Usuario:

    def __init__(self,id,nombres,apellidos,rol,contrasena,
    correo,ciudad,direccion,telefono,zip,pedidos):
        self.id = int(id)
        self.nombres = nombres
        self.apellidos = apellidos
        self.rol = rol
        self.contrasena = contrasena
        self.correo = correo
        self.ciudad = ciudad
        self.direccion = direccion
        self.telefono = int(telefono)
        self.zip = int(zip)
        self.pedidos = pedidos
    
    def crear_usuario_dicc(self, dicc):
        return Usuario(
            dicc['id'],
            dicc['nombres'],
            dicc['apellidos'],
            dicc['rol'],
            dicc['contrasena'],
            dicc['correo'],
            dicc['ciudad'],
            dicc['direccion'],
            dicc['telefono'],
            dicc['zip'],
            dicc['pedidos']
        )

    def obtener_dicc_usuario(self):
        usuario = {}
        usuario["nombres"] = self.nombres
        usuario["apellidos"] = self.apellidos
        usuario["rol"] = self.rol
        usuario["contrasena"] = self.contrasena
        usuario["correo"] = self.correo
        usuario["ciudad"] = self.ciudad
        usuario["direccion"] = self.direccion
        usuario["telefono"] = self.telefono
        usuario["zip"] = self.zip
        usuario["pedidos"] = self.pedidos
        return usuario
    
    def mostrar(self):
        for atributo in self.__dict__:
            print(f"{atributo}: {self.__dict__[atributo]}")
    
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

'''
nuevo_usuario = Usuario(1000182041,"Pepito","Perez","cliente","amoamimami","ola@ola.com","Bogotá",
                        "CL 57",3145897656,110141,"1,2")
print(nuevo_usuario.obtener_json_usuario()
'''