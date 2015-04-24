from hero import Hero
from enemy import Enemy
from spell import Spell
from weapon import Weapon


class Fight:
    def __init__(self):
        self.hero_pos = None
        self.enemy_pos = None

    def fight_range(self, hero_pos, enemy_pos):
        hero_x, hero_y = hero_pos
        enemy_x, enemy_y = enemy_pos
        if hero_x == enemy_x:
            if hero_y > enemy_y:
                print("Enemy moves right.This is his move.")
                enemy_y = hero_y - enemy_y
            else:
                print("Enemy moves left.This is his move.")
                enemy_y = enemy_y - hero_y
        elif hero_y == enemy_y:
            if hero_x > enemy_x:
                print("Enemy moves down.This is his move.")
                enemy_x = hero_x - enemy_x
            else:
                print("Enemy moves up.This is his move.")
                enemy_x = enemy_x - hero_x
        self.hero_pos = [hero_x, hero_y]
        self.enemy_pos = [enemy_x, enemy_y]

    def start(self, hero, enemy, hero_pos, enemy_pos):
        self.hero_pos = hero_pos
        self.enemy_pos = enemy_pos
        print("A fight is started between our {} and {}".format(hero, enemy))
        while True:
            if hero.weapon.damage > hero.spell.damage:
                enemy.take_damage(hero.attack(by="weapon"))
                print("Hero hits Enemy with {} for {} dmg. Enemy health is {}.".format(hero.weapon.name, hero.weapon.damage, enemy.health))
            elif hero.can_cast():
                enemy.take_damage(hero.attack(by="spell"))
                print("Hero casts a {}, hits Enemy for {} dmg.Enemy health is {}.".format(hero.spell.name, hero.spell.damage, enemy.health))
            else:
                print("Hero does not have mana for {}".format(hero.spell.name))
                enemy.take_damage(hero.attack(by="weapon"))
                print("Hero hits Enemy with {} for {} dmg. Enemy health is {}.".format(hero.weapon.name, hero.weapon.damage, enemy.health))
            if not enemy.is_alive():
                print("Enemy is dead")
                break
            if self.hero_pos == self.enemy_pos:
                hero.take_damage(enemy.attack())
                print("Enemy hits Hero for {} dmg. Hero health is {}.".format(enemy.damage, hero.health))
            else:
                self.fight_range(self.hero_pos,self.enemy_pos)
            if not hero.is_alive():
                print("Hero is dead")
                break


