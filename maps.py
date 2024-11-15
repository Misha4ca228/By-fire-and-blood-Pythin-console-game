
obj_build = {
    'empty':"\033[32m.\033[0m",
    'wall':"\033[38;5;130m#\033[0m",
    'water':"\033[34m~\033[0m",
    'port':"\033[90mP\033[0m",
    'industrial':"\033[90mI\033[0m",
    'weapons_store':'\033[90mW\033[0m',
    'job': "\033[90mJ\033[0m",
    'store':"\033[38;5;220mS\033[0m",
    'food':"\033[38;5;220mF\033[0m",
    'home': "\033[38;5;196mH\033[0m",
    'medical':"\033[38;5;156mM\033[0m",
    'gumir': "\033[36mg\033[0m",
    'yakov':"\033[36my\033[0m",
    'bought_home': "\033[32mH\033[0m",
    'player': "\033[36m●\033[0m",
    'casino':"\033[38;5;220mK\033[0m",

    'business': "\033[38;5;220mB\033[0m",
    'business_restaurant':1,
    'business_stall':2,

    'business_restaurant_bought':100,
    'business_stall_bought':200,


}
main_map = {
    (0, 0): obj_build['business'], (1, 0): obj_build['store'], (2, 0): obj_build['wall'], (3, 0): obj_build['wall'],
    (0, 2): obj_build['medical'], (2, 2): obj_build['wall'], (4, 2): obj_build['food'], (5, 2): obj_build['home'], (14, 2): obj_build['bought_home'],
    (0, 3): obj_build['home'], (2, 3): obj_build['business'],(2, 6): obj_build['weapons_store'],
    (0, 4): obj_build['casino'], (2, 4): obj_build['wall'],
    (12, 5): obj_build['store'], (14, 5): obj_build['home'],
    (0, 6): obj_build['wall'],  (12, 6): obj_build['wall'], (14, 6): obj_build['industrial'],(14, 7): obj_build['food'],
    (0, 7): obj_build['store'], (14, 0): obj_build['job'], (1, 6): obj_build['wall'],(9,11):obj_build['port'],
    (14, 10): obj_build['water'],
    (14, 11): obj_build['water'],(13, 11): obj_build['water'],(12, 11): obj_build['water'],(11, 11): obj_build['water'],(10, 11): obj_build['water'],
    (9, 12): obj_build['water'],(10, 12): obj_build['water'], (11, 12): obj_build['water'], (12, 12): obj_build['water'], (13, 12): obj_build['water'], (14, 12): obj_build['water'],
    (5, 13): obj_build['water'], (6, 13): obj_build['water'], (7, 13): obj_build['water'], (8, 13): obj_build['water'], (9, 13): obj_build['water'],
    (10, 13): obj_build['water'], (11, 13): obj_build['water'], (12, 13): obj_build['water'], (13, 13): obj_build['water'], (14, 13): obj_build['water'],
    (14, 1): obj_build['gumir'],
    (8, 12): obj_build['yakov']
}
two_main_map = {
    (0, 0): obj_build['business_stall'], (1, 0): obj_build['store'], (2, 0): obj_build['wall'], (3, 0): obj_build['wall'],
    (0, 2): obj_build['medical'], (2, 2): obj_build['wall'], (4, 2): obj_build['food'], (5, 2): obj_build['home'], (14, 2): obj_build['bought_home'],
    (0, 3): obj_build['home'], (2, 3): obj_build['business_restaurant'],(2, 6): obj_build['weapons_store'],
    (0, 4): obj_build['casino'], (2, 4): obj_build['wall'],
    (12, 5): obj_build['store'], (14, 5): obj_build['home'],
    (0, 6): obj_build['wall'],  (12, 6): obj_build['wall'], (14, 6): obj_build['industrial'],(14, 7): obj_build['food'],
    (0, 7): obj_build['store'], (14, 0): obj_build['job'], (1, 6): obj_build['wall'],(9,11):obj_build['port'],
    (14, 10): obj_build['water'],
    (14, 11): obj_build['water'],(13, 11): obj_build['water'],(12, 11): obj_build['water'],(11, 11): obj_build['water'],(10, 11): obj_build['water'],
    (9, 12): obj_build['water'],(10, 12): obj_build['water'], (11, 12): obj_build['water'], (12, 12): obj_build['water'], (13, 12): obj_build['water'], (14, 12): obj_build['water'],
    (5, 13): obj_build['water'], (6, 13): obj_build['water'], (7, 13): obj_build['water'], (8, 13): obj_build['water'], (9, 13): obj_build['water'],
    (10, 13): obj_build['water'], (11, 13): obj_build['water'], (12, 13): obj_build['water'], (13, 13): obj_build['water'], (14, 13): obj_build['water'],
    (14, 1): obj_build['gumir'],
    (8, 12): obj_build['yakov']
}
