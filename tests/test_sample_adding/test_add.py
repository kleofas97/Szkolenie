from src.sample_adding.adding import add
import unittest


class TestAddFunction(unittest.TestCase):
    def test_add_integers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_strings(self):
        self.assertEqual(add("foo", "bar"), "foobar")

    def test_wrong_adding(self):
        self.assertRaises(TypeError, add, 2, "teskt")