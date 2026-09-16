from time import sleep as zzz
import random
def mint(a):
    return int(a)-1
def roll(p):
    s = len(p.dice)
    d = dict()
    h = []
    print(s*'*')
    for i in p.dice:
        c = random.choice(i.sides)
        h.append(c)
        if c not in d:
            d[c] = 0
        d[c] += 1
        print(*h, (s-len(h))*'*', sep = '')
        zzz(1.5/s)
    return d, h
def calculate(p, target, d, t):
    for i in '+-&^?$~x@%!oi':
        if i not in d:
            d[i] = 0
        if i not in t:
            t[i] = 0
    x = 1
    for i in range(d['x']):
        x+=1
        print(f'{p.name} +1 mult')
    for i in range(d['+']*x):
        p + 2
    for i in range(d['o']*x):
        c = 0
        for g in p.dice:
            for z in g.sides:
                if z == 1:
                    c+=1
        target - c
    for i in range(d['%']):
        p.dice.append(TempDemonDice())
        print(f'{p.name} gained strength')
    for i in range(d['!']):
        p.dice.append(TempHealDice())
        print(f'{p.name} gained dexterity')
    for i in range(d['i']):
        p.dice.append(TempFishDice())
        print(f'{p.name} summoned fishes')
    for i in range(d['-']*x):
        p - 1
    
    for i in range(d['$']*x):
        p.souls+=1
        print(f'{p.name} focused a soul')
    for i in range(t['+']*x):
        p + 3
    for i in range(t['@']*x):
        target.dice.append(StatusDice())
        print(f'{target.name} was poisoned')
    for i in range(t['^']*x):
        c = 0
        for g in range(d['~']):
            c+=1
        target - c*9
    for i in range(t['&']*x):
        c = 0
        for g in p.dice:
            for z in g.sides:
                if z == '+':
                    c+=1
        target - c*3
    for i in range(t['?']*x):
        c = random.randint(1, 3)
        if c == 1:
            c = random.randint(1, 6)
            p + c
        elif c == 2:
            c = random.randint(1, 6)
            p - c
        else:
            c1 = random.randint(1, 6)
            c2 = random.randint(1, 6)
            c3 = random.randint(1, 6)
            t - c1*c2*c3
    k = {}
    for i in t:
        try:
            k[int(i)] = t[int(i)]
        except:
            pass
    c = 0
    for i in k:
          c+=i**k[i]
    target - c*x
def transform(p, target):
    for i in p.dice:
        print(*i.sides)
    a = input(f'Choose from what dice to transform into {target}')
    while True:
        try:
            if int(a) in range(1, len(p.dice)+1):
                a = int(a)-1
                break
        except:
            pass
        a = input(f'Choose from what dice to transform into {target}')
    print(*p.dice[a].sides)
    b = input(f'Choose what side to transform into {target}')
    while True:
        try:
            if int(b) in range(1, len(p.dice[a].sides)+1):
                b = int(b)-1
                break
        except:
            pass
        b = input(f'Choose what side to transform into {target}')
    p.dice[a].sides[b] = target
    print('Now it is done')
def clear_cache(p):
    c = []
    for i in p.dice:
        if not i.temp:
            c.append(i)
    p.dice = c
class Dice():
    def __init__(self):
        self.sides = []
        self.name = ''
        self.temp = False
    def __str__(self):
        c = []
        for i in self.sides:
            c.append(str(i))
        return f'Cube {self.name} '+' '.join(c)
class HealDice(Dice):
    def __init__(self):
       super().__init__()
       self.sides = ['+', '+', '+', '+', '+', '+']
       self.name = 'Heal dice'
class DemonDice(Dice):
    def __init__(self):
       super().__init__()
       self.sides = ['x', 'x', 'x', 'x', 'x', 'x']
       self.name = 'Demon dice'
class FishDice(Dice):
    def __init__(self):
       super().__init__()
       self.sides = ['~', '~', '~', '~', '~', '~']
       self.name = 'Fish dice'
class TempFishDice(FishDice):
    def __init__(self):
       super().__init__()
       self.temp = True
class TempDemonDice(DemonDice):
    def __init__(self):
       super().__init__()
       self.temp = True
class TempHealDice(HealDice):
    def __init__(self):
        super().__init__()
        self.temp = True
class StatusDice(Dice):
    def __init__(self):
       super().__init__()
       self.sides = ['-', '-', '-', '-', '-', '-']
       self.name = 'Status dice'
       self.temp = True

class Enemy():
    def __init__(self):
        self.maxhp = 50
        self.hp = 50
        self.souls = random.randint(1, 4)
        self.dice = []
        self.elite = False
        self.guard = False
        if random.randint(1, 6) == 6:
            self.guard = True
        self.name = ''
    def eq(self):
        self.maxhp = self.hp
    def attack(self, p):
        r, a = roll(self)
        calculate(self, p, r, r)
    def __sub__(self, am):
        if self.hp > 0:
            print(f'{self.name} - {am} hp')
            zzz(1)
            self.hp -= am
            if self.hp <= 0:
                self.hp = 0
                print(f'{self.name} dies')
                zzz(1)
                print(f'Its souls are now yours')
                return None
            print(f'{self.name} still stands with {self.hp}')
    def __add__(self, am):
        self.hp += am
        if self.hp > self.maxhp:
            self.hp = self.maxhp
        print(f'{self.name} + {am} hp')

class Elite(Enemy):
    def __init__(self):
        super().__init__()
        self.souls = random.randint(5, 9)
        self.guard = False
        self.elite = True

class Boss(Enemy):
    def __init__(self):
        super().__init__()
        self.souls = random.randint(10, 16)
        self.guard = False

