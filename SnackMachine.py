import Products
import Payment
from random import randint
from random import random


class SnackMachine:

    def __init__(self, capacity, slots, coins):
        self.capacity = capacity
        self.slots = slots
        self.coins = coins

    def checkAvailableSnack(self, prod):
        if prod.stock > 0 and self.capacity > 0:
            return True
        else:
            return False
