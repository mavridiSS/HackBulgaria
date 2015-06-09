import unittest
from hero import Hero
from mana import Mana
from weapon import Weapon
from spell import Spell


class TestHero(unittest.TestCase):
    def setUp(self):
        self.hero = Hero(name="Bron",
                         title="Dragonslayer",
                         health=100, mana=100,
                         mana_regeneration_rate=2)

    def test_init(self):
        self.assertTrue(isinstance(self.hero, Hero))
        self.assertTrue(self.hero.weapon is None)
        self.assertTrue(self.hero.spell is None)

    def test_repr(self):
        test_str = "Hero(health={}, mana={})".format(self.hero.get_health(),
                                                     self.hero.get_mana())
        self.assertEqual(test_str, str(self.hero))

    def test_known_as(self):
        test_str = "Bron the Dragonslayer"
        self.assertEqual(self.hero.known_as(), test_str)

    def test_get_health(self):
        self.assertEqual(self.hero.get_health(), 100)

    def test_get_mana(self):
        self.assertEqual(self.hero.get_mana(), 100)

    def test_can_cast(self):
        self.assertFalse(self.hero.can_cast())

    def test_take_damage(self):
        self.hero.take_damage(150)
        self.assertEqual(self.hero.get_health(), 0)

    def test_take_healing(self):
        self.hero.take_damage(50)
        self.assertTrue(self.hero.take_healing(50))
        self.assertFalse(self.hero.take_healing(70))

    def test_take_mana(self):
        self.hero.take_mana(Mana(mana=50))
        self.assertTrue(self.hero.get_mana(), 100)

    def test_equip(self):
        w = Weapon(name="The Axe of Destiny", damage=20)
        self.hero.equip(w)
        self.assertTrue(self.hero.weapon is not None)

    def test_already_equipped_hero(self):
        w = Weapon(name="The Axe of Destiny", damage=20)
        self.hero.equip(w)
        with self.assertRaises(AttributeError):
            self.hero.equip(w)

    def test_attack_with_no_weapons(self):
        with self.assertRaises(Exception):
            self.hero.attack(by='weapon')

    def test_attack_with_weapon(self):
        w = Weapon(name="The Axe of Destiny", damage=20)
        self.hero.equip(w)
        self.assertEqual(self.hero.attack(by='weapon'), 20)

    def test_attack_with_no_spell(self):
        with self.assertRaises(Exception):
            self.assertEqual(self.hero.attack(by='spell'), 30)

    def test_attack_with_spell_with_insufficient_mana(self):
        s = Spell(name="Fireball", damage=30, mana_cost=150, cast_range=2)
        self.hero.learn(s)
        with self.assertRaises(Exception):
            self.assertEqual(self.hero.attack(by='spell'), 30)

    def test_attack_with_spell(self):
        s = Spell(name="Fireball", damage=30, mana_cost=50, cast_range=2)
        self.hero.learn(s)
        self.assertEqual(self.hero.attack(by='spell'), 30)

    def test_pick_weapon(self):
        test_str = "Hero has no weapons and no spells"
        self.assertEqual(self.hero.pick_weapon(), test_str)

if __name__ == '__main__':
    unittest.main()
