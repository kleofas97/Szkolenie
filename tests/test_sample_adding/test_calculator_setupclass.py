import unittest
from src.sample_adding.calculator import Calculator

class TestCalculatorSetUp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set up the calculator once for the entire class
        cls.calculator_valid = Calculator(3, 4)

    def test_dodawanie_dwoch_liczb(self):
        self.assertEqual(self.calculator_valid.dodawanie(), 7)

    def test_odejmowanie_dwoch_liczb(self):
        self.assertEqual(self.calculator_valid.odejmowanie(), -1)

    def test_dodwanie_dwoch_slow(self):
        self.assertRaises(Exception, Calculator, 'text', 'text')