"""
    Party class that contains a list of all heroes
    in the party as well as gold amount, items, and
    Global Event Flags.
"""

class Party(object):
    
    def __init__(self, heroes, gold=0, items=[]):
        
        if type(heroes) != list:
            raise Exception('Heroes not in list form')
            
        self.heroes = heroes
        self.gold = gold
        self.items = items


    # Prints stats for entire party
    def print_stats(self):
        for h in self.heroes:
            h.print_stats()


    # Heals party to full HP/AP
    def heal_party(self):
        for h in self.heroes:
            h.hp = h.stats['max_hp']
            h.ap = h.stats['max_ap']


    # Levels up the entire party by 1
    def level_up(self):
        for h in self.heroes:
            h.level_up