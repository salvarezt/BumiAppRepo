class Nodo:
    def __init__(self,dato):
        self.previo = None
        self.siguiente = None
        self.dato = dato

class ListaEnlazada:
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
    
    def push_back(self,dato):
        """
        Añade el nuevo nodo después de la cabeza/cursor y 
        cambia el cursor/cabeza al nuevo nodo.
        """
        nuevo_nodo = Nodo(dato)
        if self.lenght==0:
            self.cabeza = nuevo_nodo
            self.cabeza.previo = self.cabeza
            self.cabeza.siguiente = self.cabeza
            self.lenght = nuevo_nodo
        else:
            nuevo_nodo.previo = self.cabeza
            self.cabeza.siguiente.previo = nuevo_nodo
            self.cabeza.siguiente = nuevo_nodo
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
                raise Exception("Lo siento, el dato con {id} no se encuentra en lista.".format(id=id))
    
    def add_after(nodo_1, dato):
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
        elif self.cabeza.dato.id > dato.id:
            self.push_front(dato)
        elif self.cabeza.dato.id == dato.id:
            raise Exception("Lo siento, el dato con {id} ya se encuentra en lista.".format(id=id))
        else:
            puntero_actual = self.cabeza
            for i in range(0,self.lenght()-2):
                puntero_actual = puntero_actual.siguiente
                if puntero_actual.dato.id > dato.id:
                    self.add_after(puntero_actual.previo,dato)
                    break
                elif puntero_actual.dato.id == dato.id:
                    raise Exception("Lo siento, el dato con {id} ya se encuentra en lista.".format(id=id))
            
            if i==self.lenght()-3 and puntero_actual.siguiente.dato.id < dato.id:
                self.add_after(puntero_actual.siguiente,dato)
            elif i==self.lenght()-3 and puntero_actual.siguiente.dato.id == dato.id:
                raise Exception("Lo siento, el dato con {id} ya se encuentra en lista.".format(id=id))
        self.lenght += 1
    
    def erase(id):
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