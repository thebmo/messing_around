from hero import Hero


class Wizard(Hero):

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
        'AGI': 2,
        'INT': 2,
        'CHA': 1,
        'LCK': 1,
        'max_hp': 3,
        'max_ap': 2
        }
    
    CLASS = 'Wizard'
    INT_MOD = 2
