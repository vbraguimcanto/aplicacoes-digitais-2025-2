from abc import ABC, abstractmethod


class FiguraGeometrica(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass


class Circulo(FiguraGeometrica):

    def __init__(self, raio):
        self.raio = raio
    
    def area(self):
        return 3.14 * (self.raio ** 2)

    def perimetro(self):
        return 2 * 3.14 * self.raio
    

circulo = Circulo(raio=10)
print(circulo.area())
print(circulo.perimetro())