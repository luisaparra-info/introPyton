class Coche:
    __ruedas=4
    def __init__(self, color, aceleracion):
        self.__color=color
        self.__aceleracion=aceleracion
        self.__velocidad=0
    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color=color

    def getAceleracion(self):
        return self.__aceleracion

    def getVelocidad(self):
        return self.__velocidad

    def getRuedas(self):
        return self.__ruedas


    def acelera(self):
        self.velocidad += self.aceleracion
    def frena(self):
        self.velocidad -= self.aceleracion
        if self.velocidad < 0:
            self.velocidad = 0
    def imprimir(self):
        return "Tengo un "+ str(type(c)).split(".")[1].split("'")[0] + " " + c.color + " con aceleracion a " + str(c.aceleracion) + " y velocidad " + str(
            c.velocidad)

class CocheVolador(Coche):
    ruedas = 6
    def __init__(self, color, aceleracion=10, volando=False):
        super().__init__(color,aceleracion)
        self.volando=volando
    def imprimir(self):
        if self.volando:
            return (super().imprimir() + "  y volando")
        else:
            return (super().imprimir() + " y en el suelo")


c1 = Coche('Rojo',20)
c2 = Coche('Azul',30)
cv1= CocheVolador('Amarillo',15,True)
cv2= CocheVolador('Verde',45)
cv3= CocheVolador('Rosa')

c1.aceleracion = 50

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