import unittest
import warmup


class WarmUpTest(unittest.TestCase):

    def test_factorial(self):
        fact = warmup.factorial(3)
        self.assertEqual(fact, 6)

    def test_fibonacci(self):
        fibonacci_list = warmup.fibonacci(3)
        self.assertEqual(fibonacci_list, [1, 1, 2])

    def test_sum_of_digits(self):
        sum = warmup.sum_of_digits(120)
        self.assertEqual(sum, 3)

    def test_fact_digits(self):
        digits = warmup.fact_digits(23)
        self.assertEqual(digits, 8)

    def test_palindrome(self):
        palindrome = warmup.palindrome("kapak")
        self.assertTrue(palindrome)

    def test_to_digits(self):
        digits = warmup.to_digits(123)
        self.assertEqual(digits, [1, 2, 3])

    def test_to_number(self):
        to_numb = warmup.to_number([9, 9, 9])
        self.assertEqual(to_numb, 999)

    def test_fib_number(self):
        fib = warmup.fib_number(3)
        self.assertEqual(fib, 112)

    def test_count_vowels(self):
        vowels_count = warmup.count_vowels("Python")
        self.assertEqual(vowels_count, 2)

    def test_count_consonants(self):
        cons_count = warmup.count_consonants("Python")
        self.assertEqual(cons_count, 4)

    def test_char_histogram(self):
        histogram = warmup.char_histogram("Python!")
        hist_dict = {'P': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1, '!': 1}
        self.assertEqual(histogram, hist_dict)

    def test_p_score(self):
        score = warmup.p_score(48)
        self.assertEqual(score, 3)

    def test_is_increasing(self):
        seq = warmup.is_increasing([1, 2, 3])
        self.assertTrue(seq)

    def test_is_decreasing(self):
        seq = warmup.is_decreasing([1, 2, 3])
        self.assertFalse(seq)

    def test_next_hack(self):
        hack = warmup.next_hack(10)
        self.assertEqual(hack, 21)


if __name__ == '__main__':
    unittest.main()
