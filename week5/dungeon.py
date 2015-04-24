"""
lines = open("name of file").read().split("\n")
lines = [line for line in lines if line.strip()!=""]
map = [list(line) for line in lines]


S means a starting point for our hero.
G means gateway - the end of the dungeon (and most propably the enter to another)
# is an obstacle
. is a walkable path.
T is a treasure that can be either mana, health, weapon or spell
E is an enemy that our hero can fight
15-17karh 18 geomtr 20-24 dis 27 daa 29-4 chm 6-10-11lp 5-12
"""
from hero import Hero
from weapon import Weapon
from spell import Spell
from mana import Mana
import itertools
import random


class Dungeon:

    def __init__(self, filename):
        lines = open(filename).read().split("\n")
        lines = [line for line in lines if line.strip() != ""]

        self.map = [list(line) for line in lines]

        self.spawn_points = [[i, j] for i, line in enumerate(self.map)
                             for j, ch in enumerate(line) if ch == "S"]

        self.treasure_points = [[i, j] for i, line in enumerate(self.map)
                                for j, ch in enumerate(line) if ch == "T"]

        self.enemy_points = [[i, j] for i, line in enumerate(self.map)
                             for j, ch in enumerate(line) if ch == "E"]

        self.obstacle_points = [[i, j] for i, line in enumerate(self.map)
                                for j, ch in enumerate(line) if ch == "#"]

        self.treasures = [Weapon(name="The Axe of Destiny", damage=20),
                          Spell(
                              name="Fireball", damage=30, mana_cost=50, cast_range=2),
                          Mana(mana=50)]

        self.hero_pos = [None, None]

        self.hero_in_dungeon = None

    def print_map(self):
        for line in self.map:
            print(''.join(line))

    def place_on_map(self, point, entity):
        x, y = point
        self.map[x][y] = entity

    def spawn(self, hero):
        self.hero_in_dungeon = hero
        if len(self.spawn_points) == 0:
            raise Exception("Cannot spawm hero")

        self.hero_pos = self.spawn_points.pop(0)
        self.place_on_map(self.hero_pos, "H")

    def point_in_dungeon(self, point):
        x, y = point
        if x < 0 or x >= len(self.map):
            return False
        if y < 0 or y >= len(self.map[0]):
            return False
        return True

    def pick_treasure(self):
        treasure = random.choice(self.treasures)
        if isinstance(treasure, Weapon):
            self.hero_in_dungeon.equip(treasure)
        if isinstance(treasure, Spell):
            self.hero_in_dungeon.learn(treasure)
        if isinstance(treasure, Mana):
            self.hero_in_dungeon.take_mana(treasure)

    def swap_curr_point_with(self, point):
        x, y = point
        hero_x, hero_y = self.hero_pos
# NEED TO IMPLEMENT "START A FIGHT" LOGIC!
        if point in self.enemy_points:
            pass
        if point in self.obstacle_points:
            return False
        if point in self.treasure_points:
            print("Found treasure!")
            self.pick_treasure()
            self.place_on_map(self.hero_pos, ".")
            self.hero_pos = point
            self.place_on_map(self.hero_pos, "H")

        if self.point_in_dungeon(point):
            self.place_on_map(self.hero_pos, ".")
            self.hero_pos = point
            self.place_on_map(self.hero_pos, "H")
            self.hero_in_dungeon.take_mana()
        else:
            return False

    def has_enemy_in_cast_range(self, spell_range):
        hero_x, hero_y = self.hero_pos
        cast_range_squares = [[hero_x + spell_range, hero_y],
                              [hero_x - spell_range, hero_y],
                              [hero_x, hero_y + spell_range],
                              [hero_x, hero_y - spell_range]]
        for square in cast_range_squares:
            if square in self.enemy_points and self.point_in_dungeon(square):
                return True
        return "Nothing in casting range {}".format(self.hero_in_dungeon.cast_range)

    def move_hero(self, direction):
        hero_x, hero_y = self.hero_pos
        if direction is "up":
            return self.swap_curr_point_with([hero_x - 1, hero_y])
        if direction is "down":
            return self.swap_curr_point_with([hero_x + 1, hero_y])
        if direction is "right":
            return self.swap_curr_point_with([hero_x, hero_y + 1])
        if direction is "left":
            return self.swap_curr_point_with([hero_x, hero_y - 1])

    def hero_attack(self, by):
        hero_x, hero_y = self.hero_pos
        if by is "spell":
            self.hero.attack(by)
            if self.hero_in_dungeon.can_cast():
                return self.has_enemy_in_cast_range(self.hero_in_dungeon.cast_range)
            else:
                raise Exception("Cannot cast spell!")

h = Hero(name="Bron", title="Dragonslayer", health=100,
         mana=50, mana_regeneration_rate=2)
s = Spell(name="Fireball", damage=30, mana_cost=50, cast_range=1)
h.learn(s)
dungeon = Dungeon("level1.txt")
dungeon.print_map()
dungeon.spawn(h)
dungeon.move_hero("right")
dungeon.move_hero("down")
dungeon.move_hero("down")
dungeon.move_hero("down")
dungeon.print_map()
print(dungeon.hero_attack(by="spell"))

"""
1.да оправя max_health  и max_mana
2.да направя метода place_on_map
3.да кача проекта в github
4.moga da napravq igrata da se igrae s strelkite na klaviatura s while True i vutre raw_input i da pravi nqkakuv hod
"""
