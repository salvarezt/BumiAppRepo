class Nodo:
    def __init__(self, data):
        self.dato = data
        self.siguiente = None

    def __repr__(self):
        return str(self.dato)

class NodoBidireccional(Nodo):
    def __init__(self, data):
        super().__init__()
        self.previo = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        
    def insertar(self, data):
        temp = Nodo(data)
        if self.cabeza == None:
            self.cabeza = temp
            return 1
        actual = self.cabeza
        while actual.siguiente != None:
            actual = actual.siguiente
        actual.siguiente = temp

    def imprimir(self):
        actual = self.cabeza
        while actual != None:
            print(actual, end = " => ")
            actual = actual.siguiente
        print(None)

class ListaEnlazadaConCola(ListaEnlazada):
    def __init__(self):
        super().__init__()
        self.cola = None

    def insertar(self, dato):
        temp = Nodo(dato)
        self.cola.siguiente = temp
        self.cola = self.cola.siguiente

class ListaEnlazadaDoble(ListaEnlazada):
    def __init__(self):
        super().__init__()

    def insertar(self, data):
        temp = NodoBidireccional(data)
        if self.cabeza == None:
            self.cabeza = temp
            return 1
        previo = None
        actual = self.cabeza
        while actual.siguiente != None:
            previo = actual
            actual = actual.siguiente
        actual.siguiente = temp
        actual.previo = previo

class ListaEnlazadaDobleConCola(ListaEnlazadaConCola):
    def __init__(self):
        super().__init__()

    def insertar(self, dato):
        temp = NodoBidireccional(dato)
        previo = self.cola # New previous.
        self.cola.siguiente = temp # Update next.
        self.cola = self.cola.siguiente
        self.previo = previo
  
def mezclar_listas_enlazadas(cabeza1: Nodo, cabeza2: Nodo):
    nueva_cabeza = Nodo(data = "dummy")
    actual = nueva_cabeza
    while True: 
        if cabeza1 == None: 
            actual.siguiente = cabeza2
            break
        if cabeza2 == None:
            actual.siguiente = cabeza1
            break

        if cabeza1.dato <= cabeza2.dato: 
            actual.siguiente = cabeza1
            cabeza1 = cabeza1.siguiente
            
        else:
            actual.siguiente = cabeza2
            cabeza2 = cabeza2.siguiente
        actual = actual.siguiente

    return nueva_cabeza.siguiente

def eliminar_duplicados(cabeza: Nodo):
    actual = cabeza
    while actual: 
        while actual.siguiente and actual.dato == actual.siguiente.dato:
            actual.siguiente = actual.siguiente.siguiente
        actual = actual.siguiente
    return cabeza

if __name__ == '__main__':
    llist1 = ListaEnlazada()
    llist1.insertar(4)
    llist1.insertar(5)
    llist1.insertar(6)
    llist1.imprimir()

    llist2 = ListaEnlazada()
    llist2.insertar(1)
    llist2.insertar(2)
    llist2.insertar(4)
    llist2.imprimir()
    
    llist3 = ListaEnlazada()
    llist3.cabeza = mezclar_listas_enlazadas(llist1.cabeza, llist2.cabeza)
    llist3.imprimir()

    llist4 = ListaEnlazada()
    llist4.cabeza = eliminar_duplicados(llist3.cabeza)
    llist4.imprimir()
    #print(llist2.cola.data)