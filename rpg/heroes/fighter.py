from hero import Hero
from npc import NPC


class Fighter(Hero, NPC):
    
    # class variiables
    CLASS = 'Fighter'
    STR_MOD = 2
    
    growth = {
        'STR': 3,
        'AGI': 1,
        'INT': 1,
        'CHA': 1,
        'LCK': 1,
        'max_hp': 4,
        'max_ap': 1
        }
