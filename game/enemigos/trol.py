from game.enemigos.enemigo import Enemigo

Enemigo.registrar_tipo("Trol")

class Trol(Enemigo):
    def __init__(self, nombre, maza_duracion):
        super().__init__(
            tipo="Trol",
            nombre=nombre, 
            vida=20, 
            arma="maza", 
            arma_daño= 10,
            armadura=80)
        self.maza_duracion = maza_duracion # El número de golpes de la maza antes de romperse

    def ataca(self):
        if self.vida <= 0:
            print(f"{self.nombre} no puede atacar porque está muerto")
            return
        
        if self.maza_duracion <= 0:
            print(f"{self.nombre} no puede atacar porque su maza se rompió")
            return
        else:
            print(f"{self.nombre} ataca con la maza, y tiene {self.maza_duracion} golpes restantes")
            self.maza_duracion -= 1
            return self.arma_daño