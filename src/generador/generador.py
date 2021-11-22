import random
import json
import time
import sys
import csv
from faker import Faker
import string
from typing import List
fake = Faker()

def generar_usuarios(numero_datos: int = 10, save_file: str = ""):
    usuarios = {}
    for i in range(numero_datos):
        datos = {}
        datos["id"] = i
        datos["nombre"] = fake.name()
        datos["rol"] = random.choice(["usuario", "funcionario"])
        datos["contrasena"] = fake.password()
        datos["correo"] = fake.email(), 
        datos["direccion"] = fake.address(), 
        datos["telefono"] = fake.phone_number(), 
        datos["zip"] = random.randint(10000000, 20000000), 
        datos["pedidos"] = ""
        usuarios[i] = datos
    with open(save_file, 'w') as f:
        json.dump(usuarios, f)

def generar_articulos(numero_datos: int = 10, save_file: str = ""):
    articulos = {}
    for i in range(numero_datos):
        datos = {}
        datos["id"] = i
        datos["nombre"] = "Producto Bumi " + str(i)
        datos["stock"] = random.randint(10, 50)
        datos["url_img"] = "https://bumi.com/id/" + ''.join(random.choice(string.ascii_letters + string.digits) for x in range(12)) + ".png"
        precio = random.randint(100000, 2000000)
        datos["precio_antes_impuesto"] = precio
        datos["impuesto_porcentaje"] = .19
        datos["descuento"] = random.random()
        articulos[i] = datos
    with open(save_file, 'w') as f:
        json.dump(articulos, f)

def generar_pedidos(usuarios, articulos, save_file: str = ""):

    pass

if __name__ == "__main__":
    #generar_usuarios(save_file = "../../data/usuarios.json")
    generar_articulos(save_file = "../../data/articulos.json")

