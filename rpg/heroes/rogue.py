from hero import Hero


class Rogue(Hero):
    
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