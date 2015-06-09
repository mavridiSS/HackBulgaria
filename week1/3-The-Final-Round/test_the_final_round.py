import unittest
import the_final_round


class TestFinalRound(unittest.TestCase):

    def test_count_words(self):
        res = the_final_round.count_words(["apple", "banana", "apple"])
        self.assertEqual(res, {'apple': 2, 'banana': 1})

    def test_unique_words_count(self):
        res = the_final_round.unique_words_count(["apple", "banana", "apple"])
        self.assertEqual(res, 2)

    def test_nan_expand(self):
        res = the_final_round.nan_expand(3)
        self.assertEqual(res, "Not a Not a Not a NaN")

    def test_iterations_of_nan_expand(self):
        res = the_final_round.iterations_of_nan_expand("Not a NaN")
        self.assertEqual(res, 1)

    def test_iterations_of_false_nan_expand(self):
        res = the_final_round.iterations_of_nan_expand("This is not true")
        self.assertFalse(res)

    def test_prime_factorization(self):
        res = the_final_round.prime_factorization(1000)
        self.assertEqual(res, [(2, 3), (5, 3)])

    def test_group(self):
        res = the_final_round.group([1, 1, 1, 2, 3, 1, 1])
        self.assertEqual(res, [[1, 1, 1], [2], [3], [1, 1]])

    def test_max_consecutive(self):
        res = the_final_round.max_consecutive([1, 2, 3, 3, 3, 3, 4, 3, 3])
        self.assertEqual(res, 4)

    def test_group_by(self):
        res = the_final_round.groupby(lambda x: x % 3, [0, 1, 2, 3, 4, 5, 6])
        self.assertEqual(res, {0: [0, 3, 6], 1: [1, 4], 2: [2, 5]})

    def test_prepare_meal(self):
        res = the_final_round.prepare_meal(5)
        self.assertEqual(res, "eggs")

    def test_reduce_file_path(self):
        res = the_final_round.reduce_file_path("/srv/www/htdocs/wtf")
        self.assertEqual(res, "/srv/www/htdocs/wtf")

    def test_is_an_bn(self):
        res = the_final_round.is_an_bn("aaaaabbbb")
        self.assertFalse(res)

    def is_credit_card_valid(self):
        res = the_final_round.is_credit_card_valid(79927398713)
        self.assertTrue(res)

    def test_goldbach(self):
        res = the_final_round.goldbach(10)
        self.assertEqual(res, [(3, 7), (5, 5)])

    def test_magic_square(self):
        res = the_final_round.magic_square([[4, 9, 2], [3, 5, 7], [8, 1, 6]])
        self.assertTrue(res)

    def test_friday_years(self):
        res = the_final_round.friday_years(1990, 2015)
        self.assertEqual(res, 4)

if __name__ == '__main__':
    unittest.main()
