from collections import OrderedDict


# Basic Hero Class Object
class Hero(object):
    
    stats = {
        'STR': 0,
        'AGI': 0,
        'INT': 0,
        'CHA': 0,
        'LCK': 0,
        'max_hp': 0,
        'max_ap': 0
        }


    # when the hero levels up
    def level_up(self):
        self.level += 1
        self.stats['STR'] += 2
        self.stats['AGI'] += 1
        self.stats['INT'] += 1
        self.stats['CHA'] += 1
        self.stats['LCK'] += 1
        self.stats['max_hp'] += 3
        self.stats['max_ap'] += 2


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
        print "LEVEL: %s" % self.level
        for k, v in sorted(self.stats.iteritems()):
            print "%s: %s" % (k, v)