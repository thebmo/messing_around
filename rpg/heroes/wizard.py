from hero import Hero


class Wizard(Hero):
    
    CLASS = 'Wizard'
    INT_MOD = 2

    growth = {
        'STR': 1,
        'AGI': 2,
        'INT': 2,
        'CHA': 1,
        'LCK': 1,
        'max_hp': 3,
        'max_ap': 2
        }
