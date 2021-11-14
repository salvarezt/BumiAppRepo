# LinkedList Doble con cola
# Por Samuel Alvarez

class Nodo:
  def __init__(self, dato = None):
    self.dato = dato
    self.next = None # Nodo siguiente
    self.prev = None # Nodo anterior

class DobleLinkedList:
  def __init__(self, head = None):
    if head is None:
      head = Nodo()
      tail = head
    else:
      nod = head
      while nod.next is not None:
        nod = nod.next
      tail = nod
    self.head = head
    self.tail = tail
    
  def append(self, dato):
    # Añade un nuevo dato al final de la lista
    if self.head.dato is None:
      self.head.dato = dato
    else:
      self.tail.next = Nodo(dato)
      self.tail.next.prev = self.tail
      self.tail = self.tail.next
  
  def insert(self, dato, k = 0):
    # Inserta un dato en la k-esima posicion de la lista. Numerando desde 0
    if k == 0:
      self.head.prev = Nodo(dato)
      self.head.prev.next = self.head
      self.head = self.head.prev
    else:
      nodo = self.head
      k -= 1
      while k != 0:
        nodo = nodo.next
        k -= 1
      nuevo = Nodo(dato)
      nuevo.next = nodo.next
      nuevo.next.prev = nuevo
      nodo.next = nuevo
      nuevo.prev = nodo
  
  
