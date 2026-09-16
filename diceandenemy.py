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
class TogetherDice(Dice):
    def __init__(self):
       super().__init__()
       self.sides = ['i', 'i', 'i', 'i', 'i', 'i']
       self.name = 'Together dice'
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
        self.sides = list(a)
        self.name = 'Infinite sided dice'
class BasicDice(Dice):
    def __init__(self):
       super().__init__()
       self.sides = [1, 2, 3, 4, 5, 6]
       self.name = 'Basic dice'
CD = CustomDice

class Worm(Enemy):
    def __init__(self):
        super().__init__()
        self.name = 'Worm'
        self.hp = 1
        self.dice = [CD(1)]
        self.eq()


class Serpent(Boss):
    def __init__(self):
        super().__init__()
        self.name = 'Serpent'
        self.hp = 300
        self.dice = [CD('@'), CD('+'), CD(4, 5, 6), CD('!')]
        self.eq()
class DeadKing(Boss):
    def __init__(self):
        super().__init__()
        self.name = 'Dead King'
        self.hp = 250
        self.dice = [CD('%', '-'), CD(3, 4), CD(3, 4)]
        self.eq()
class Ghost(Boss):
    def __init__(self):
        super().__init__()
        self.name = 'Ghost'
        self.hp = 150
        self.dice = [CD('!'), CD(4, 1, 1), CD(4, 1), CD(4)]
        self.eq()


class DevilServant(Elite):
    def __init__(self):
        super().__init__()
        self.name = "Devil's Servant"
        self.hp = 100
        self.dice = [CD('%'), CD(3), CD(3)]
        self.eq()
class Keeper(Elite):
    def __init__(self):
        super().__init__()
        self.name = "The Keeper"
        self.hp = 50
        self.dice = [CD('%'), CD('%'), CD('%'), CD(6)]
        self.eq()
class Traveller(Elite):
    def __init__(self):
        super().__init__()
        self.name = "Traveller"
        self.hp = 200
        self.dice = [CD('!'), CD(3), CD(3)]
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
class Goblin(Enemy):
    def __init__(self):
        super().__init__()
        self.name = 'Goblin'
        self.hp = 30
        self.dice = [CD(1, 2, 3), CD(1, 2, 3), CD(1, 2, 3)]
        self.eq()
class Imp(Enemy):
    def __init__(self):
        super().__init__()
        self.name = 'Imp'
        self.hp = 20
        self.dice = [CD('!'), CD('!'), CD('!'), CD(6)]
        self.eq()
class Snakeling(Enemy):
    def __init__(self):
        super().__init__()
        self.name = 'Snakeling'
        self.hp = 30
        self.dice = [CD('@'), CD(1, 2, 3)]
        self.eq()


class Blessed(Boss):
    def __init__(self):
        super().__init__()
        self.name = 'Blessed'
        self.hp = 500
        self.dice = [CD('$'), CD('!'), CD('%'), CD(4, 5, 6), CD(6), CD(6)]
        self.eq()
class Zapper(Boss):
    def __init__(self):
        super().__init__()
        self.name = 'Zapper'
        self.hp = 400
        self.dice = [CD('@'), CD('@'), CD('@'), CD(1, 9), CD(1, 9), CD(1, 9)]
        self.eq()
class Tyrant(Boss):
    def __init__(self):
        super().__init__()
        self.name = 'Tyrant'
        self.hp = 400
        self.dice = [CD('-'), CD('-'), CD('-'), CD('%'), CD(5), CD(5), CD(1, 5)]
        self.eq()

class LesserDemon(Elite):
    def __init__(self):
        super().__init__()
        self.name = "Lesser Demon"
        self.hp = 200
        self.dice = [CD('%'), CD(5), CD(5), CD(6), CD(6), CD(4, 5, 6)]
        self.eq()
class Tongue(Elite):
    def __init__(self):
        super().__init__()
        self.name = "The Tongue"
        self.hp = 300
        self.dice = [CD('@'), CD('@'), CD('@'), CD(1, 2, 3, 4, 5, 6), CD(1, 2, 3, 4, 5, 6), CD(1, 2, 3, 4, 5, 6), CD('x'), CD('x')]
        self.eq()
