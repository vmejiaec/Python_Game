from .spawner import Spawner
from ..enemigos import Enemigo, Esqueleto

class Spawner_Esqueletos(Spawner):
    def spawn(self, nombre) -> Enemigo:
        return Esqueleto( nombre, cantidad_fechas=20) 