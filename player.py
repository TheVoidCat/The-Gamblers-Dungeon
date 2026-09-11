from time import sleep as zzz
import random
from engine import *
from diceandenemy import *
from art import *
class Player():
    def __init__(self):
        self.name = 'You'
        self.maxhp = 30
        self.hp = 30
        self.dpt = 3
        self.pos = [2, 2]
        self.inv = ['Bag of dice']
        self.dice = [BasicDice(), BasicDice(), BasicDice(), BasicDice(), BasicDice()]
        self.souls = 0
        self.desc = {'Bag of dice':'A bag for dice'}
    def attack(self, e):
        print('Time to roll the dice')
        zzz(1)
        r, a = roll(self)
        while True:
            print(*a)
            try:
                t = list(map(mint, input(f'Choose {self.dpt} to play ').split()))
                zzz(1)
                if len(set(t)) <= self.dpt and len(t) <= self.dpt and len(set(t)) == len(t):
                    d = dict()
                    for i in t:
                        if a[i] not in d:
                            d[a[i]] = 0
                        d[a[i]] += 1
                    f = True
                    for i in d:
                        if i in r:
                            if r[i]-d[i] >= 0:
                                pass
                            else:
                                f = False
                                break
                        else:
                            f = False
                            break
                    if not f:
                        continue
                else:
                    continue
                for i in range(self.dpt):
                    t[i] = a[t[i]]
                d = dict()
                for i in t:
                    if i not in d:
                        d[i] = 0
                    d[i] += 1
                calculate(self, e, r, d)
                break
            except:
                pass
    def __sub__(self, am):
        print(f' - {am} hp')
        zzz(1)
        self.hp -= am
        if self.hp <= 0:
            self.hp = 0
            death_cutscene()
        print(f'You have {self.hp} left')
    def __add__(self, am):
        self.hp += am
        if self.hp > self.maxhp:
            self.hp = self.maxhp
        print(f' + {am} hp')
        zzz(1)
        print(f'You have {self.hp} hp')
        zzz(1)
class Caroline():
    def __init__(self):
        self.rep = 0
        self.alive = True
    def dialog(self, player):
        if not self.alive:
            print('You thought you heard a strange noise...')
            zzz(1)
            print("Maybe it was an enemy you've just killed")
            return None
        if self.rep == 0:
            print('You see a girl standing in a corner')
            zzz(1)
            print('Caroline: AAAAAA')
            zzz(1)
            print('Caroline: What?')
            zzz(1)
            print("Caroline: Why didn't I die?")
            zzz(1)
            print('You step into a circle of light')
            zzz(1)
            print('Caroline: Kitty?')
            zzz(1)
            print('Caroline: Whas it you, who saved me?')
            zzz(1)
            print("Caroline: Come closer. I won't harm you")
            zzz(1)
            print('KILL HER, PUPPET')
            zzz(1)
            print('1) KILL')
            print('2) REFUSE')
            while True:
                try:
                    a = input('What shall I do? ')
                    if int(a) in (1, 2):
                        a = int(a)
                        break
                except:
                    pass
            if a == 1:
                print('You surround the girl with dice')
                zzz(1)
                print('She dies')
                zzz(1)
                print('YES, PUPPET')
                self.alive = False
            else:
                print('You come closer')
                zzz(1)
                print('Caroline: Hi, Kitty, I am Caroline')
                zzz(1)
                print('You nuzzle her')
                zzz(1)
                print('Caroline: Oh, Kitty!')
                zzz(1)
                print('Caroline: Lets be friends')
                zzz(1)
                print('You: Meow!')
                self.rep+=1
        elif self.rep == 1:
            print('You see Caroline standing in a corner')
            zzz(1)
            print('Caroline: Kitty, you saved me!')
            zzz(1)
            print('Caroline: AGAIN!')
            zzz(1)
            print('Caroline: Kitty, you know')
            zzz(1)
            print('Caroline: I have no idea how i got here')
            zzz(1)
            print("Caroline: I don't remember anything")
            zzz(1)
            print('Caroline: But I know you are my friend')
            zzz(1)
            print('You: Meow!')
            self.rep+=1
        elif self.rep == 2:
            print('You see Caroline standing in a corner')
            zzz(1)
            print('Caroline: You saved me!')
            zzz(1)
            print('Caroline: For the 3rd time already')
            zzz(1)
            print('Caroline: I seriosly need a way to defend myself')
            zzz(1)
            print('Caroline: You could teach me?')
            zzz(1)
            print('Caroline: Yes! That would be awesome!')
            zzz(1)
            print('You train for a lot of time...')
            zzz(1)
            print('Caroline: Thanks, Kitty!')
            zzz(1)
            print('You: Meow!')
            zzz(1)
            print('Caroline: Wait, I almost forgot!')
            zzz(1)
            print('Caroline: Kitty, I made these dice for you!')
            zzz(1)
            player.dice.append(FriendshipDice)
            print('Caroline: They have the power of ours friendship!')
            zzz(1)
            print('Caroline: With the skills you gave me I can even defeat the...')
            zzz(1)
            print("Caroline: Wait, I don't remember...")
            zzz(1)
            print('Caroline: But its allright!')
            zzz(1)
            print('You: Meow')
            self.rep+=1
        else:
            print('You see Caroline defeat a Gambler')
            zzz(1)
            print('Caroline: Hi, Kitty!')
            zzz(1)
            print('You: Meow')
