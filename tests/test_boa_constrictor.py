import unittest
from models.boa_constrictor import Boa_Constrictor

class TestBoaConstrictor(unittest.TestCase):

    def setUp(self):
        self.boa = Boa_Constrictor ("Python", 2, 5.0, "Colombia", 10.0)

    def test_hacer_sonido(self):
        self.assertEqual(self.boa.hacer_sonido(), "¡Tsss!")

    def test_calcular_flete_should_be_30(self):
        self.assertEqual(self.boa.calcular_flete(), 50.0)

    def test_comer_un_raton(self):
        self.assertEqual(self.boa.alimientar_boa(), 'Se ha comido un ratón')

    def test_comer_mas_de_10_ratones(self):
        self.boa.ratones_comidos = 20
        self.assertRaises(ValueError, self.boa.alimientar_boa)