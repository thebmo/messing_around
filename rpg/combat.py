# import sys               # for the str to class call
from random import randrange, choice
from monsters import *

MAX_MONSTERS = 4

# create monsters
# determine action order based on agi
# issue commands
# repeat
def random_encounter():
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

# converts the string to an object
# def str_to_class(str):
    # return reduce(getattr, str.split("."), sys.modules[__name__])


# def combat_round(party, monsters, initiative):
# def combat_round(party_monsters_initiative_dict):
    
def main():
    random_encounter()


if __name__ == '__main__':
    main()
