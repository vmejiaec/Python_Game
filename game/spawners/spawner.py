from abc import ABC, abstractmethod
from game.enemigos.enemigo import Enemigo

class Spawner(ABC):

    @abstractmethod
    def spawn(self, nombre) -> Enemigo:
        pass