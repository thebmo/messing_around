from npc import NPC
from random import randrange


class Monster(NPC):
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

    # monster spells stored in a dict per class
    # spells: { 'name': rank }
    # monster spells are class variables
    spells = {
        'Fire': 0,
        'Ice': 0,
        'Heal': 0,
        }
        
    # monster elemental strengths / weakness
    halv = []
    null = []
    absb = []
    weak = []

    def __init__(
        self,
        is_dead=False,
        is_defending=False,
        has_fled=False
        ):

        self.name = self.NAME
        self.stats = self.STATS
        self.is_dead = is_dead
        self.is_defending = is_defending
        self.has_fled = has_fled
        self.hp = self.stats['max_hp']
        self.ap = self.stats['max_ap']
        
        self.HALV = self.halv
        self.NULL = self.null
        self.ABSB = self.absb
        self.WEAK = self.weak



    def __str__(self):
        return self.name


    def __ref__(self):
        return self.name

            
    # chooses target from list of targets
    # returns live target's index
    def choose_target(self, targets):
        targeting = True
        while(targeting):
            r = randrange(0, 100)
            t = (r / 25 )

            if not targets[t].is_dead:
                return targets[t]
