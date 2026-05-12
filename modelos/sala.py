from modelos.servicio import Servicio

class ReservaSala(Servicio):

    def __init__(self, nombre, precio, capacidad):

        super().__init__(nombre, precio)

        self.capacidad = capacidad

    def calcular_costo(self):

        return self.precio * 1.19

    def descripcion(self):

        return f"Sala para {self.capacidad} personas"