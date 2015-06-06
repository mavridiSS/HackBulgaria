import unittest
from fractions import Fraction


class TestFractions(unittest.TestCase):
    def setUp(self):
        self.first = Fraction(1, 2)
        self.second = Fraction(2, 4)

    def test_init(self):
        with self.assertRaises(ValueError):
            self.fraction = Fraction(1, 0)

    def test_str(self):
        test_str = "1 / 2"
        self.assertEqual(str(self.first), test_str)

    def test_str_with_null(self):
        self.fraction = Fraction(0, 1)
        self.assertEqual(str(self.fraction), "0")

    def test_eq(self):
        self.assertTrue(self.first == self.second)

    def test_add(self):
        self.assertEqual(self.first + self.second, Fraction(8, 8))

    def test_sub(self):
        self.assertEqual(self.first - self.second, Fraction(0, 1))

    def test_mull(self):
        self.assertEqual(self.first * self.second, Fraction(1, 4))


if __name__ == '__main__':
    unittest.main()
