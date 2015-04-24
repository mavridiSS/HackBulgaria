class Enemy:

    def __init__(self, health, mana, damage):
        self.health = health
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

"""
    def take_mana(self, potion=None):
        if isinstance(potion, Mana):
            self.mana += potion.mana
        self.mana += self.mana_regeneration_rate

        if self.mana > self.max_mana:
            self.mana = self.max_mana
    def can_cast(self):
        if self.damage_by_spell == 0 or self.mana_cost > self.mana:
            raise Exception("Cannot cast spell")
        else:
            return True
"""
