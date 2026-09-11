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

sightmap = [[-1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1],
            [-1, -1, -1, -1, -1]]
rare_pool = (SuperDice, CatDice, MoneyDice, OnlyDice, PoisonDice, DevilDice, EmergencyDice, LuckyDice)
uncommon_pool = (DemonDice, GamblingDice, RandomDice, AllDice, FiveDice, PetDice, OneDice, EightDice, HugeDice, FishDice)
common_pool = (BabyDice, DinnerDice, SmallHealDice, SmallDice, BigDice, MidDice, DamageDice, GrayDice, RiskyDice, SharpDice, BasicDice)
generate_floor(floor, 5)
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
        if random.randint(0, 3) == 3:
            e = Skeleton()
        else:
            e = Gambler()
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
        camp(player, cam)
        floor[player.pos[0]][player.pos[1]] = '_'
    elif floor[player.pos[0]][player.pos[1]] == '@':
        print('Do you want to fight the boss')
        while True:
            try:
                m = input('1-Yes/2-No')
                if int(m) in (1, 2):
                    m = int(m)
                    break
            except:
                pass
        if m == 2:
            input('Proceed')
            continue
        fight(Serpent(), player)
        end_cutscene()
    elif floor[player.pos[0]][player.pos[1]] == '!':
        caroline.dialog(player)
        floor[player.pos[0]][player.pos[1]] = '_'
    
    input('Proceed')
    continue
