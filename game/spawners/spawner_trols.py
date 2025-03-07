from .spawner import Spawner
from ..enemigos import Enemigo, Trol

class Spawner_Trols (Spawner):
    def spawn(self, nombre) -> Enemigo:
        return Trol(nombre, maza_duracion=10)