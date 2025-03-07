from abc import ABC, abstractmethod 

class Enemigo(ABC):
    # lista con los tipos de enemigos
    tipos = []

    def __init__(self, tipo, nombre, vida, armadura, arma, arma_daño):
        # Asegurarse de que el tipo sea válido antes de asignarlo
        if tipo not in self.tipos:
            raise ValueError(f"El tipo {tipo} no es válido")
        else:
            self.tipo = tipo    

        self.nombre = nombre
        self.vida = vida
        self.armadura = armadura  # Porcentaje de reducción de daño, ejemplo: 0 (indefenso) , 50, 80, 100 (inmune)
        self.arma = arma
        self.arma_daño = arma_daño        

    @classmethod
    def registrar_tipo(cls, tipo):
        if tipo not in cls.tipos:
            cls.tipos.append(tipo)

    @abstractmethod
    def ataca(self):
        pass

    def esta_vivo(self):
        return self.vida > 0

    def recibe_daño(self, daño):
        daño_menos_armadura = daño *(1-self.armadura/100)
        self.vida -= daño_menos_armadura
        print(f"{self.nombre} recibe {daño_menos_armadura:.2f} de daño")
        if self.esta_vivo():
            print(f"{self.nombre} tiene {self.vida:.2f} de vida")
        else:
            print(f"{self.nombre} ha muerto")
