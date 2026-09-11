from time import sleep as zzz
import random
from engine import *

class BabyDice(Dice):
    def __init__(self):
       super().__init__()
       self.sides = [1, 2, 1, 2, 1, 2]
       self.name = 'Baby dice'
class DinnerDice(Dice):
    def __init__(self):
       super().__init__()
       self.sides = ['+', '~', '+', '~', '+', '~']
       self.name = 'Dinner dice'
class GamblingDice(Dice):
    def __init__(self):
       super().__init__()
       self.sides = ['$', '-', '$', '-', '$', '-']
       self.name = 'Gambling dice'
class RandomDice(Dice):
    def __init__(self):
        super().__init__()
        self.sides = ['?', '?', '?', '?', '?', '?']
        self.name = 'Random dice'
class AllDice(Dice):
    def __init__(self):
       super().__init__()
       self.sides = ['?', 'x', '$', '-', '+', '~']
       self.name = 'All in one dice'
class SuperDice(Dice):
    def __init__(self):
       super().__init__()
       self.sides = [6, 5, 6, 5, 6, 5]
       self.name = 'Super dice'
class CatDice(Dice):
    def __init__(self):
       super().__init__()
       self.sides = ['^', '^', '^', '^', '^', '^']
       self.name = 'Cat dice'
class FriendshipDice(Dice):
    def __init__(self):
       super().__init__()
       self.sides = ['&', '+', '+', '+', '+', '+']
       self.name = 'Friendship dice'
class SmallHealDice(Dice):
    def __init__(self):
       super().__init__()
       self.sides = [1, '+', 2, '+', 3, '+']
       self.name = 'Small Heal dice'
class SmallDice(Dice):
    def __init__(self):
       super().__init__()
       self.sides = [1, 2, 3, 1, 2, 3]
       self.name = 'Small dice'
class BigDice(Dice):
    def __init__(self):
       super().__init__()
       self.sides = [4, 5, 6, 4, 5, 6]
       self.name = 'Big dice'
class MidDice(Dice):
    def __init__(self):
       super().__init__()
       self.sides = [3, 4, 3, 4, 3, 4]
       self.name = 'Mid dice'
class DamageDice(Dice):
    def __init__(self):
       super().__init__()
       self.sides = [6, 6, 6, 6, '-', '-']
       self.name = 'Damage dice'
class CursedDice(Dice):
    def __init__(self):
       super().__init__()
       self.sides = ['-', '-', '-', '-', '-', '-']
       self.name = 'Cursed dice'
class GrayDice(Dice):
    def __init__(self):
       super().__init__()
       self.sides = [1, '~', 1, '~', 1, '~']
       self.name = 'Gray dice'
class FiveDice(Dice):
    def __init__(self):
       super().__init__()
       self.sides = [5, 5, 5, 5, 5, '~']
       self.name = 'Five dice'
class MoneyDice(Dice):
    def __init__(self):
       super().__init__()
       self.sides = ['$', '$', '$', '$', '$', '$']
       self.name = 'Money dice'
class FishDice(Dice):
    def __init__(self):
       super().__init__()
       self.sides = ['~', '~', '~', '~', '~', '~']
       self.name = 'Fish dice'
class PetDice(Dice):
    def __init__(self):
       super().__init__()
       self.sides = ['^', '~', '^', '~', '^', '~']
       self.name = 'Pet dice'
class OnlyDice(Dice):
    def __init__(self):
       super().__init__()
       self.sides = ['-']
       self.name = 'Only dice'
class PoisonDice(Dice):
    def __init__(self):
       super().__init__()
       self.sides = ['@', '@', '@', '@', '@', '@']
       self.name = 'Poison dice'
class DevilDice(Dice):
    def __init__(self):
       super().__init__()
       self.sides = ['-', '-', '-', '%', '%', '%']
       self.name = 'Devil dice'
class EmergencyDice(Dice):
    def __init__(self):
       super().__init__()
       self.sides = ['~', '~', '+', '+', '!', '!']
       self.name = 'Emergency dice'
class LuckyDice(Dice):
    def __init__(self):
       super().__init__()
       self.sides = [7, 7, 7]
       self.name = 'Lucky dice'
class RiskyDice(Dice):
    def __init__(self):
       super().__init__()
       self.sides = [7, 7, 7, '-', '-', '-']
       self.name = 'Risky dice'
class SharpDice(Dice):
    def __init__(self):
       super().__init__()
       self.sides = [9, 9, '-', '-', '-', '-']
       self.name = 'Sharp dice'
class OneDice(Dice):
    def __init__(self):
       super().__init__()
       self.sides = ['o', 'o', 'o', 'o', 'o', 'o']
       self.name = 'One dice'
class EightDice(Dice):
    def __init__(self):
       super().__init__()
       self.sides = [8, 8, '~', '~', '~', '~']
       self.name = 'Eight dice'
class HugeDice(Dice):
    def __init__(self):
       super().__init__()
       self.sides = [7, 8, 9, 7, 8, 9]
       self.name = 'Huge dice'
class CustomDice(Dice):
    def __init__(self, *a):
        super().__init__()
        self.sides = a
        self.name = 'Infinite sided dice'
class BasicDice(Dice):
    def __init__(self):
       super().__init__()
       self.sides = [1, 2, 3, 4, 5, 6]
       self.name = 'Basic dice'
CD = CustomDice

class Serpent(Enemy):
    def __init__(self):
        super().__init__()
        self.name = 'Serpent'
        self.hp = 300
        self.dice = [CD('@'), CD('+'), CD(4, 5, 6), CD('-', '%')]
        self.eq()

class Gambler(Enemy):
    def __init__(self):
        super().__init__()
        self.name = 'Gambler'
        self.hp = 30
        self.dice = [CD(1, 2, 3), CD(1, 2, 3)]
        self.eq()
class Skeleton(Enemy):
    def __init__(self):
        super().__init__()
        self.name = 'Skeleton'
        self.hp = 40
        self.dice = [CD(2, 3), CD(2, 3)]
        self.eq()
