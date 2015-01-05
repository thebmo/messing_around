from hero import Hero


class Cleric(Hero):

    CLASS = 'Cleric'
    INT_MOD = 2
    
    def __init__(self,
        name='Bmo',
        level=0,
        max_hp=2,
        max_ap=0,
        is_dead=False,
        ):

        self.name = name
        self.level = level
        self.is_dead = is_dead
        
        self.stats = {
            'STR': 0,
            'AGI': 0,
            'INT': 0,
            'CHA': 0,
            'LCK': 0,
            'max_hp': 0,
            'max_ap': 0
            }

        self.growth = {
            'STR': 2,
            'AGI': 1,
            'INT': 2,
            'CHA': 1,
            'LCK': 1,
            'max_hp': 3,
            'max_ap': 2
            }

        self.hp = self.stats['max_hp']
        self.ap = self.stats['max_ap']