"""
    Helper methods for the combat.py module. This file
    should only be imported and never called directly.
"""
from config import *                              # for global settings
from monsters import *
from monsters.__init__ import __all__ as MONSTERS # for monster pool
from random import randrange, choice


# determines which monsters attack the party
def random_encounter(console=False, max_monsters=4):
    
    # this will be dynamically extended
    monster_pool = [''.join((m[0].upper(), m[1:])) for m in MONSTERS]
    m_count = randrange(max_monsters)+1
    monsters = []
    
    # chooses monsters from the monster pool
    for i in range(m_count):
        monsters.append(choice(monster_pool))
        
    monsters = fetch_monsters(monsters)
    
    if console:
        print'%s monster%s appear%s!' % (m_count, 's'[m_count==1:], 's'[m_count!=1:])
        for monster in monsters:
            print '%s: %s' % (monster.NAME, monster.hp)

    return monsters


# takes a list of monsters as string and returns a list of monster
# objects
def fetch_monsters(monsters):
    monster_objects = []
    
    for monster in monsters:
        # forms the class string ex: slime.Slime
        mstring = monster.lower() + '.' + monster
        
        m_class = eval(mstring)
        m = m_class()
        monster_objects.append(m)
    
    return monster_objects


# calculates and returns a list of tuples containing
# sorted monster and party initiatives
# Ex:
#   (party or monster, object list index, initiative roll)
#   ('p' or 'm', 0-9, 15)
def determine_initiative(party, monsters, testing=TESTING):
    
    # a list of tuples (p/m, index, roll)
    initiatives = []
    
    for i, p in enumerate(party):
        # r = 1d20 plus agility
        r = randrange(0,20)+1 + p.stats['AGI']
        initiatives.append(('p', i, r))
    
    for i, m in enumerate(monsters):
        r = randrange(0,20)+1 + m.stats['AGI']
        initiatives.append(('m', i, r))
    
    # sorts initiative by highest roll value
    initiatives = sorted(initiatives, key=lambda x: x[2], reverse=True)
    
    if testing:
        print '\nINITIATIVE ORDER'
        print '================'
        for i in initiatives:
            print i

    return initiatives


# converts the initiative member to
# its proper party or monster object
def get_member(member, party, monsters):
    if member[0] == 'p':
        return party[member[1]]
    return monsters[member[1]]


# checks if any monsters are alive
# returns True if all dead : Else False
def monsters_are_dead(monsters):
    all_dead = False
    
    for m in monsters:
        if not m.is_dead:
            all_dead = False
            break
        else:
            all_dead = True
            
    return all_dead

    
# verifies if all party members dead
# returns True if all dead : Else False
def party_is_dead(party):
    all_dead = False
    
    for p in party:
        if not p.is_dead:
            all_dead = False
            break
        else:
            all_dead = True
            
    return all_dead


# returns the total amount of EXP from monsters
# for each party member
def get_exp(monsters):
    exp = 0
    
    for m in monsters:
        exp += m.stats['exp']

    return exp

    
# returns the total amount of EXP from monsters
# for each party member
def get_gold(monsters):
    gold = 0
    
    for m in monsters:
        gold += m.stats['gold']

    return gold


# calcs if preemptive fight or not
# returns:
#   0 - no premptive fight
#   1 - party goes first
#   2 - monsters go first
def pre_emptive():
    fight = 0
    
    # party goes first
    r = randrange(100)
    if r > 79:
        fight += 1
    
    # monsters go first
    elif r < 20:
        fight +=2
    
    return fight


# Returns the average level of a list of objects    
def avg_level(party):
    avg = sum([p.level for p in party]) / (len(party))
    return avg


# main call for boilerplate code
def main():
    random_encounter()


if __name__ == '__main__':
    main()
