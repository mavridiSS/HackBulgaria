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
        self.mana_cost = 0
        self.cast_range = 0
        self.damage_by_weapon = 0
        self.damage_by_spell = 0

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
        if self.damage_by_spell == 0 or self.mana_cost > self.mana:
            raise Exception("Cannot cast spell")
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
        if self.damage_by_weapon > 0:
            raise AttributeError("Hero is already equipped with weapon.")
        else:
            self.damage_by_weapon = weapon.get_damage()

    def learn(self, spell):
        self.damage_by_spell = spell.get_damage()
        self.mana_cost = spell.get_mana_cost()
        self.cast_range = spell.get_cast_range()

    def attack(self, by):
        if self.damage_by_weapon == 0 and self.damage_by_spell == 0:
            return 0
        if by is "weapon":
            return self.damage_by_weapon
        if by is "spell":
            if self.can_cast():
                self.mana -= self.mana_cost
                return self.damage_by_spell
            else:
                raise Exception("Cannot cast spell!")

h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
print(h)
# да направя за член данни оръжие и магия и да ги изициалиризирам като инстанции на оръжие и магия