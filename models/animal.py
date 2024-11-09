from abc import abstractmethod
from models.ianimal import IAnimal

class Animal(IAnimal):
    
    def __init__(self, nombre:str, edad:int, peso:float) -> None:
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self.kilos_comidos = 0.0

    #Metodos
    def comer(self, kilos: float) -> None:
        self.kilos_comidos += kilos

    def obtener_kilos_comidos(self) -> float:
        return self.kilos_comidos

    @abstractmethod
    def hacer_sonido(self) -> str:
        pass

    #Getters y Setters
    @property
    def nombre(self) -> str:
        """ Devuelve el valor del atributo privado 'nombre' """
        return self._nombre
    
    @nombre.setter
    def nombre(self, value:str) -> None:
        """ 
        Establece un nuevo valor para el atributo privado 'nombre'
    
        Valida que el valor enviado corresponda al tipo de dato del atributo
        """ 
        if isinstance(value, str):
            self._nombre = value
        else:
            raise ValueError('Expected str')
        
    @property
    def edad(self) -> int:
        """ Devuelve el valor del atributo privado 'edad' """
        return self._edad
    
    @edad.setter
    def edad(self, value:int) -> None:
        """ 
        Establece un nuevo valor para el atributo privado 'edad'
    
        Valida que el valor enviado corresponda al tipo de dato del atributo
        """ 
        if isinstance(value, int):
            self._edad = value
        else:
            raise ValueError('Expected int')
        
    @property
    def peso(self) -> float:
        """ Devuelve el valor del atributo privado 'peso' """
        return self._peso
    
    @peso.setter
    def peso(self, value:float) -> None:
        """ 
        Establece un nuevo valor para el atributo privado 'peso'
    
        Valida que el valor enviado corresponda al tipo de dato del atributo
        """ 
        if isinstance(value, float):
            self._peso = value
        else:
            raise ValueError('Expected float')
        
    @property
    def kilos_comidos(self) -> float:
        """ Devuelve el valor del atributo privado 'kilos_comidos' """
        return self._kilos_comidos
    
    @kilos_comidos.setter
    def kilos_comidos(self, value:float) -> None:
        """ 
        Establece un nuevo valor para el atributo privado 'kilos_comidos'
    
        Valida que el valor enviado corresponda al tipo de dato del atributo
        """ 
        if isinstance(value, float):
            self._kilos_comidos = value
        else:
            raise ValueError('Expected float')