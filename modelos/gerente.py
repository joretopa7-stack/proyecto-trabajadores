from modelos.trabajador import Trabajador

# HERENCIA
class Gerente(Trabajador):

    def __init__(self, nombre, salario, equipoACargo):
        super().__init__(nombre, salario)
        self.equipoACargo = equipoACargo

    # POLIMORFISMO
    def calcularBono(self):
        return self.getSalario() * 0.20

    # POLIMORFISMO
    def mostrarInformacion(self):
        return (
            f"Gerente: {self.getNombre()}"
            f"Equipo a cargo: {self.equipoACargo}"
            f"Salario: ${self.getSalario()}"
            f"Bono: ${self.calcularBono()}"
        )