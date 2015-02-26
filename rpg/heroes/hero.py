"""
    This is the hero base class, the parent for all hero
    sub-classes.
"""

from exp import exp_to_next_level
from npc import NPC
from random import randrange as rand

# Basic Hero Class Object
class Hero(NPC):
    
    # A chart of required xp to reach next level as list.
    # Uses index as current level
    # ex: Level 1 hero
    #   exp_to_next_level[self.level]
    exp_to_next_level = exp_to_next_level
    
    # stats, spells, stat growth, and stat mods

    
    CLASS = 'Hero'
    
    STR_MOD = 1
    AGI_MOD = 1
    INT_MOD = 1
    
    growth = {
        'STR': 0,
        'AGI': 0,
        'INT': 0,
        'CHA': 0,
        'LCK': 0,
        'max_hp': 0,
        'max_ap': 0
    }
    
    # class spells stored in a dict per class
    # spells: { 'name': rank }
    class_spells = {
        'Fire': 0,
        'Ice': 0,
        'Heal': 0,
        }

    # end stats, spells, stat growth, and stat mods


    # when the hero levels up
    def level_up(self):
        self.level += 1
        self.stats['STR'] += self.growth['STR']
        self.stats['AGI'] += self.growth['AGI']
        self.stats['INT'] += self.growth['INT']
        self.stats['CHA'] += self.growth['CHA']
        self.stats['LCK'] += self.growth['LCK']
        self.stats['max_hp'] += self.growth['max_hp']
        self.stats['max_ap'] += self.growth['max_ap']
        self.hp += self.growth['max_hp']
        self.ap += self.growth['max_ap']  


    # checker to see if leveled after combat
    def leveled(self):
        if self.EXP > self.exp_to_next_level[self.level]:
            return True
        
        return False


    # initializes the hero
    def __init__(self,
        name='Bmo',
        level=0,
        max_hp=3,
        max_ap=0,
        is_dead=False,
        ):

        self.name = name
        self.level = level
        self.is_dead = is_dead
        self.is_defending = False
        
        self.stats = {
            'STR': 0,
            'AGI': 0,
            'INT': 0,
            'CHA': 0,
            'LCK': 0,
            'max_hp': 5,
            'max_ap': 0
            }

        self.hp = self.stats['max_hp']
        self.ap = self.stats['max_ap']
        self.spells = self.class_spells
                
        # hero elemental strengths / weakness
        self.HALV = []
        self.NULL = []
        self.ABSB = []
        self.WEAK = []
        
        self.EXP = 0


    # cleanly prints stats
    def print_stats(self):
        print "\nNAME : %s" % self.name
        print "LEVEL: %s" % self.level
        print "CLASS: %s" % self.CLASS
        print 'STR: %s' % self.stats['STR']
        print 'AGI: %s' % self.stats['AGI']
        print 'INT: %s' % self.stats['INT']
        print 'CHA: %s' % self.stats['CHA']
        print 'LCK: %s' % self.stats['LCK']
        print 'HP : %s/%s' % (self.hp, self.stats['max_hp'])
        print 'AP : %s/%s' % (self.ap, self.stats['max_ap'])
        print 'EXP   : %s' % self.EXP
        if self.level < 99:
            print 'NEEDED: %s' % self.exp_to_next_level[self.level]


    # calculates if party can run from hero's
    # run value
    def run(self):
        roll = rand(100)+1
        rv = roll + (self.level * self.AGI_MOD)

        if rv > 80:
            return True
        return False
