# Enemy starts with health-100,random mana-[50,100] and random damage-[0,50]
import random


class Enemy:

    def __init__(self, health=100,
                 mana=random.randrange(50, 100, 10),
                 damage=random.randrange(10, 50, 10)):
        self.health = health
        self.max_health = health
        self.mana = mana
        self.damage = damage

    def __repr__(self):
        return "Enemy(health={}, mana={}, damage={})".format(self.health,
                                                             self.mana,
                                                             self.damage)

    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

    def get_damage(self):
        return self.damage

    def is_alive(self):
        return self.get_health() > 0

    def take_damage(self, damage_points):
        self.health -= damage_points
        if self.health < 0:
            self.health = 0

    def take_healing(self, healing_points):
        if self.is_alive() is False:
            return False
        heal = self.health + healing_points
        if heal > self.max_health:
            return False
        else:
            self.health = heal
            return True

    def attack(self):
        return self.damage

