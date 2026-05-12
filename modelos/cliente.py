from modelos.entidad import Entidad

class Cliente(Entidad):

    def __init__(self, nombre, correo, telefono):

        self.__nombre = nombre
        self.__correo = correo
        self.__telefono = telefono

    def mostrar_info(self):

        return f"""
Nombre: {self.__nombre}
Correo: {self.__correo}
Telefono: {self.__telefono}
"""