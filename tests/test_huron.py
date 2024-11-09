import unittest
from models.huron import Huron

class TestHuron(unittest.TestCase):

    def setUp(self):
        self.huron = Huron("Pepe", 5, 2.0, "USA", 15.0)

    def test_hacer_sonido(self):
        self.assertEqual(self.huron.hacer_sonido(), '¡Eek Eek')

    def test_calcular_flete_should_be_30(self):
        self.assertEqual(self.huron.calcular_flete(), 30)
