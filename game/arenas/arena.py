from abc import ABC, abstractmethod

class Arena(ABC):
    
    @abstractmethod
    def __init__(self, nombre, enemigos):
        pass

