from lista_circular_doble import ListaEnlazadaCircularDoble
from usuario import Cliente,Funcionario

coleccion_de_usuarios = None
estructura_de_datos = 1
file_data_clients = "../examples/usuarios.json"

#Funciones de la API que proveen funcionalidades CRUD sobre el manejo de usuarios

def seleccionar_estructura():
    if estructura_de_datos == 1:
        coleccion_de_usuarios = ListaEnlazadaCircularDoble()

#Función que carga la base de datos de clientes del archivo JSON a la lista
def descargar_usuarios():
    #Del file_data_clients, cargue todos los usuarios a un objeto de tipo Usuario
    pass

def crear_nuevo_cliente(id,nombres,apellidos,contrasena,
    correo,ciudad,direccion,telefono,zip):
    """
    Función que crea un nuevo cliente

    Parámetros
    ----------
    id: int
        Documento de identidad del usuario
    nombres: string
        Nombres del usuario
    apellidos: string
        Apellidos del usuario
    contrasena: string
        Contraseña del usuario
    correo: string
        Correo del usuario
    ciudad: string
        Ciudad del usuario
    direccion: string
        Dirección de residencia del usuario
    telefono: int
        Teléfono del usuario
    zip: int
        Códido postal del usuario
    Retorna
    ----------
    ver_datos_usuario()
    """    
    #Llame el constructor de la clase Cliente
    #nuevo_cliente = Cliente(...)
    #coleccion_de_usuarios.insert_with_order(nuevo_cliente)
    #Haga catch de la excepción Lo siento, el id ya se encuentra en lista
    #para que si el id ya existe retorne que FAIL,el cliente ya existe
    #ver_datos_usuario()
    pass

def crear_nuevo_funcionario(id,nombres,apellidos,contrasena,
    correo,ciudad,direccion,telefono,zip):
    """
    Función que crea un nuevo funcionario

    Parámetros
    ----------
    id: int
        Documento de identidad del usuario
    nombres: string
        Nombres del usuario
    apellidos: string
        Apellidos del usuario
    contrasena: string
        Contraseña del usuario
    correo: string
        Correo del usuario
    ciudad: string
        Ciudad del usuario
    direccion: string
        Dirección de residencia del usuario
    telefono: int
        Teléfono del usuario
    zip: int
        Códido postal del usuario
    Retorna
    ----------
    ver_datos_usuario()
    """    
    #Llame el constructor de la clase funcionario
    #nuevo_funcionario = Funcionario(...)
    #coleccion_de_funcionarios.insert_with_order(nuevo_funcionario)
    #Haga catch de la excepción Lo siento, el id ya se encuentra en lista
    #para que si el id ya existe retorne que FAIL,el funcionario ya existe
    #ver_datos_usuario()
    pass

def actualizar_datos_usuario(id):
    #Menú que actualiza los datos de un usuario
    #nodo_usuario = coleccion_de_usuarios.search(id)
    #nodo_usuario.telefono = 80309900
    #Luego retone 200 OK y el JSON de ver_datos_usuario()
    pass

def ver_datos_usuario(id):
    #Idea: coleccion_de_usuarios.search(id) para obtener el nodo que contiene al cliente y retorne la sección del JSON respectiva
    #Retorne 200 OK y un JSON como el de examples/usuario con los datos del usuario
    pass

def eliminar_usuario(id):
    #dato_nodo_eliminado = coleccion_de_usuarios.erase(id)
    pass

