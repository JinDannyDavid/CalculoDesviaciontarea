import math


class NoSePuedeCalcular(Exception):
    pass


class Calculadora:
    def __init__(self, elementos):
        self.elementos = elementos

    def media(self):
        if not self.elementos:
            raise NoSePuedeCalcular("No se puede calcular la media de una lista vacía")

        if any(not isinstance(x, (int, float)) for x in self.elementos):
            raise TypeError("Todos los elementos deben ser numéricos")

        return sum(self.elementos) / len(self.elementos)

    def desviacion_estandar(self):
        if not self.elementos:
            raise NoSePuedeCalcular("No se puede calcular la desviación estándar de una lista vacía")

        if any(not isinstance(x, (int, float)) for x in self.elementos):
            raise TypeError("Todos los elementos deben ser numéricos")

        media = self.media()
        varianza = sum((x - media) ** 2 for x in self.elementos) / len(self.elementos)
        return math.sqrt(varianza)