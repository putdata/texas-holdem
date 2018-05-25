import pygame
import constants as c
import buttons as b

def MODE_SCREEN():
    c.SCREEN.blit(c.MODE_BACK, (0,0))
    b.b_mode_ai()
    if b.b_mode_ai.motion:
        b.b_ai_easy()
        if b.b_ai_easy.motion:
            c.WHERE = "GAME_AI_EASY" # EASY GAME
            b.b_ai_easy.reset