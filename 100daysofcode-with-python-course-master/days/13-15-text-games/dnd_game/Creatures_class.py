import random


class Creature:

    def __init__(self, name, prowess):
        self.name = name
        self.prowess = prowess

    def defence_roll(self):
        roll = random.randint(0,100)
        return roll * self.prowess


class Dragon_Ball(Creature):
    def __init__(self, name, prowess, mutation):
        super().__init__(name, prowess)
        self.mutation = mutation

    def defensive_roll(self):
        roll = super().defensive_roll()
        value = roll * self.mutation
        return value


class Wizard(Creature):

    def attack(self,creature):
        enemy_roll = creature.defence_roll()
        my_roll = self.defence_roll()
        return my_roll >= enemy_roll



