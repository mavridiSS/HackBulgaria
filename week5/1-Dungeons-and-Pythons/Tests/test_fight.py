import unittest
from dungeon import Dungeon
from fight import Fight
from enemy import Enemy
from hero import Hero
from spell import Spell
from weapon import Weapon


class TestFight(unittest.TestCase):
    def setUp(self):
        self.fight = Fight()
        self.dungeon = Dungeon("test_map.txt")
        self.hero = Hero(name="Bron",
                         title="Dragonslayer",
                         health=100,
                         mana=100,
                         mana_regeneration_rate=2)
        self.dungeon.spawn(self.hero)
        self.w = Weapon(name="The Axe of Destiny", damage=50)
        self.s = Spell(name="Fireball", damage=30, mana_cost=50, cast_range=2)
        self.hero.learn(self.s)
        self.hero.equip(self.w)
        self.dungeon.move_hero("right")

    def test_init(self):
        self.assertIsNone(self.fight.enemy_pos)
        self.assertIsNone(self.fight.hero_pos)
        self.assertFalse(self.fight.is_hero_dead)

# maybe the worst testcase but..
    def test_start(self):
        enemy_pos = [3, 1]
        res = self.fight.start(self.hero,
                               Enemy(),
                               self.dungeon.hero_pos,
                               enemy_pos)
        self.assertFalse(res)

if __name__ == '__main__':
    unittest.main()
