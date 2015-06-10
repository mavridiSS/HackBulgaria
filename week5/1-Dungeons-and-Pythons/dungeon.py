from hero import Hero
from weapon import Weapon
from spell import Spell
from mana import Mana
from fight import Fight
from enemy import Enemy
import random


class Dungeon:
    HERO = "H"
    ENEMY = "E"
    SPAWN = "S"
    TREASURE = "T"
    WALKABLE = "."
    OBSTACLE = "#"

    def __init__(self, filename):
        self.map = self.generate_map_from(filename)

        self.spawn_points = [[i, j] for i, line in enumerate(self.map)
                             for j, ch in enumerate(line)
                             if ch == Dungeon.SPAWN]

        self.treasure_points = [[i, j] for i, line in enumerate(self.map)
                                for j, ch in enumerate(line)
                                if ch == Dungeon.TREASURE]

        self.enemy_points = [[i, j] for i, line in enumerate(self.map)
                             for j, ch in enumerate(line)
                             if ch == Dungeon.ENEMY]

        self.obstacle_points = [[i, j] for i, line in enumerate(self.map)
                                for j, ch in enumerate(line)
                                if ch == Dungeon.OBSTACLE]

        self.treasures = [Weapon(name="The Axe of Destiny", damage=20),
                          Spell(name="Fireball",
                                damage=30,
                                mana_cost=50,
                                cast_range=2),
                          Mana(mana=50)]

        self.hero_pos = None
        self.enemy_to_fight_pos = None

        self.hero_in_dungeon = None

    def generate_map_from(self, filename):
        with open(filename, 'r') as f:
            lines = f.read().split("\n")
            lines = [line for line in lines if line.strip() != ""]
        return [list(line) for line in lines]

    def print_map(self):
        for line in self.map:
            print(''.join(line))

    def place_on_map(self, point, entity):
        x, y = point
        self.map[x][y] = entity

    def spawn(self, hero):
        self.hero_in_dungeon = hero
        if self.hero_in_dungeon.health == 0:
            self.hero_in_dungeon.health = self.hero_in_dungeon.max_health
        if len(self.spawn_points) == 0:
            raise Exception("Game is over,no more spawn points!")
        self.hero_pos = self.spawn_points.pop(0)
        self.place_on_map(self.hero_pos, Dungeon.HERO)

    def point_in_dungeon(self, point):
        x, y = point
        if x < 0 or x >= len(self.map):
            return False
        if y < 0 or y >= len(self.map[0]):
            return False
        if self.map[x][y] == Dungeon.OBSTACLE:
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

    def create_a_fight(self):
        fight = Fight()
        fight.start(self.hero_in_dungeon, Enemy(),
                    self.hero_pos, self.enemy_to_fight_pos)
        if fight.is_hero_dead:
            self.place_on_map(self.hero_pos, Dungeon.ENEMY)
            self.place_on_map(self.enemy_to_fight_pos, Dungeon.WALKABLE)
            self.spawn(self.hero_in_dungeon)
        else:
            self.enemy_points.remove(self.enemy_to_fight_pos)
            self.place_on_map(self.enemy_to_fight_pos, Dungeon.HERO)
            self.place_on_map(self.hero_pos, Dungeon.WALKABLE)

    def trigger_action(self, point):
        x, y = point
        hero_x, hero_y = self.hero_pos
        if point in self.enemy_points:
            self.place_on_map(self.hero_pos, Dungeon.WALKABLE)
            self.hero_pos = point
            self.enemy_to_fight_pos = point
            self.create_a_fight()
        if point in self.obstacle_points:
            return False
        if point in self.treasure_points:
            print("Found treasure!")
            self.pick_treasure()
            self.treasure_points.remove(point)
            self.place_on_map(self.hero_pos, Dungeon.WALKABLE)
            self.hero_pos = point
            self.place_on_map(self.hero_pos, Dungeon.HERO)

        if self.point_in_dungeon(point):
            self.place_on_map(self.hero_pos, Dungeon.WALKABLE)
            self.hero_pos = point
            self.place_on_map(self.hero_pos, Dungeon.HERO)
            self.hero_in_dungeon.take_mana()
        else:
            return False

    def move_hero(self, direction):
        hero_x, hero_y = self.hero_pos
        if direction is "up":
            return self.trigger_action([hero_x - 1, hero_y])
        if direction is "down":
            return self.trigger_action([hero_x + 1, hero_y])
        if direction is "right":
            return self.trigger_action([hero_x, hero_y + 1])
        if direction is "left":
            return self.trigger_action([hero_x, hero_y - 1])

    def has_enemy_in_range(self, square):
        hero_x, hero_y = self.hero_pos
        range_squares = [[hero_x + square, hero_y],
                         [hero_x - square, hero_y],
                         [hero_x, hero_y + square],
                         [hero_x, hero_y - square]]
        for square in range_squares:
            if square in self.enemy_points and self.point_in_dungeon(square):
                self.enemy_to_fight_pos = square
                return True
        return False

    def hero_attack(self, by):
        hero_x, hero_y = self.hero_pos
        if by is "spell":
            if self.hero_in_dungeon.can_cast():
                if self.has_enemy_in_range(self.hero_in_dungeon.spell.cast_range):
                    self.create_a_fight()
                else:
                    return "Nothing in casting range {}".format(self.hero_in_dungeon.spell.cast_range)
            else:
                return "Cannot cast spell"
        if by is "weapon":
            if self.has_enemy_in_range(2):
                self.create_a_fight()
            else:
                return "Nothing in weapon range 2"
