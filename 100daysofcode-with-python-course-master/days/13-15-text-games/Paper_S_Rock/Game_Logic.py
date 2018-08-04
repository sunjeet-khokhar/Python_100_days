from random import randint
import random


class PSR_player:

    def __init__(self, name):
    pass

class Roll:
    def __init__(self):
        #self.roll_name = ['paper', 'scissors']
        self.roll_name = None
        self.can_defeat = []
        self.can_be_defeated_by = []

    def set_roll(self,roll_name,can_defeat,can_be_defeated_by):
        self.roll_name = roll_name
        self.can_defeat = can_defeat
        self.can_be_defeated_by = can_be_defeated_by












