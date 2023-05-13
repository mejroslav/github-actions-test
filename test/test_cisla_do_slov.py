import unittest
from utils import cisla_do_slov


class TestCisel(unittest.TestCase):
    def test_cisla_do_slov_1(self):
        self.assertEqual(cisla_do_slov(10), "jedna nula")

    def test_cisla_do_slov_2(self):
        self.assertEqual(cisla_do_slov(28), "dva osm")
