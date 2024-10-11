import unittest
from src.sample_adding.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def test_dodawanie_dwoch_liczb(self):
        c = Calculator(3, 4)
        assert c.dodawanie() == 7, "Dodawanie jest zle!"

    def test_dodawanie_dwoch_slow(self):
        self.assertRaises(Exception, Calculator, "text", "text")
