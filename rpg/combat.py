from combat_functions import *
from config import *                  # for global settings
# from random import randrange, choice

# main call to initiate combat.
# party: a list of hero party objects
# console: param to dictate if in a console window
def start_combat(party, console=CONSOLE):
    
    # initializes combat variables
    in_combat = True
    monsters = random_encounter(console=console)
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

                # total exp gains grants to live party
                exp = get_exp(monsters)
                for p in party:
                    if not p.is_dead:
                        p.EXP += exp
                        while(p.leveled()):
                            p.level_up()
                            if console:
                                print '\n%s has leveled up' % p.name
                                p.print_stats()
                break

            # skips dead member's combat turn
            elif member.is_dead:
                print '%s is dead!' % member.name
                continue

            # check for available commands
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
            
            # end combat command check


        # test block to end combat
        if TESTING:
            for m in monsters:
                m.is_dead = True
            print '\nend combat testing'
        # end test block
