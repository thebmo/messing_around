# from collections import OrderedDict
from exp import exp_to_next_level

# Basic Hero Class Object
class Hero(object):
    
    # A chart of required xp to reach next level as list.
    # Uses index as current level
    # ex: Level 1 hero
    #   exp_to_next_level[self.level]
    exp_to_next_level = exp_to_next_level
    
    # stats, stat growth, and stat mods

    
    CLASS = 'Hero'
    
    STR_MOD = 1
    AGI_MOD = 1
    INT_MOD = 1
    
    EXP = 0    
    # end stats, stat growth, and stat mods

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

    # initializes the hero
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
        
        self.growth = {
            'STR': 0,
            'AGI': 0,
            'INT': 0,
            'CHA': 0,
            'LCK': 0,
            'max_hp': 0,
            'max_ap': 0
            }

        self.stats = {
            'STR': 0,
            'AGI': 0,
            'INT': 0,
            'CHA': 0,
            'LCK': 0,
            'max_hp': 0,
            'max_ap': 0
            }

        self.hp = self.stats['max_hp']
        self.ap = self.stats['max_ap']
        
        # # if no level is selected, this generates level 1
        # if self.level == 0:
            # self.level_up()

        # # levels up hero to designated level
        # else:
            # for i in range(0, level):
                # self.level_up()
            # self.level-=level


    # cleanly prints stats
    def print_stats(self):
        print "\nNAME : %s" % self.name
        print "LEVEL: %s" % self.level
        print "CLASS: %s" % self.CLASS
        for k, v in sorted(self.stats.iteritems()):
            print "%s: %s" % (k, v)
        print 'EXP   : %s' % self.EXP
        print 'NEEDED: %s' % self.exp_to_next_level[self.level]


    # raw damage calculations
    def deal_damage(self):
        return self.stats['STR'] + int((.5 * self.AGI_MOD) * self.stats['AGI'])


    # takes raw damage and applies modifiers, then
    # subtracts from hero's hp
    def take_damage(self, raw_damage):
        damage = raw_damage - int(.5 * self.stats['AGI'])
        
        if damage > 1:
            self.hp -= damage
            self.check_for_death()


    # checks if hero is dead and makes adjustments
    def check_for_death(self):
        if self.hp <=0:
            self.is_dead = True
            self.hp = 0
            

    # def cast_spell(self, spell):
        