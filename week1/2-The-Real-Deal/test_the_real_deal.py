import unittest
import the_real_deal


class TestTheRealDeal(unittest.TestCase):
    def test_sum_of_dividors(self):
        self.assertEqual(the_real_deal.sum_of_divisors(1000), 2340)

    def test_is_not_prime(self):
        self.assertFalse(the_real_deal.is_prime(8))

    def test_is_prime(self):
        self.assertTrue(the_real_deal.is_prime(2))

    def test_prime_number_of_dividors(self):
        self.assertTrue(the_real_deal.prime_number_of_divisors(7))

    def test_contains_digit(self):
        self.assertTrue(the_real_deal.contains_digit(42, 2))

    def test_contains_digits(self):
        self.assertTrue(the_real_deal.contains_digits(456, []))

    def test_is_number_balance(self):
        self.assertTrue(the_real_deal.is_number_balanced(9))

    def test_count_substrings(self):
        self.assertEqual(the_real_deal.count_substrings("babababa", "baba"), 2)

    def test_zero_insert(self):
        self.assertEqual(the_real_deal.zero_insert(116457), 10160457)

    def test_sum_matrix(self):
        self.assertEqual(the_real_deal.sum_matrix([[1, 2, 3],
                                                   [4, 5, 6], [7, 8, 9]]), 45)

    def test_matrix_bombing_plan(self):
        result = {(0, 0): 42,
                  (0, 1): 36,
                  (0, 2): 37,
                  (1, 0): 30,
                  (1, 1): 15,
                  (1, 2): 23,
                  (2, 0): 29,
                  (2, 1): 15,
                  (2, 2): 26}
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(the_real_deal.matrix_bombing_plan(matrix), result)

if __name__ == '__main__':
    unittest.main()
