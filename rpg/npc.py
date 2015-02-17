'''
    this is a base clase for the monster and hero
    subclasses. all generic methods should be made
    in this class only.
'''

class NPC(object):
    
    # initializes the NPC
    def __init__(self,
        name='',
        max_hp=0,
        max_ap=0,
        is_dead=False,
        ):

        self.name = name
        self.is_dead = is_dead
        self.is_defending = False
        
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
        self.spells = self.class_spells
                
        # hero elemental strengths / weakness
        self.HALV = []
        self.NULL = []
        self.ABSB = []
        self.WEAK = []
        
    

    '''
        DAMAGE/DEFENSE BLOCK:
            this block handles basic damage components such as
            basic attacks, taking damage, defending against
            damage
    '''


    # basic attack damage calculation
    # returns the modified damage value
    def attack(self, target):
        damage = self.stats['STR'] + int((.5 * self.AGI_MOD) * self.stats['AGI'])
        
        return target.take_damage(damage)


    # takes raw damage and applies modifiers, then
    # subtracts from hero's hp
    # returns the modified damage
    def take_damage(self, raw_damage):
        dam_mod = 1
        
        if self.is_defending:
            dam_mod = 2
        
        damage = ((raw_damage - int(.5 * self.stats['AGI'])) / dam_mod)
        
        if damage > 1:
            self.hp -= damage
            self.check_for_death()
        
        return damage


    # checks if hero is dead and makes adjustments
    def check_for_death(self):
        if self.hp <=0:
            self.is_dead = True
            self.hp = 0


    # the defend command, sets defending BOOL to true for use
    # in the take damage method
    def defend(self):
        self.is_defending = True


# END DAMAGE/DEFENSE BLOCK
    
    
    # def cast_spell(self, spell):
    
    # order of checking should be
    # absorbed -> nulled -> halved -> weak
    
    
    # returns True if hero has any spalls lvl 1 or higher
    def has_spells(self):
        for k in self.spells:
            if self.spells[k] > 0:
                return True
        return False


    # checks for elemental weaknes
    def is_weak(self, element):
        if element in self.WEAK:
            return True
        else:
            return False

    # checks for elemental halved
    def is_halv(self, element):
        if element in self.HALV:
            return True
        else:
            return False
            
    # checks for elemental nullified   
    def is_null(self, element):
        if element in self.NULL:
            return True
        else:
            return False
            
    # checks for elemental absorbed
    def is_absb(self, element):
        if element in self.ABSB:
            return True
        else:
            return False
