
import unittest
from salario import calcular_salario

class TestSalario(unittest.TestCase):
    def test_salario_basico(self):
        self.assertAlmostEqual(calcular_salario(25.50, 160), 4080.0, places=2)

    def test_salario_zero(self):
        self.assertEqual(calcular_salario(0.0, 200), 0.0)
        self.assertEqual(calcular_salario(50.0, 0.0), 0.0)

    def test_valores_negativos(self):
        with self.assertRaises(ValueError):
            calcular_salario(-1.0, 100)
        with self.assertRaises(ValueError):
            calcular_salario(50.0, -5.0)

if __name__ == '__main__':
    unittest.main()
