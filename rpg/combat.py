from combat_functions import *
from random import randrange, choice

# MAX_MONSTERS = 4

# create monsters
# determine action order based on agi
# issue commands
# repeat

# starts combat
def start_combat(party):
    
    # initializes combat variables
    in_combat = True
    monsters = random_encounter(console=True)
    initiatives = determine_initiative(party, monsters)
    # end combat initialization

    # pseudo code below for basic combat logic
    # monster/party death checks should be done in between
    # combat action. combat should end if party has fallen
    # or all monsters have been defeated
    while (in_combat):
        for initiative in initiatives:
            # sets member to the active character
            member = get_member(initiative, party, monsters)
            
            if party_is_dead(party):
                print 'The party has been defeated.'
                in_combat = False
                break
            
            elif monsters_are_dead(monsters):
                print 'The party is victorious'
                in_combat = False
                
                # total exp gains
                # for p in party:
                    # if not p is_dead:
                        # give xp
                        # check for level up

            # skips dead member's combat turn
            elif member.is_dead:
                print '%s is dead!' % member.name
                continue
            
            
            # check for available options
            else:
                print '%s\'s turn' % member.name
                if member in party:
                    print 'this is where you choose your command'
                else:
                    print '%s attacks!' % member.name
                # attack
                # if member in party (not monsters)
                    # defend
                # spells
                    # go throw hero spells
                        # if rank >0: list spell
                # if member in party (not monsters)
                    # items
                        # check for items owned by party


        print '1 round of combat end'
        in_combat = False
