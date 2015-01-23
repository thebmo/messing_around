from monster import Monster
from npc import NPC


class Imp(Monster, NPC):
    
    NAME = 'Imp'
    
    STATS = {
        'STR': 2,
        'AGI': 3,
        'INT': 1,
        'CHA': 0,
        'LCK': 0,
        'max_hp': 6,
        'max_ap': 1,
        'damage': 2,
        'level': 2,
        'exp': 2,
        }
