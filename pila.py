from nodo import Nodo

class Pila:
    # constructor de la pila 
    def __init__(self, tamaño):
        if tamaño <= 0: # valida el tamaño sea positivo
            raise ValueError("El tamaño de la pila debe ser un número positivo.")
        self.tamaño = tamaño
        # lista para almacenar los nodos
        self.array = []

    # método para agregar un nodo a la pila
    def push(self, nodo):
        # valida si la pila está llena
        if len(self.array) >= self.tamaño:           
            # error si la pila está llena 
            raise OverflowError("La pila está llena.")
        # agrega el nodo a la pila
        self.array.append(nodo)

    # método para retirar un nodo de la pila
    def pop(self):
        # valida si la pila está vacía
        if self.is_empty():
            return None
        # retira y devuelve el nodo del top de la pila
        return self.array.pop()

    # método para ver el nodo en el top de la pila sin retirarlo
    def peek(self):
        if self.is_empty():
            return None
        # devuelve el nodo en  el top de la pila
        return self.array[-1]

    # método para verificar si la pila está vacía
    def is_empty(self):
        return len(self.array) == 0

    # método para verificar si la pila está llena
    def is_full(self):
        return len(self.array) >= self.tamaño

    # método para vaciar la pila
    def clear(self):
        # vacía la lista de nodos
        self.array = []

    # método para buscar un nodo por su ID
    def contains(self, id_a_buscar):
        # recorre los nodos en la pila
        for nodo in self.array:
            # compara el ID del nodo con el ID buscado
            if nodo.id == id_a_buscar:
                return True
        return False

    # método para mostrar el contenido de la pila
    def show_list(self):
        """
        Muestra el contenido actual de la pila.
        """
        if self.is_empty():
            print("Pila vacía.")
        else:
            print("Contenido actual de la pila (de abajo hacia arriba):")
            for i, nodo in enumerate(self.array):
                print(f"     [{i}] {nodo}")