class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro
    
    def cambiarRegistro(self, n):
        self.registro = n
    
    def asignarTipo(self, aTipo):
        if (aTipo == "electrico" or aTipo == "gasolina"):
            self.tipo = aTipo

class Asiento:
    paleta = ("rojo", "verde", "amarillo", "negro", "blanco")
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self,c):
        if c in self.paleta:
            self.color = c

class Auto:
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
        self.cantidadCreados = 0

    def cantidadAsientos(self):
        contador = 0
        for i in range(len(self.asientos)):
            if self.asientos[i] != None:
                contador += 1
        return contador
    
    def verificarIntegridad(self):
        for i in range(len(self.asientos)):
            if self.registro != self.motor.registro or self.motor.registro != self.asientos[i].registro:
                return("Las piezas no son originales")
                break
            else:
                return("Auto original")

if __name__=="__main__":
    print(Asiento.paleta)