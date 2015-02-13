"""
    Goblin monster sub-class of parents Monster and NPC.
"""

from monster import Monster
from npc import NPC


class Goblin(Monster, NPC):

    NAME = 'Goblin'

    STATS = {
        'STR': 10,
        'AGI': 7,
        'INT': 4,
        'CHA': 0,
        'LCK': 5,
        'max_hp': 12,
        'max_ap': 0,
        'damage': 7,
        'level': 6,
        'exp': 10,
        'gold': 15,
        }
