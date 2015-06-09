import unittest
from dungeon import Dungeon
from hero import Hero

"""
S.##.....T
#.##.S###.
#.###E###E
#E....###.
###T#####G
"""


class TestDungeon(unittest.TestCase):
    def setUp(self):
        self.dungeon = Dungeon('test_map.txt')
        self.hero = Hero(name="Bron",
                         title="Dragonslayer",
                         health=100, mana=100,
                         mana_regeneration_rate=2)

    def test_init(self):
        self.assertIsNone(self.dungeon.hero_pos)
        self.assertIsNone(self.dungeon.hero_in_dungeon)
        self.assertIsNone(self.dungeon.enemy_to_fight_pos)
        self.assertEqual(len(self.dungeon.spawn_points), 2)
        self.assertEqual(len(self.dungeon.enemy_points), 3)
        self.assertEqual(len(self.dungeon.treasure_points), 2)

    def test_place_on_map(self):
        self.dungeon.place_on_map((0, 0), self.dungeon.HERO)
        self.assertEqual(self.dungeon.map[0][0], self.dungeon.HERO)

    def test_spawn(self):
        self.dungeon.spawn(self.hero)
        self.assertEqual(self.dungeon.hero_pos, [0, 0])

    def test_point_in_dungeon(self):
        self.assertFalse(self.dungeon.point_in_dungeon([0, 2]))
        self.assertFalse(self.dungeon.point_in_dungeon([0, 250]))
        self.assertFalse(self.dungeon.point_in_dungeon([150, 250]))
        self.assertTrue(self.dungeon.point_in_dungeon([0, 4]))

    def test_create_a_fight(self):
        pass

    def test_trigger_action_on_obstacle(self):
        self.dungeon.spawn(self.hero)
        self.assertFalse(self.dungeon.trigger_action([0, 2]))

    def test_trigger_action_on_treasure(self):
        self.dungeon.spawn(self.hero)
        self.dungeon.trigger_action([0, 9])
        self.assertEqual(self.dungeon.hero_pos, [0, 9])
        self.assertEqual(self.dungeon.map[0][9], self.dungeon.HERO)

    def test_trigger_action_on_walkable_point(self):
        self.dungeon.spawn(self.hero)
        hero_x, hero_y = self.dungeon.hero_pos
        self.dungeon.trigger_action([0, 1])
        self.assertEqual(self.dungeon.map[hero_x][hero_y],
                         self.dungeon.WALKABLE)
        self.assertEqual(self.dungeon.map[0][1], self.dungeon.HERO)

    def test_trigger_action_on_point_outside_dungeon(self):
        self.dungeon.spawn(self.hero)
        self.assertFalse(self.dungeon.trigger_action([0, 250]))

    def test_move_hero(self):
        self.dungeon.spawn(self.hero)
        self.assertFalse(self.dungeon.move_hero(direction="down"))

    def test_has_enemy_in_range(self):
        self.dungeon.spawn(self.hero)
        self.assertFalse(self.dungeon.has_enemy_in_range(5))

    def test_hero_attack_with_no_spell(self):
        self.dungeon.spawn(self.hero)
        test_str = "Cannot cast spell"
        self.assertEqual(self.dungeon.hero_attack(by='spell'), test_str)

    def test_hero_attack_with_no_weapon(self):
        self.dungeon.spawn(self.hero)
        test_str = "Nothing in weapon range 1"
        self.assertEqual(self.dungeon.hero_attack(by='weapon'), test_str)


if __name__ == '__main__':
    unittest.main()
