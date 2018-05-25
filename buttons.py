from class_button import *

import constants as c

# button in logo
b_select = button((485, 600), c.SELECT_MODE, c.SELECT_MODE_O, c.SELECT_MODE_C)
b_developer = button((485,690), c.DEVELOPER, c.DEVELOPER_O, c.DEVELOPER_C)
b_scroll_ok = button((598,515), c.SCROLL_OK, c.SCROLL_OK_O, c.SCROLL_OK_C)

# button in select mode
b_mode_ai = button((178,116), c.MODE_AI, c.MODE_AI_O, c.MODE_AI_C)
b_ai_easy = button((178,542), c.AI_EASY, c.AI_EASY_O, c.AI_EASY_C)