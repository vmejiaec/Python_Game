from .enemigo import Enemigo

Enemigo.registrar_tipo("Esqueleto")

class Esqueleto(Enemigo):
    def __init__(self, nombre,  cantidad_fechas):
        super().__init__(
            tipo="Esqueleto",
            nombre=nombre, 
            vida = 10,
            arma= "arco", 
            arma_daño=15, 
            armadura=60)
        self.cantidad_fechas = cantidad_fechas

    def ataca(self):
        if self.vida <= 0:
            print(f"{self.nombre} no puede atacar porque está muerto")
            return
        
        if self.cantidad_fechas > 0:
            print(f"{self.nombre} ataca con {self.arma} y tiene {self.cantidad_fechas} flechas")
            self.cantidad_fechas -= 1
            return self.arma_daño
        else:
            print(f"{self.nombre} se ha quedado sin flechas. No puede atacar")

