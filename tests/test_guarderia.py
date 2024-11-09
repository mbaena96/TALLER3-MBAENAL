import unittest
from models.guarderia import Guarderia
from models.boa_constrictor import Boa_Constrictor
from models.huron import Huron

class TestGuarderia(unittest.TestCase):

    def setUp(self):
        self.boa1 = Boa_Constrictor ("Python", 2, 5.0, "Colombia", 10.0)
        self.boa2 = Boa_Constrictor ("Juancho", 5, 7.0, "Colombia", 11.0)
        huron1 = Huron("Pepe", 5, 2.0, "USA", 15.0)
        huron2 = Huron("Paco", 3, 1.5, "USA", 12.0)
        self.guarderia = Guarderia([self.boa1, self.boa2], [huron1, huron2])

    def test_alimentar_boas_should_return_exito(self):
        self.assertEqual(self.guarderia.alimentar_boa('Juancho'), 'Éxito')

    def test_alimentar_boas_should_return_no_existe_boa(self):
        self.assertEqual(self.guarderia.alimentar_boa('boa'), 'Esta Boa no existe!')

    def test_alimentar_boas_should_return_no_existe_boa_none(self):
        self.assertEqual(self.guarderia.alimentar_boa(None), 'Esta Boa no existe!')

    def test_alimentar_boas_should_return_boa_exito_9_ratones(self):
        self.boa1.ratones_comidos = 9
        self.assertEqual(self.guarderia.alimentar_boa('Juancho'), 'Éxito')

    def test_alimentar_boas_should_return_boa_llena(self):
        self.boa1.ratones_comidos = 20
        self.assertEqual(self.guarderia.alimentar_boa('Juancho'), 'La boa está llena')

if __name__ == "__main__":
    unittest.main()