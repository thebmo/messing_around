from random import randrange


class Monster(object):
    """
        basic moster class
    """
    NAME = 'Monster'
    
    STATS = {
        'STR': 0,
        'AGI': 0,
        'INT': 0,
        'CHA': 0,
        'LCK': 0,
        'max_hp': 0,
        'max_ap': 0,
        'damage': 0,
        'level': 0,
        'exp': 0,
        }

    def __init__(
        self,
        is_dead=False,
        ):

        self.name = self.NAME
        self.stats = self.STATS
        self.is_dead = is_dead
        
        self.hp = self.stats['max_hp']
        self.ap = self.stats['max_ap']



    def __str__(self):
        return self.name


    def __ref__(self):
        return self.name


    def take_damage(self, taken_damage):
        self.hp -= taken_damage
        if self.hp < 1:
            self.is_dead = True


    # checks if hero is dead and makes adjustments
    def check_for_death(self):
        if self.hp <=0:
            self.is_dead = True
            self.hp = 0

            
    # chooses target from list of targets
    # returns live target's index
    def choose_target(self, targets):
        targeting = True
        while(targeting):
            r = randrange(0, 100)
            t = (r / 25 )

            if not targets[t].is_dead:
                return t
        
            
            
    # deals damage
    def deal_damage(self):
        return self.damage
        