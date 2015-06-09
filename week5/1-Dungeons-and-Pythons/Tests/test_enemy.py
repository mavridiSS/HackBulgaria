import unittest
from enemy import Enemy


class TestEnemy(unittest.TestCase):
    def setUp(self):
        self.enemy = Enemy()

    def test_get_damage(self):
        self.assertLessEqual(self.enemy.get_damage(), 100)

    def test_get_mana(self):
        self.assertLessEqual(self.enemy.get_mana(), 100)

    def test_take_damage(self):
        self.enemy.take_damage(50)
        self.assertEqual(self.enemy.get_health(), 50)

    def test_take_healing(self):
        self.enemy.take_damage(50)
        self.assertTrue(self.enemy.take_healing(50))
        self.assertFalse(self.enemy.take_healing(70))


if __name__ == '__main__':
    unittest.main()
