from hero import Hero


class Rogue(Hero):

    stats = {
        'STR': 0,
        'AGI': 0,
        'INT': 0,
        'CHA': 0,
        'LCK': 0,
        'max_hp': 0,
        'max_ap': 0
        }

    growth = {
        'STR': 1,
        'AGI': 3,
        'INT': 1,
        'CHA': 1,
        'LCK': 1,
        'max_hp': 4,
        'max_ap': 1
        }
    
    CLASS = 'Rogue'
    AGI_MOD = 2