class Mimic(Elite):
    def __init__(self):
        super().__init__()
        self.name = "Mimic"
        self.hp = 300
        self.dice = [CD('$'), CD(8), CD('%')]
        self.eq()

class Chained(Enemy):
    def __init__(self):
        super().__init__()
        self.name = 'The Chained'
        self.hp = 300
        self.dice = [CD('@'), CD(6), CD(6), CD(4, 5, 6)]
        self.eq()
class Mutant(Enemy):
    def __init__(self):
        super().__init__()
        self.name = 'The Mutant'
        self.hp = 300
        self.dice = [CD('!'), CD(1), CD('-', '-', '%')]
        self.eq()
class Maniac(Enemy):
    def __init__(self):
        super().__init__()
        self.name = 'The Maniac'
        self.hp = 200
        self.dice = [CD('-'), CD('-'), CD('-'), CD(1, 6), CD(1, 6), CD(1, 6), CD(1, 6)]
        self.eq()
class Hydra(Enemy):
    def __init__(self):
        super().__init__()
        self.name = 'The Hydra'
        self.hp = 150
        self.dice = [CD('@'), CD('@'), CD('@')]
        self.eq()
class Nightmare(Enemy):
    def __init__(self):
        super().__init__()
        self.name = 'The Nightmare'
        self.hp = 150
        self.dice = [CD('!'), CD('!'), CD('!'), CD(7), CD(1, 7), CD(1, 1, 1, 7)]
        self.eq()

class Queen(Boss):
    def __init__(self):
        super().__init__()
        self.name = 'Queen of death - Caroline'
        self.hp = 999
        self.dice = [CD('!'), CD('!'), CD('!'), CD(9), CD(1, 9), CD(1, 1, 9), CD(1, 1, 1, 9), CD('%'), CD('%')]
        self.eq()
class DoG(Boss):
    def __init__(self):
        super().__init__()
        self.name = 'DEMON OF GAMBLING'
        self.hp = 999
        self.dice = [CD('!'), CD('!'),  CD('@'), CD('@'), CD('%'), CD('%'), CD(6), CD(6), CD(6)]
        self.eq()
class Mellstroy(Boss):
    def __init__(self):
        super().__init__()
        self.name = 'Меллстрой'
        self.hp = 999
        self.dice = [CD('%'), CD('%'), CD('%'), CD('%'), CD('%'), CD(1)]
        self.eq()

class Warrior(Elite):
    def __init__(self):
        super().__init__()
        self.name = "Warrior"
        self.hp = 900
        self.dice = [CD('%'), CD(9), CD(9), CD('%')]
        self.eq()
class Angel(Elite):
    def __init__(self):
        super().__init__()
        self.name = "Slaved Angel"
        self.hp = 900
        self.dice = [CD('!'), CD('!'), CD('!'), CD('!'), CD('!'), CD(6), CD(7), CD('%'), CD('%'), CD('%'), CD('%'), CD('%'), ]
        self.eq()
class Cleaner(Elite):
    def __init__(self):
        super().__init__()
        self.name = "Cleaner"
        self.hp = 900
        self.dice = [CD(8), CD(8), CD(8)]
        self.eq()

class Giant(Enemy):
    def __init__(self):
        super().__init__()
        self.name = 'The Giant'
        self.hp = 700
        self.dice = [CD('%'), CD(6), CD(6), CD(6)]
        self.eq()
class Head(Enemy):
    def __init__(self):
        super().__init__()
        self.name = 'The Head'
        self.hp = 700
        self.dice = [CD('!'), CD('!'), CD('!'), CD(9), CD(9), CD('%')]
        self.eq()
class Gargoyle(Enemy):
    def __init__(self):
        super().__init__()
        self.name = 'The Gargoyle'
        self.hp = 600
        self.dice = [CD('@'), CD('@'), CD('@'), CD('@'), CD('@'), CD('@'), CD('@'), CD('!')]
        self.eq()
class LilGod(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "The Lil God"
        self.hp = 800
        self.dice = [CD('%'), CD(7), CD(7), CD(1, 1, 7)]
        self.eq()
class Bloom(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "The Bloom"
        self.hp = 600
        self.dice = [CD('!'), CD('!'), CD('!'), CD('!'), CD('!'), CD('!'), CD('!'), CD('%'), CD(9)]
        self.eq()
