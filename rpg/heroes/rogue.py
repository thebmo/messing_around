from hero import Hero
from npc import NPC


class Rogue(Hero, NPC):
    
    CLASS = 'Rogue'
    AGI_MOD = 2

    growth = {
        'STR': 1,
        'AGI': 3,
        'INT': 1,
        'CHA': 1,
        'LCK': 1,
        'max_hp': 4,
        'max_ap': 1
        }