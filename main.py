from modelos.desarrollador import Desarrollador
from modelos.gerente import Gerente

trabajadores = []

try:

    print("--- REGISTRO DE DESARROLLADOR ---")

    nombreDesarrollador = input(
        "Ingrese el nombre del desarrollador: "
    )

    salarioDesarrollador = float(
        input("Ingrese el salario del desarrollador: ")
    )

    lenguaje = input(
        "Ingrese el lenguaje de programación: "
    )

    print("--- REGISTRO DE GERENTE ---")

    nombreGerente = input(
        "Ingrese el nombre del gerente: "
    )

    salarioGerente = float(
        input("Ingrese el salario del gerente: ")
    )

    equipoACargo = input(
        "Ingrese el equipo a cargo: "
    )

    trabajador1 = Desarrollador(
        nombreDesarrollador,
        salarioDesarrollador,
        lenguaje
    )

    trabajador2 = Gerente(
        nombreGerente,
        salarioGerente,
        equipoACargo
    )

    trabajadores.append(trabajador1)
    trabajadores.append(trabajador2)

    print("--- INFORMACIÓN DE LOS TRABAJADORES ---")

    # POLIMORFISMO
    for trabajador in trabajadores:
        print(trabajador.mostrarInformacion())
        print("-" * 40)

except ValueError:
    print("\nError: Debe ingresar un valor numerico para el salario.")