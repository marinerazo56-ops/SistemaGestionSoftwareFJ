from modelos.cliente import Cliente
from modelos.sala import ReservaSala
from modelos.equipo import AlquilerEquipo
from modelos.asesoria import AsesoriaEspecializada
from modelos.reserva import Reserva

from utils.logger import registrar_log

print("\n========= SOFTWARE FJ =========\n")

reservas = []

try:

    cliente1 = Cliente(
        "Sebastian",
        "sebastian@gmail.com",
        "315987654"
    )

    sala1 = ReservaSala(
        "Sala Premium",
        100000,
        20
    )

    reserva1 = Reserva(
        cliente1,
        sala1,
        3
    )

    reserva1.confirmar()

    reservas.append(reserva1)

    registrar_log("Reserva 1 creada correctamente")

except Exception as e:

    registrar_log(str(e))

    print(e)


try:

    cliente2 = Cliente(
        "Laura",
        "laura@gmail.com",
        "320555888"
    )

    equipo1 = AlquilerEquipo(
        "Portatil Gamer",
        80000,
        "Computador"
    )

    reserva2 = Reserva(
        cliente2,
        equipo1,
        2
    )

    reserva2.confirmar()

    reservas.append(reserva2)

    registrar_log("Reserva 2 creada correctamente")

except Exception as e:

    registrar_log(str(e))

    print(e)


try:

    cliente3 = Cliente(
        "Carlos",
        "carlos@gmail.com",
        "311777999"
    )

    asesoria1 = AsesoriaEspecializada(
        "Asesoria IA",
        150000,
        "Ingeniero Senior"
    )

    reserva3 = Reserva(
        cliente3,
        asesoria1,
        4
    )

    reserva3.confirmar()

    reservas.append(reserva3)

    registrar_log("Reserva 3 creada correctamente")

except Exception as e:

    registrar_log(str(e))

    print(e)


print("\n========= RESERVAS =========\n")

for reserva in reservas:

    print(reserva.mostrar_reserva())

print("\nSistema ejecutado correctamente.\n")