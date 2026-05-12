from modelos.servicio import Servicio

class AsesoriaEspecializada(Servicio):

    def __init__(self, nombre, precio, experto):

        super().__init__(nombre, precio)

        self.experto = experto

    def calcular_costo(self):

        return self.precio * 1.10

    def descripcion(self):

        return f"Asesoria con experto {self.experto}"