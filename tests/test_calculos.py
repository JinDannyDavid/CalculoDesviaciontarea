import unittest
from scr.logica.calculos import Calculadora, NoSePuedeCalcular


class TestCalculadora(unittest.TestCase):

    def test_media_sin_elementos(self):
        calculadora = Calculadora([])
        with self.assertRaises(NoSePuedeCalcular):
            calculadora.media()

    def test_media_un_elemento(self):
        calculadora = Calculadora([5])
        self.assertEqual(calculadora.media(), 5)

    def test_media_dos_elementos(self):
        calculadora = Calculadora([5, 15])
        self.assertEqual(calculadora.media(), 10)

    def test_media_n_elementos_positivos(self):
        calculadora = Calculadora([1, 2, 3, 4, 5])
        self.assertEqual(calculadora.media(), 3)

    def test_media_n_elementos_ceros(self):
        calculadora = Calculadora([0, 0, 0, 0])
        self.assertEqual(calculadora.media(), 0)

    def test_media_n_elementos_mixtos(self):
        calculadora = Calculadora([-1, 1, -2, 2])
        self.assertEqual(calculadora.media(), 0)

    def test_media_elementos_no_numericos(self):
        calculadora = Calculadora([1, 2, 'a', 4])
        with self.assertRaises(TypeError):
            calculadora.media()

    def test_desviacion_estandar_sin_elementos(self):
        calculadora = Calculadora([])
        with self.assertRaises(NoSePuedeCalcular):
            calculadora.desviacion_estandar()

    def test_desviacion_estandar_un_elemento(self):
        calculadora = Calculadora([5])
        self.assertEqual(calculadora.desviacion_estandar(), 0)

    def test_desviacion_estandar_dos_elementos(self):
        calculadora = Calculadora([5, 15])
        self.assertAlmostEqual(calculadora.desviacion_estandar(), 5)

    def test_desviacion_estandar_n_elementos_positivos(self):
        calculadora = Calculadora([1, 2, 3, 4, 5])
        self.assertAlmostEqual(calculadora.desviacion_estandar(), 1.4142135623730951)

    def test_desviacion_estandar_n_elementos_ceros(self):
        calculadora = Calculadora([0, 0, 0, 0])
        self.assertEqual(calculadora.desviacion_estandar(), 0)

    def test_desviacion_estandar_n_elementos_mixtos(self):
        calculadora = Calculadora([-1, 1, -2, 2])
        self.assertAlmostEqual(calculadora.desviacion_estandar(), 1.5811388300841898)

    def test_desviacion_estandar_elementos_no_numericos(self):
        calculadora = Calculadora([1, 2, 'a', 4])
        with self.assertRaises(TypeError):
            calculadora.desviacion_estandar()


if __name__ == '__main__':
    unittest.main()
