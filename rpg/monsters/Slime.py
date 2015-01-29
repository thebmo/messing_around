from monster import Monster
from npc import NPC


class Slime(Monster, NPC):

    NAME = 'Slime'

    STATS = {
        'STR': 1,
        'AGI': 2,
        'INT': 0,
        'CHA': 0,
        'LCK': 0,
        'max_hp': 5,
        'max_ap': 0,
        'damage': 1,
        'level': 1,
        'exp': 1,
        'gold': 5,
        }
