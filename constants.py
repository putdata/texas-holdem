import pygame

# GUI
GUIWIDTH = 1280
GUIHEIGHT = 800
GUITITLE = "BSIK TEXAS HOLDEM"
SCREEN = pygame.display.set_mode((GUIWIDTH, GUIHEIGHT))

MOUSE_POS = (0,0)
MOUSE_CLICKED = False # 마우스 왼쪽버튼

# COLOUR
WHITE = (255,255,255)
BLACK = (0,0,0)
LOGO_GREEN = (11,148,68)
EASY_COLOUR = (210,200,0)

# SCREEN WHERE
WHERE = "GAME_AI_EASY" # FIRST = LOGO

# LOGO
TEXAS_LOGO = pygame.image.load("img/logo/holdem_logo.png")
CARD_IN_LOGO = pygame.image.load("img/logo/card_in_logo.png")
HAND_IN_LOGO = pygame.image.load("img/logo/hand_in_logo.png")

SELECT_MODE = pygame.image.load("img/logo/button/select_mode.png")
SELECT_MODE_O = pygame.image.load("img/logo/button/select_mode_o.png")
SELECT_MODE_C = pygame.image.load("img/logo/button/select_mode_c.png")

DEVELOPER = pygame.image.load("img/logo/button/developer.png")
DEVELOPER_O = pygame.image.load("img/logo/button/developer_o.png")
DEVELOPER_C = pygame.image.load("img/logo/button/developer_c.png")

D_SCROLL = pygame.image.load("img/logo/scroll.png")
SCROLL_OK = pygame.image.load("img/logo/button/ok.png")
SCROLL_OK_O = pygame.image.load("img/logo/button/ok_o.png")
SCROLL_OK_C = pygame.image.load("img/logo/button/ok_c.png")

FIXED_HAND_X = 950
FIXED_HAND_Y = 400
HAND_X = 950
HAND_Y = 400
HAND_BACK = False

# SELECT MODE
MODE_BACK = pygame.image.load("img/mode/back.png")

MODE_AI = pygame.image.load("img/mode/button/mode_ai.png")
MODE_AI_O = pygame.image.load("img/mode/button/mode_ai_o.png")
MODE_AI_C = pygame.image.load("img/mode/button/mode_ai_c.png")

AI_EASY = pygame.image.load("img/mode/button/ai_easy/easy.png")
AI_EASY_O = pygame.image.load("img/mode/button/ai_easy/easy_o.png")
AI_EASY_C = pygame.image.load("img/mode/button/ai_easy/easy_c.png")

# MODE_AI
AI_EASY_BACK = pygame.image.load("img/ai/easy/back.png")