def generate_floor(floor, w):
    shadow = []
    for i in range(w):
        shadow.append([0]*w)
    shadow[w//2][w//2] = 1
    o = [w//2, w//2]
    stack = []
    for i in range(random.randint(2, 4)):
        stack.append(o)
    ways = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    c = random.randint(w+2, w+6)
    while stack != [] and c > 0:
        cur = stack.pop(0)
        f = True
        for i, g in ways:
            try:
                if shadow[cur[0]+i][cur[1]+g] == 0:
                    f = False
                    break
            except:
                pass
        if not f:
            new = cur
            while True:
                try:
                    ch = random.choice(ways)
                    new = [cur[0]+ch[0], cur[1]+ch[1]]
                    if shadow[new[0]][new[1]] != 1:
                        break
                except:
                    pass
            shadow[new[0]][new[1]] = 1
            stack.append(new)
            c-=1
    c = 0
    for i in shadow:
        for g in i:
            if g == 1:
                c+=1
    c-=1
    pool = []
    s = w//2-2
    e = w//2-1
    r = w//2-1
    if c > w+3:
        s+=1
        e+=1
        r+=1
    for i in range(s):
        pool.append('$')
    for i in range(e):
        pool.append('#')
    for i in range(r):
        pool.append('&')
    for i in range(c-sum((s, e, r))):
        pool.append('#')
    for i in range(w):
        for g in range(w):
            if i == w//2 and g == w//2:
                floor[i][g] = '@'
                continue
            if shadow[i][g] == 0:
                floor[i][g] = ' '
            else:
                floor[i][g] = random.choice(pool)
                pool.remove(floor[i][g])
def update_sightmap(sightmap, player):
    for i in range(-1, 2):
        for g in range(-1, 2):
            try:
                if i==0 and g==i:
                    sightmap[player.pos[0]][player.pos[1]] = 1
                else:
                    if sightmap[player.pos[0]+i][player.pos[1]+g] == -1:
                        sightmap[player.pos[0]+i][player.pos[1]+g] = 1
        
            except:
                pass

def drawUI(player, floor, sightmap):
    update_sightmap(sightmap, player)
    floorm = []
    for i in range(len(floor)):
        floorm.append([' ']*len(floor))
    for i in range(5):
        for g in range(5):
            if sightmap[i][g] == -1:
                floorm[i][g] = '*'
            elif sightmap[i][g] == 0 and floor[i][g] != ' ':
                floorm[i][g] = '#'
            else:
                floorm[i][g] = floor[i][g]
    floorm[player.pos[0]][player.pos[1]] = '^'
    print(f' HP: {player.hp}                                                                                                                                        SOULS: {player.souls}')
    print(f'                                                                                                                                                         -----------')
    print(f'                                                                                                                                                        |', *floorm[0], '|')
    print(f'   ^                                                                                                                                                    |', *floorm[1], '|')
    print(f' <   > - to Move                                                                                                                                        |', *floorm[2], '|')
    print(f'   v                                                                                                                                                    |', *floorm[3], '|')
    print(f'                                                                                                                                                        |', *floorm[4], '|')
    print(f'                                                                                                                                                         -----------')
def end_cutscene():
    print('HELLO, PUPPET, THANK YOU FOR THE SOULS')
    zzz(1)
    print('RETURN BACK, PUPPET')
    zzz(1)
    print('YOU DIED')
    zzz(1)
    print('You black out')
    exit()
def death_cutscene():
    print(f'YOU DIE')
    zzz(1)
    print(f'The Gambling Demon takes your soul')
    zzz(1)
    print(f'GOOD BYE MY PUPPET, BETTER LUCK NEXT TIME')
    zzz(1)
    print(f'You black out')
    exit()
def intro_cutscene():
    print('THE GAMBLING DUNGEON')
    input('PLAY')
    print('\n'*45)
    print('You feel being rebuild by someone')
    zzz(1)
    print('You were brought back to life by Gambling Demon')
    zzz(1)
    print('COLLECT THE SOULS')
    zzz(1)
def move(player, floor):
    m = input('Where should I go?')
    while True:
        if m == 'i':
            show_inventory(player)
        else:
            try:
                g = {'^':[-1, 0], '>':[0, 1], '<':[0, -1], 'v':[1, 0]}
                m = g[m]
                if floor[player.pos[0]+m[0]][player.pos[1]+m[1]] != ' ':
                    break
            except:
                pass
        m = input('Where should I go?')
    player.pos = [player.pos[0]+m[0], player.pos[1]+m[1]]
    print(45*'\n')
def show_inventory(player):
    for i in player.dice:
        print(i)
def fight(e, player):
    print(f'You VS {e.name}')
    zzz(3)
    input('Player roll! ')
    player.attack(e)
    while e.hp > 0:
        print(f'{e.name} roll!')
        zzz(1)
        e.attack(player)
        input('Player roll! ')
        player.attack(e)
    clear_cache(player)
    print('You got 1 soul')
    player.souls += 1
    zzz(1)
def camp(player, cam):
    print(cam)
    print('You see a campfire. What will you do?')
    zzz(1)
    print('1) Rest. Heal 15 hp')
    zzz(1)
    print('2) Practice. Transform to 6')
    a = input('1) or 2)')
    while a != '1' and a != '2':
        a = input('1) or 2)')
    if a == '1':
        player + 15
        zzz(1)
    else:
        transform(player, 6)
def reward(player, c, u, r, rew, am=3, boss=False):
    a = []
    for i in range(am):
        ch = random.randint(1, 24)
        if ch == 24 or boss:
            a.append(random.choice(r)())
        elif ch in (17, 18, 19, 20, 21, 22, 23 ):
            a.append(random.choice(u)())
        else:
            a.append(random.choice(c)())
    print(rew)
    print('0) skip, gain 1 dpt')
    for i in range(1, am+1):
        print(f'{i})', a[i-1])
    s = input('Choose ')
    while True:
        try:
            if int(s) in range(am+1):
                s = int(s)
                break
        except:
            pass
        s = input('Choose ')
    if s == 0:
        print('Skipped')
        zzz(1)
        player.dpt += 1
        if player.dpt > len(player.dice):
            self.dpt = len(player.dice)
        return None
    player.dice.append(a[s-1])
    print('Added', a[s-1])
    zzz(1)
def shop(player, c, u, r, sho):
    rarit = (c, u, r)
    price = (random.randint(1, 4), random.randint(5, 9), random.randint(10, 14))
    ch = []
    for i in range(3):
        ch.append(random.choice(rarit[i])())
    f = True
    print('You step into a little shop')
    zzz(1)
    print(sho)
    zzz(1)
    print()
    while f:
        try:
            print('0) leave')
            for i in range(3):
                if ch[i] != 'Sold Out':
                    print(f'{i+1})', ch[i], f'for {price[i]} souls')
                else:
                    print('f{i+1}) Sold Out')
            while True:
                t = input('Choose ')
                if int(t) in range(4):
                    t = int(t)
                    if t == 0:
                        print('You Left')
                        zzz(1)
                        f = False
                        break
                    t -= 1
                    if price[t] <= player.souls or ch[t] == 'Sold Out':
                        player.souls -= price[t]
                        print(f'Bought {ch[i]}')
                        zzz(1)
                        print('Yesss, Soulsss')
                        zzz(1)
                        print('Give more')
                        player.dice.append(ch[i])
                        ch[i] = 'Sold Out'
                        break
                    elif ch[t] == 'Sold Out':
                        continue
                    else:
                        print('No soulsss?!')
                        zzz(1)
                        print('Leave!')
                        f = False
                        break
        except:
            pass
