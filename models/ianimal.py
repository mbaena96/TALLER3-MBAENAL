from abc import ABC, abstractmethod

class IAnimal(ABC):

    @abstractmethod
    def hacer_sonido() -> str:
        pass

    @abstractmethod 
    def comer(self, kilos):
        pass

    @abstractmethod
    def obtener_kilos_comidos():
        pass