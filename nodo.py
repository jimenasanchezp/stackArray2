class Nodo:
    # constructor de la clase Nodo
    def __init__(self, id, nombre, telfono):
        # Validar que el ID sea un entero
        if not isinstance(id, int):
            raise TypeError("El ID debe ser un número entero.")
        self.id = id # asigna el id
        self.nombre = nombre # asigna el nombre
        self.telefono = telfono # asigna el telefono
        
        # método para representar el nodo como una cadena
    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Correo: {self.telefono}"