from modelos.trabajador import Trabajador

# HERENCIA
class Desarrollador(Trabajador):

    def __init__(self, nombre, salario, lenguaje):
        super().__init__(nombre, salario)
        self.lenguaje = lenguaje

    # POLIMORFISMO
    def calcularBono(self):
        return self.getSalario() * 0.10

    # POLIMORFISMO
    def mostrarInformacion(self):
        return (
            f"Desarrollador: {self.getNombre()}"
            f"Lenguaje: {self.lenguaje}"
            f"Salario: ${self.getSalario()}"
            f"Bono: ${self.calcularBono()}"
        )