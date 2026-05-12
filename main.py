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


try:

    cliente4 = Cliente(
        "Andrea",
        "andrea@gmail.com",
        "321654987"
    )

    sala2 = ReservaSala(
        "Sala Ejecutiva",
        120000,
        15
    )

    reserva4 = Reserva(
        cliente4,
        sala2,
        2
    )

    reserva4.confirmar()

    reservas.append(reserva4)

except Exception as e:

    registrar_log(str(e))


try:

    cliente5 = Cliente(
        "Felipe",
        "felipe@gmail.com",
        "311222333"
    )

    equipo2 = AlquilerEquipo(
        "VideoBeam",
        50000,
        "Proyeccion"
    )

    reserva5 = Reserva(
        cliente5,
        equipo2,
        1
    )

    reserva5.confirmar()

    reservas.append(reserva5)

except Exception as e:

    registrar_log(str(e))


try:

    cliente6 = Cliente(
        "Valentina",
        "valentina@gmail.com",
        "300888777"
    )

    asesoria2 = AsesoriaEspecializada(
        "Consultoria Cloud",
        200000,
        "Arquitecto Cloud"
    )

    reserva6 = Reserva(
        cliente6,
        asesoria2,
        5
    )

    reserva6.confirmar()

    reservas.append(reserva6)

except Exception as e:

    registrar_log(str(e))


try:

    cliente7 = Cliente(
        "Miguel",
        "miguel@gmail.com",
        "322111000"
    )

    sala3 = ReservaSala(
        "Sala Junior",
        70000,
        8
    )

    reserva7 = Reserva(
        cliente7,
        sala3,
        1
    )

    reserva7.confirmar()

    reservas.append(reserva7)

except Exception as e:

    registrar_log(str(e))


try:

    cliente8 = Cliente(
        "Camila",
        "camila@gmail.com",
        "310555999"
    )

    equipo3 = AlquilerEquipo(
        "Camara Profesional",
        95000,
        "Audiovisual"
    )

    reserva8 = Reserva(
        cliente8,
        equipo3,
        3
    )

    reserva8.confirmar()

    reservas.append(reserva8)

except Exception as e:

    registrar_log(str(e))


try:

    cliente9 = Cliente(
        "Santiago",
        "santiago@gmail.com",
        "320444888"
    )

    asesoria3 = AsesoriaEspecializada(
        "Asesoria Ciberseguridad",
        180000,
        "Especialista Seguridad"
    )

    reserva9 = Reserva(
        cliente9,
        asesoria3,
        2
    )

    reserva9.confirmar()

    reservas.append(reserva9)

except Exception as e:

    registrar_log(str(e))


try:

    cliente10 = Cliente(
        "Natalia",
        "natalia@gmail.com",
        "301777222"
    )

    sala4 = ReservaSala(
        "Sala VIP",
        250000,
        30
    )

    reserva10 = Reserva(
        cliente10,
        sala4,
        4
    )

    reserva10.confirmar()

    reservas.append(reserva10)

except Exception as e:

    registrar_log(str(e))


print("\n========= RESERVAS =========\n")

for reserva in reservas:

    print(reserva.mostrar_reserva())

print("\nSistema ejecutado correctamente.\n")