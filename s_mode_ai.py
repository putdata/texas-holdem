from class_card import *
from class_ai import *
from class_player import *

import random
import pygame
import constants as c

deck = []
small_blind = 1
max_player = 2
me = player(1,275)
com = ai(2,250)
divided = False
race_step = 0
bet_state = 50
my_bet = 25
com_bet = 50
def fresh_deck(mode):
    global deck, first
    new = []
    suits = ["SPADE", "HEART", "DIAMOND", "CLUB"]
    ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    for i in range(len(suits)):
        for j in range(len(ranks)):
            new.append((suits[i], ranks[j]))
    random.shuffle(new)

    # 플레이어에게 배분
    for i in range(2):
        for j in range(max_player):
            give = (small_blind + (i*2 + j)) % max_player
            if give == 0:
                give = max_player
            deck.append(card(new[i*2 + j], give, i + 1, mode))

    # 커뮤니티 카드
    for i in range(max_player*2 + 1, max_player*2 + 6):
        deck.append(card(new[i], "COMMUNITY", i - (max_player * 2), mode))


def div_animation():
    i = 0
    while True:
        if deck[i].get_moved:
            deck[i].show()
        else:
            for j in range(i + 1, max_player * 2 + 5):
                deck[j].show()
            deck[i].show(True)
            break
        i += 1
        if i >= max_player * 2 + 5:
            global divided
            divided = True
            break


def GAME_AI_SCREEN(mode):
    global deck, divided, race_step
    if mode == "EASY":
        c.SCREEN.blit(c.AI_EASY_BACK, (0,0))
    elif mode == "NORMAL":
        pass
    elif mode == "HARD":
        pass

    if not deck: # 덱이 비었을때
        fresh_deck(mode)

    if not divided:
        div_animation()
    else:
        opened = False
        check = 0
        for i in range(max_player*2 + 5):
            if deck[i].get_owner == 1 and not deck[i].get_faced:
                deck[i].show(False, True)
            elif race_step and max_player*2 <= i < (max_player*2 + 5) - (3-race_step):
                deck[i].show(False, True)
            else:
                deck[i].show()
            if deck[i].get_faced:
                check += 1

        if check == 2 + (3 if race_step == 1 else (0 if race_step == 0 else 2 + race_step)):
            opened = True

        if opened:
            command = input("콜/레이즈/폴드 : ")
            if command == "콜":
                me.bet(bet_state - my_bet)
                com.bet(bet_state - com_bet)
                race_step += 1