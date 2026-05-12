from modelos.servicio import Servicio

class AlquilerEquipo(Servicio):

    def __init__(self, nombre, precio, tipo):

        super().__init__(nombre, precio)

        self.tipo = tipo

    def calcular_costo(self):

        return self.precio + 50000

    def descripcion(self):

        return f"Equipo tipo {self.tipo}"