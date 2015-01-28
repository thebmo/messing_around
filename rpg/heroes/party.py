class Party(object):
    
    def __init__(self, heroes, gold=0, items=[]):
        
        if type(heroes) != list:
            raise Exception('Heroes not in list form')
            
        self.members = heroes
        self.gold = gold
        self.items = items
        
    