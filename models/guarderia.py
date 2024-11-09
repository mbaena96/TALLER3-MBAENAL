#from boa_constrictor import Boa_Constrictor

class Guarderia:
    def __init__(self, boas:list, hurones:list) -> None:
        self.boas = boas
        self.hurones = hurones

    def alimentar_boa(self, boa_alimentar):
        try:
            existe = False
            for boa in self.boas:
                if boa_alimentar == boa.nombre:
                    existe = True
                    break
            
            if existe:
                for boa in self.boas:
                    boa.alimientar_boa()
            else:
                return 'Esta Boa no existe!'
            
        except ValueError as e:
            return 'La boa está llena' 
        else:
            return 'Éxito'


    @property
    def boas(self) -> list:
        """ Devuelve el valor del atributo privado 'boas' """
        return self._boas
    
    @boas.setter
    def boas(self, value:list) -> None:
        """ 
        Establece un nuevo valor para el atributo privado 'boas'
    
        Valida que el valor enviado corresponda al tipo de dato del atributo
        """ 
        if isinstance(value, list):
            self._boas = value
        else:
            raise ValueError('Expected list')
        
    @property
    def hurones(self) -> list:
        """ Devuelve el valor del atributo privado 'hurones' """
        return self._hurones
    
    @hurones.setter
    def hurones(self, value:list) -> None:
        """ 
        Establece un nuevo valor para el atributo privado 'hurones'
    
        Valida que el valor enviado corresponda al tipo de dato del atributo
        """ 
        if isinstance(value, list):
            self._hurones = value
        else:
            raise ValueError('Expected list')