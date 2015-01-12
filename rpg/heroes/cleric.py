from hero import Hero


class Cleric(Hero):

    CLASS = 'Cleric'
    INT_MOD = 2
    
    growth = {
        'STR': 2,
        'AGI': 1,
        'INT': 2,
        'CHA': 1,
        'LCK': 1,
        'max_hp': 3,
        'max_ap': 2
        }
