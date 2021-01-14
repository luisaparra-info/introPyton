class Coche:
    ruedas=4
    def __init__(self, color, aceleracion):
        self.__color=color
        self.__aceleracion=aceleracion
        self.__velocidad=0
    def getColor(self):
        return str(self.__color)

    def setColor(self, color):
        self.__color=color

    def getAceleracion(self):
        return self.__aceleracion

    def getVelocidad(self):
        return self.__velocidad

    def acelera(self):
        self.__velocidad += self.getAceleracion()
    def frena(self):
        self.__velocidad -= self.getAceleracion()
        if self.getVelocidad() < 0:
            self.__velocidad = 0

    def imprimir(self):
        return "Tengo un "+ str(type(self)).split(".")[1].split("'")[0] + " " + self.getColor() + " con aceleracion a " + str(self.getAceleracion()) + " y velocidad " + str(
            str(self.getVelocidad()))

class CocheVolador(Coche):
    ruedas = 6
    def __init__(self, color, aceleracion=10, volando=False):
        super().__init__(color,aceleracion)
        self.__volando=volando

    def getVolando(self):
        return self.__volando

    def setVolando(self, volando):
        self.__volando = volando

    def imprimir(self):
        if self.getVolando():
            return (super().imprimir() + "  y volando")
        else:
            return (super().imprimir() + " y en el suelo")


c1 = Coche('Rojo',20)
c2 = Coche('Azul',30)
cv1= CocheVolador('Amarillo',15,True)
cv2= CocheVolador('Verde',45)
cv3= CocheVolador('Rosa')

c1._Coche__aceleracion = 50

Coches = [c1, c2, cv1, cv2, cv3]
print("Numero de ruedas: "+ str(Coche.ruedas))

for c in Coches:
    print(c.imprimir())

c1.acelera()
c2.frena()
"""
for c in Coches:
    c.imprimir()
"""