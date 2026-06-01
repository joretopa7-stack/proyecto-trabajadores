from abc import ABC, abstractmethod

# ABSTRACCIÓN
class Trabajador(ABC):

    def __init__(self, nombre, salario):

        # ENCAPSULACIÓN
        self.__nombre = nombre
        self.__salario = salario

    # ENCAPSULACIÓN
    def getNombre(self):
        return self.__nombre

    def getSalario(self):
        return self.__salario

    def setNombre(self, nombre):
        self.__nombre = nombre

    def setSalario(self, salario):
        self.__salario = salario

    # ABSTRACCIÓN
    @abstractmethod
    def calcularBono(self):
        pass

    # ABSTRACCIÓN
    @abstractmethod
    def mostrarInformacion(self):
        pass