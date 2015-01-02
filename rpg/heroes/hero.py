# from collections import OrderedDict


# Basic Hero Class Object
class Hero(object):
    
    # stats, stat growth, and stat mods
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
        'STR': 0,
        'AGI': 0,
        'INT': 0,
        'CHA': 0,
        'LCK': 0,
        'max_hp': 0,
        'max_ap': 0
        }
    
    CLASS = 'Hero'
    
    STR_MOD = 1
    AGI_MOD = 1
    INT_MOD = 1
    
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
        self.stats['max_hp'] = max_hp
        self.stats['max_ap'] = max_ap
        self.hp = max_hp
        self.ap = max_ap
        self.is_dead = is_dead

        # if no level is selected, this generates level 1
        if self.level == 0:
            self.level_up()

        # levels up hero to designated level
        else:
            for i in range(0, level):
                self.level_up()
            self.level-=level


    # cleanly prints stats
    def print_stats(self):
        print "NAME : %s" % self.name
        print "LEVEL: %s" % self.level
        for k, v in sorted(self.stats.iteritems()):
            print "%s: %s" % (k, v)


    # raw damage calculations
    def deal_damage(self):
        return self.stats['STR'] + int((.5 * self.AGI_MOD) * self.stats['AGI'])

        
    def take_damage(self, raw_damage):
        damage = raw_damage - int(.5 * self.stats['AGI'])
        return damage if damage >=0 else 0