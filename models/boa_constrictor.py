from models.animal_exotico import AnimalExotico

class Boa_Constrictor(AnimalExotico):

    def __init__(self, nombre: str, edad: int, peso: float, pais_origen: str, impuestos: float) -> None:
        super().__init__(nombre, edad, peso, pais_origen, impuestos)
        self.ratones_comidos = 0

    def hacer_sonido(self) -> str:
        return "¡Tsss!"
    
    def calcular_flete(self) -> float:
        return super().calcular_flete()
    
    def alimientar_boa(self) -> int:
        if self.ratones_comidos != 20:
            self.ratones_comidos += 1
            return "Se ha comido un ratón"
        else:
            raise ValueError('Demasiados Ratones!')
    
    @property
    def ratones_comidos(self) -> int:
        """ Devuelve el valor del atributo privado 'ratones_comidos' """
        return self.__ratones_comidos
    
    @ratones_comidos.setter
    def ratones_comidos(self, value:int) -> None:
        """ 
        Establece un nuevo valor para el atributo privado 'ratones_comidos'
    
        Valida que el valor enviado corresponda al tipo de dato del atributo
        """ 
        if isinstance(value, int):
            self.__ratones_comidos = value
        else:
            raise ValueError('Expected int')
        
    