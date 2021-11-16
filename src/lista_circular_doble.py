class Nodo:
    def __init__(self,dato):
        self.previo = None
        self.siguiente = None
        self.dato = dato

#Esta lista enlazada circular doble posee orden decreciente respecto al id
class ListaEnlazadaCircularDoble():
    def __init__(self):
        self.cabeza = None
        self.lenght = 0
    
    def push_front(self,dato):
        """
        Añade el nuevo nodo antes de la cabeza/cursor y 
        cambia el cursor/cabeza al nuevo nodo.
        """
        nuevo_nodo = Nodo(dato)
        if self.lenght==0:
            self.cabeza = nuevo_nodo
            self.cabeza.previo = self.cabeza
            self.cabeza.siguiente = self.cabeza
            self.lenght = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            nuevo_nodo.previo = self.cabeza.previo
            self.cabeza.previo = nuevo_nodo
            self.cabeza = nuevo_nodo
        self.lenght += 1

    def search(self,id):
        """
        Retorna el dato en lista con el indicado.
        """
        if self.lenght == 0:
            raise Exception("Lo siento, esta lista está vacía")
        elif self.cabeza.dato.id == id:
            return self.cabeza.dato
        else:
            puntero_actual = self.cabeza
            for i in range(0,self.lenght()-1):
                puntero_actual = puntero_actual.siguiente
                if puntero_actual.dato.id == id:
                    return puntero_actual.dato
                    break
            if i==self.lenght()-2 and puntero_actual.dato.id != id:
                raise Exception("Lo siento, el dato no se encuentra en lista.".format(id=id))
    
    def add_after(self,nodo_1, dato):
        """
        Añade un nuevo nodo con el dato indicado después de nodo_1.
        """
        nodo_2 = Nodo(dato)
        nodo_2.siguiente = nodo_1.siguiente
        nodo_2.previo = nodo_1
        nodo_1.siguiente = nodo_2
        nodo_2.siguiente.previo = nodo_2
        self.lenght += 1

    def insert_with_order(self,dato):
        """
        Inserta un nuevo nodo con el dato indicado teniendo en 
        cuenta el orden decreciente dado por id.
        """
        if self.lenght == 0:
            self.push_front(dato)
        elif self.cabeza.dato.id == dato.id:
            raise Exception("Lo siento, el id ya se encuentra en lista.".format(id=id))
        elif self.lenght == 1 and self.cabeza.dato.id > dato.id:
            self.add_after(self.cabeza,dato)
        elif self.lenght == 1 and self.cabeza.dato.id < dato.id:
            self.push_front(dato)
        elif self.cabeza.previo.dato.id < dato.id:
            self.add_after(self.cabeza.previo,dato)
        elif self.cabeza.previo.dato.id == dato.id:
            raise Exception("Lo siento, el id ya se encuentra en lista.".format(id=id))
        else:
            puntero_actual = self.cabeza
            for i in range(0,self.lenght()-2):
                puntero_actual = puntero_actual.siguiente
                if puntero_actual.dato.id > dato.id:
                    self.add_after(puntero_actual.previo,dato)
                    break
                elif puntero_actual.dato.id == dato.id:
                    raise Exception("Lo siento, el id ya se encuentra en lista.".format(id=id))
    
    def erase(self,id):
        try:
            nodo_a_borrar = self.search(id)
            if self.lenght==1:
                self.cabeza = None
                self.lenght = 0
            else:
                nodo_a_borrar.siguiente.previo = nodo_a_borrar.previo
                nodo_a_borrar.previo.siguiente = nodo_a_borrar.siguiente
        except:
            raise Exception("Nodo no encontrado")
    
    def empty(self):
        if self.lenght==0:
            return True
        else:
            return False
    
    def get_lowest_id(self):
        if self.empty():
            return 0
        else:
            return self.cabeza.dato.id
    
    def get_higest_id(self):
        if self.empty():
            return 0
        else:
            return self.cabeza.previo.dato.id