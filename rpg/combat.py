# import sys               # for the str to class call
from random import randrange, choice
from monsters import *

MAX_MONSTERS = 4

# create monsters
# determine action order based on agi
# issue commands
# repeat

# starts combat
def start_combat(party):
    
    # initializes combat variables
    in_combat = True
    monsters = random_encounter(console=True)
    initiative = determine_initiative(party, monsters)
    # end combat initialization

    # pseudo code below for basic combat logic
    # monster/party death checks should be done in between
    # combat action. combat should end if party has fallen
    # or all monsters have been defeated
    # while still in combat
        # for loop through initiatives
            # if member is dead:
                # continue
            
            # check for available options
                # attack
                # defend
                # spells
                    # go throw hero spells
                        # if rank >0: list spell
                # if member in party (not monsters)
                    # items
                        # check for items owned by party
        
        # if any monsters still aliveL
            # if monsters_are_dead(monsters):
                # in_combat = False
            # continue combat
        # else:
            # total exp gains
            # for member in party:
                # if not member is_dead:
                    # give xp
    # end pseudo code for combat logic


# determines which monsters attack the party
def random_encounter(console=False):
    
    # this will bey dynamically extended
    monster_pool = ['Slime', 'Imp']
    m_count = randrange(MAX_MONSTERS)+1
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
def determine_initiative(party, monsters, testing=False):
    
    # a list of tuples (p/m, index, roll)
    initiatives = []
    
    for i, p in enumerate(party):
        # r = 1d20 plus agility
        r = randrange(0,20)+1 + p.stats['AGI']
        initiatives.append(('p', i, r))
    
    for i, m in enumerate(monsters):
        r = randrange(0,20)+1 + m.stats['AGI']
        initiatives.append(('m', i, r))
    
    # sorts initiative by roll value
    initiatives = sorted(initiatives, key=lambda x: x[2], reverse=True)
    
    if testing:
        print 'INITIATIVE ORDER'
        print '================'
        for i in initiatives:
            print i

    return initiatives


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


# returns the amount of EXP for each party member
def get_exp(monsters):
    exp = 0
    
    for m in monsters:
        exp += m.stats['exp']

    return exp
    
    
# main call for boilerplate code
def main():
    random_encounter()


if __name__ == '__main__':
    main()
