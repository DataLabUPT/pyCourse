import unittest
from facultate import Facultate


class TestFacultate(unittest.TestCase):
    '''Test Facultate'''

    def setUp(self):
        self.f1 = Facultate('Tehnologii Informationale', 'ti', 3720)

    def tearDown(self):
        del self.f1

    def test_nume_facultate(self):
        self.f1.nume = 'Electronica si Telecomunicatii'
        self.assertEqual(self.f1.nume_facultate, 'Facultatea de Electronica si Telecomunicatii')

    def test_numar_studenti(self):
        self.assertEqual(self.f1.numar_studenti, 'Numar studenti 3720 la facultatea ti')
        self.f1.studenti = 4050
        self.assertEqual(self.f1.numar_studenti, 'Numar studenti 4050 la facultatea ti')

    def test_finantare(self):
        self.assertEqual(self.f1.finantare, 855600)


if __name__ == "__main__":
    unittest.main()
