class Pila:
    def __init__(self, capacidad):
        self.items = []
        self.capacidad = capacidad
        self.tope = 0

    def insertar(self, elemento):
        if self.tope < self.capacidad:
            self.items.append(elemento)
            self.tope += 1
            print(f"Insertar {elemento} - Pila: {self.items}, Tope: {self.tope}")
        else:
            print("Error: Desbordamiento")

    def eliminar(self):
        if self.tope > 0:
            elemento = self.items.pop()
            self.tope -= 1
            print(f"Eliminar {elemento} - Pila: {self.items}, Tope: {self.tope}")
        else:
            print("Error: Subdesbordamiento")

pila = Pila(8)
pila.insertar("X")
pila.insertar("Y")
pila.eliminar()
pila.eliminar()
pila.eliminar()
pila.insertar("V")
pila.insertar("W")
pila.eliminar()
pila.insertar("R")
print(f"\nLa pila final tiene {pila.tope} elementos.")
