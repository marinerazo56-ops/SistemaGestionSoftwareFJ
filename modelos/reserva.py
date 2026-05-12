class Reserva:

    def __init__(self, cliente, servicio, duracion):

        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    def confirmar(self):

        self.estado = "Confirmada"

    def cancelar(self):

        self.estado = "Cancelada"

    def mostrar_reserva(self):

        return f"""
Cliente: {self.cliente.mostrar_info()}
Servicio: {self.servicio.nombre}
Duracion: {self.duracion}
Estado: {self.estado}
"""