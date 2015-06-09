import cat
import unittest


class TestCatScript(unittest.TestCase):
    def test_main(self):
        with self.assertRaises(AttributeError):
            cat.main()

if __name__ == '__main__':
    unittest.main()
