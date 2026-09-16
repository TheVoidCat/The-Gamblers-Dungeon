from time import sleep as zzz
import random
from engine import *
from diceandenemy import *
from player import *
from art import *
floor = [[' ', ' ', '#', '#', ' '],
         [' ', ' ', '#', ' ', '#'],
         ['#', ' ', '@', '#', '#'],
         ['#', '#', '#', ' ', ' '],
         [' ', '#', '#', ' ', ' ']]
sightmap = []
for i in range(5):
    sightmap.append([-1]*5)
rare_pool = (SuperDice, CatDice, MoneyDice, OnlyDice, PoisonDice, DevilDice, EmergencyDice, LuckyDice, TogetherDice)
uncommon_pool = (DemonDice, GamblingDice, RandomDice, AllDice, FiveDice, PetDice, OneDice, EightDice, HugeDice, FishDice)
common_pool = (BabyDice, DinnerDice, SmallHealDice, SmallDice, BigDice, MidDice, DamageDice, GrayDice, RiskyDice, SharpDice, BasicDice)
generate_floor(floor, 5)
a1l = (DevilServant, Keeper, Traveller)
a2l = (Mimic, Tongue, LesserDemon)
a3l = (Warrior, Angel, Cleaner)
a1e = (Gambler, Skeleton, Goblin, Imp, Snakeling)
a2e = (Nightmare, Hydra, Maniac, Mutant, Chained)
a3e = (Giant, Head, Gargoyle, LilGod, Bloom)
a1b = (Serpent, DeadKing, Ghost)
a2b = (Tyrant, Zapper, Blessed)
a3b = (Worm)
player = Player()
caroline = Caroline()
ending = 0
fnum = 1
intro_cutscene()
game = True
while game:
    print('\n'*45)
    drawUI(player, floor, sightmap)
    move(player, floor)
    insight = sightmap[player.pos[0]][player.pos[1]]
    drawUI(player, floor, sightmap)
    if floor[player.pos[0]][player.pos[1]] == '_':
        print('The room seems empty')
        zzz(1)
    elif floor[player.pos[0]][player.pos[1]] == '#':
        e = None
        ae = (a1e, a2e, a3e)
        e = random.choice(ae[player.act-1])()
        fight(e, player)
        reward(player, common_pool, uncommon_pool, rare_pool, rew)
        if e.guard:
            floor[player.pos[0]][player.pos[1]] = '!'
        else:
            floor[player.pos[0]][player.pos[1]] = '_'
    elif floor[player.pos[0]][player.pos[1]] == '$':
        shop(player, common_pool, uncommon_pool, rare_pool, sho)
        floor[player.pos[0]][player.pos[1]] = '_'
    elif floor[player.pos[0]][player.pos[1]] == '&':
        if player.act == 3 and random.randint(1, 2) == 1:
            hamam(player, cam)
        else:
            camp(player, cam)
        floor[player.pos[0]][player.pos[1]] = '_'
    elif floor[player.pos[0]][player.pos[1]] == 'X':
        e = None
        ae = (a1l, a2l, a3l)
        e = random.choice(ae[player.act-1])()
        fight(e, player)
        reward(player, common_pool, uncommon_pool, rare_pool, rew)
        transform(player, random.choice((1, 2, 3, 4, 5, 6, 7, 8, 9, '+', '-', '&', '^', '?', '$', '~', 'x', '@', '%', '!', 'o', 'i')))
    elif floor[player.pos[0]][player.pos[1]] == '@':
        if player.act == 3:
            print('Do you want to fight the boss')
            while True:
                try:
                    m = input('1-Yes/2-No')
                    if int(m) in (1, 2):
                        m = int(m)
                        break
                except:
                    pass
            if m == 1:
                bossfight(player, caroline)
                break
        if portal(player, a1b, a2b, a3b):
            floor, sightmap = next_act(player, sightmap, floor)
    elif floor[player.pos[0]][player.pos[1]] == '!':
        caroline.dialog(player)
        floor[player.pos[0]][player.pos[1]] = '_'
    input('Proceed')
    continue
