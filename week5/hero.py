from weapon import Weapon
from spell import Spell
from mana import Mana


class Hero:
    def __init__(self, name, title, health, mana, mana_regeneration_rate):
        self.name = name
        self.title = title
        self.health = health
        self.max_health = health
        self.mana = mana
        self.max_mana = mana
        self.mana_regeneration_rate = mana_regeneration_rate
        self.weapon = None
        self.spell = None

    def __repr__(self):
        return "Hero(health={}, mana={})".format(self.health, self.mana)

    def known_as(self):
        return "{} the {}".format(self.name, self.title)

    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

    def is_alive(self):
        return self.get_health() > 0

    def can_cast(self):
        if self.spell.damage == 0 or self.spell.mana_cost > self.mana:
            return False
        else:
            return True

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

    def take_mana(self, potion=None):
        if isinstance(potion, Mana):
            self.mana += potion.mana
        self.mana += self.mana_regeneration_rate

        if self.mana > self.max_mana:
            self.mana = self.max_mana

    def equip(self, weapon):
        if self.weapon is None:
            self.weapon = weapon
        else:
            raise AttributeError("Hero is already equipped with weapon.")

    def learn(self, spell):
        self.spell = spell

    def attack(self, by):
        if self.weapon.damage == 0 and self.spell.damage == 0:
            return 0
        if by is "weapon":
            return self.weapon.damage
        if by is "spell":
            if self.can_cast():
                self.mana -= self.spell.mana_cost
                return self.spell.damage
            else:
                raise Exception("Cannot cast spell!")

    def pick_weapon(self):
        if self.spell is None and self.weapon is None:
            return "Hero has no weapons and no spells"
        if self.spell is None:
            return "weapon"
        if self.weapon is None:
            return "spell"
        if not self.spell and not self.weapon:
            pass
"""
h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
w = Weapon(name="The Axe of Destiny", damage=20)
s = Spell(name="Fireball", damage=30, mana_cost=150, cast_range=2)
h.equip(w)
h.learn(s)

print(h.attack(by="spell"))
# да направя за член данни оръжие и магия и да ги изициалиризирам като инстанции на оръжие и магия
"""