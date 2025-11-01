from pila import Pila
from nodo import Nodo

def main():
    # Definir el tamaño de la pila
    tamaño = 2  
    # crea una instancia de Pila
    pila = Pila(tamaño)

    while True:
        print("\n--- Menú de Pila ---")
        print("1. Push (Agregar contacto)")
        print("2. Pop (Retirar contacto)")
        print("3. Peek (Ver contacto en la cima)")
        print("4. Contains (Buscar contacto por ID)")
        print("5. Clear (Vaciar pila)")
        print("6. Count (Contar contactos en la pila)")
        print("7. Salir")
        print("------------------------")
            
         # lee la opción del usuario
        try:
            opcion = int(input("Seleccione una opción (1-6): "))
        except ValueError:
            # si no es un número entero, muestra un mensaje de error
            print("Opción inválida. Por favor, ingrese un número.")
            continue

        # AGREGAR CONTACTO
        if opcion == 1:
            try:
                id = int(input("Ingrese el ID del contacto: "))
                nombre = input("Ingrese el nombre del contacto: ")
                correo = input("Ingrese el correo del contacto: ")
                # crea un nodo con los datos
                nodo = Nodo(id, nombre, correo)
                # agrega el nodo a la pila
                pila.push(nodo)
                print(f"Contacto '{nodo.nombre}' agregado a la pila.")
            except TypeError as e:
                print(f"Error de tipo: {e}")
            except OverflowError as e:
                print(f"Error: {e}")
            pila.show_list()

        # RETIRAR CONTACTO
        elif opcion == 2:
            nodo = pila.pop()
            if nodo is not None:
                print(f"Contacto retirado: {nodo}")
            else:
                print("La pila está vacía. No hay contactos para retirar.")
            pila.show_list()

        # VER CONTACTO EN LA CIMA
        elif opcion == 3:
            nodo = pila.peek()
            if nodo is not None:
                print(f"Contacto en la cima: {nodo}")
            else:
                print("La pila está vacía.")
            pila.show_list()

        # BUSCAR CONTACTO POR ID
        elif opcion == 4:
            if pila.is_empty():
                print("La pila está vacía. No hay contactos para buscar.")
            else:
                try:
                    id_buscado = int(input("Ingrese el ID del contacto a buscar: "))
                    if pila.contains(id_buscado):
                        print(f" El contacto con ID '{id_buscado}' SÍ está en la pila.")
                    else:
                        print(f" El contacto con ID '{id_buscado}' NO está en la pila.")
                except ValueError:
                    print("ID inválido. Debe ser un número entero.")
            pila.show_list()

        # VACIAR PILA
        elif opcion == 5:
            pila.clear()
            print("Pila vaciada exitosamente.")
            pila.show_list()

        elif opcion == 6:
            if pila.is_empty():
                print("La pila está vacía.")
            print(f"Total de elementos en la pila: '{pila.count()}'")
            pila.show_list()
            
        
        elif opcion == 7:
            print(f"Saliendo del programa." )
            break

        else:
            print("Opción no válida. Por favor, seleccione 1, 2, 3, 4, 5, 6 o 7.")

if __name__ == "__main__":
    main()