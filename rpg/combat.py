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
    monsters = random_encounter()
    initiative = determine_initiative(party, monsters)
    # end combat initialization
    
    



# determines which monsters attack the party
def random_encounter():
    
    # this will bey dynamically extended
    monster_pool = ['Slime', 'Imp']
    m_count = randrange(MAX_MONSTERS)+1
    monsters = []
    
    # chooses monsters from the monster pool
    for i in range(m_count):
        monsters.append(choice(monster_pool))
        
    monsters = fetch_monsters(monsters)
    
    print'%s monster%s appear%s!' % (m_count, 's'[m_count==1:], 's'[m_count!=1:])
    for monster in monsters:
        print '%s: %s' % (monster.name, monster.hp)

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


# def combat_round(party, monsters, initiative):
# def combat_round(party_monsters_initiative_dict):

def determine_initiative(party, monsters):
    
    # a list of tuples (p/m, index, roll)
    initiatives = []
    
    for i, p in enumerate(party):
        # r = ad20 plus agility
        r = randrange(0,20)+1 + p.stats['AGI']
        initiatives.append(('p', i, r))
    
    for i, m in enumerate(monsters):
        r = randrange(0,20)+1
        initiatives.append(('m', i, r))
    
    # sorts initiative by roll value
    initiatives = sorted(initiatives, key=lambda x: x[2], reverse=True)
    
    return initiatives
    
    # print 'INITIATIVE ORDER'
    # print '================'
    # for i in initiatives:
        # print i


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

def main():
    random_encounter()


if __name__ == '__main__':
    main()
