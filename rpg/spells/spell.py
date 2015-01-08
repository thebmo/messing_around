
class Spell(object):
    ELEMENTS = {
        'EARTH': 0,
        'WIND' : 1, 
        'ICE'  : 2,
        'FIRE' : 3,
        'LIGHT': 4,
        'DARK' : 5,
        'PHYS' : 6,
        }
    WEAK = [
        [0, 2, 1, 1, 1, 1, 1],
        [2, 0, 1, 1, 1, 1, 1],
        [1, 1, 0, 2, 1, 1, 1],
        [1, 1, 2, 0, 1, 1, 1],
        [1, 1, 1, 1, 0, 2, 1],
        [1, 1, 1, 1, 2, 0, 1],
        [1, 1, 1, 1, 1, 1, 1],
        ]
        
    def __init__(self, name, element, damage, ELEMENTS=ELEMENTS):
        self.name = name
        self.element = element
        self.damage = damage

    
    # returns the weakness modifier
    # ATK is attacking spell
    # DEF is defending spell type: default = 'PHYS'
    def check_weakness(self, DEF='PHYS', W=WEAK, E=ELEMENTS):
        ATK = self.element
        return W[E[ATK]][E[DEF]]

    # casts spell on target
    def cast_spell(self, target):
        spell_mod = self.check_weakness()
        target.take_damage(spell_mod * self.damage)