class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro
    
    def cambiarRegistro(n):
        self.registro = n
    
    def asignarTipo(aTipo):
        if (aTipo == "electrico" or aTipo == "gasolina"):
            self.tipo = aTipo

class Asiento:
    paleta = ("rojo", "verde", "amarillo", "negro", "blanco")
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(c):
        if c in paleta:
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

    def cantidadAsientos():
        return len(self.asientos)
    
    def verificarIntegridad():
        for i in range(len(self.asientos)):
            if self.registro != motor.registro or motor.registro != asiento.registro:
                return("Las piezas no son originales")
                break
            else:
                return("Auto original")

if __name__=="__main__":
    bmw = Auto("bmw", 33000, list(),"tesla", Motor(4, "electrico", 142), 341)
    print(bmw.marca)