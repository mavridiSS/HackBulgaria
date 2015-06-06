from hero import Hero
from enemy import Enemy
from spell import Spell
from weapon import Weapon


class Fight:
    HERO_ATTACK = "Hero hits Enemy with {} for {} dmg. Enemy health is {}."
    ENEMY_ATTACK = "Enemy hits Hero for {} dmg. Hero health is {}."
    HERO_CAST_ATTACK = "Hero casts a {}, hits Enemy for {} dmg.Enemy health is {}."
    HERO_WEP_ATTACK = "Hero hits Enemy with {} for {} dmg. Enemy health is {}."
    HERO_NO_MANA = "Hero does not have mana for {}"
    ENEMY_DEAD = "Enemy is dead"
    HERO_DEAD = "Hero is dead"

    def __init__(self):
        self.hero_pos = None
        self.enemy_pos = None
        self.is_hero_dead = None

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
                print(Fight.HERO_ATTACK.format(hero.weapon.name,
                                               hero.weapon.damage,
                                               enemy.health))
            elif hero.can_cast():
                enemy.take_damage(hero.attack(by="spell"))
                print(Fight.HERO_CAST_ATTACK.format(hero.spell.name,
                                                    hero.spell.damage,
                                                    enemy.health))
            else:
                print(Fight.HERO_NO_MANA.format(hero.spell.name))
                enemy.take_damage(hero.attack(by="weapon"))
                print(Fight.HERO_WEP_ATTACK.format(hero.weapon.name,
                                                   hero.weapon.damage,
                                                   enemy.health))
            if not enemy.is_alive():
                print(Fight.ENEMY_DEAD)
                self.is_hero_dead = False
                break
            if self.hero_pos == self.enemy_pos:
                hero.take_damage(enemy.attack())
                print(Fight.ENEMY_ATTACK.format(enemy.damage, hero.health))
            else:
                self.fight_range(self.hero_pos, self.enemy_pos)
            if not hero.is_alive():
                print(Fight.HERO_DEAD)
                self.is_hero_dead = True
                break
        return self.is_hero_dead
