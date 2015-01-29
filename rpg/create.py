from config import *
from heroes.party import Party


# returns a single hero class object
def create_hero():

    # main loop
    while(True):
        character_class = ''
        name = ''

        # asks for name input and varivies name < 8 Chars
        while(len(name) <1 or len(name) > 8) or ' ' in name:
            name =raw_input('Enter the hero\'s name (8 or less characters): ')

        # asks for class number and makes sure is valid choice
        while(character_class not in ['1','2','3','4']):
            print '\nPlease choose a class by number for %s:' % name
            print '1 - Fighter\n2 - Rogue\n3 - Cleric\n4 - Wizard'
            character_class = raw_input('Choose which class for %s?: ' % name) 

        # creates an instance of the desired hero class
        if character_class == '1':
            from heroes.fighter import Fighter
            hero = Fighter(name=name)
        elif character_class == '2':
            from heroes.rogue import Rogue
            hero = Rogue(name=name)
        elif character_class == '3':
            from heroes.cleric import Cleric
            hero = Cleric(name=name)
        elif character_class == '4':
            from heroes.wizard import Wizard
            hero = Wizard(name=name)
        else:
            hero = ''
            print 'uknown error'
            break
        
        hero.level_up()
        
        return hero


# creates/returns a list of hero class objects (max 4)
def create_party():
    creating = True
    party = []

    print '\nplease create your party (max members= %s)' % MAX_PARTY
    
    while(creating):
        
        party.append(create_hero())

        add_more = ' '
        while(add_more[0] != 'y' and add_more[0] != 'n' and len(party) < MAX_PARTY):
            add_more = raw_input('Add more party members (4 max)? (y/n)').lower()
        if add_more[0] == 'y':
            print '\n'
            continue
        else:
            creating = False

            for p in party:
                p.print_stats()

        return Party(party)


# this is for testing purposes
def main():
    party = create_party()
    
    print '\n**************\nafter level up\n**************'
    for p in party:
        p.level_up()
        p.print_stats()


if __name__ == '__main__':
    main()