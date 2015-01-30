"""
    Master combat logic module. This contains all the basic
    logic flow for combat. 
    MODULES:
        combat_functions: handles all the helper functions
        combat_interface: this is the GUI for selecting
            and displaying hero combat comands
        config: this module works as a settings file. It
            contains globals that are used as kwargs
"""

import combat_functions as CF
import combat_interface as CI
from config import *                  # for global settings
# from random import randrange, choice

# main call to initiate combat.
# Party: party object (contains a list of hero objects)
# console: param to dictate if in a console window
def start_combat(Party, console=CONSOLE):
    
    # converts the party object list into a local copy
    party = Party.heroes
    
    # initializes combat variables
    in_combat = True
    monsters = CF.random_encounter(console=console)
    initiatives = CF.determine_initiative(party, monsters)
    # end combat initialization

    # pseudo code below for basic combat logic
    # monster/party death checks should be done in between
    # combat action. combat should end if party has fallen
    # or all monsters have been defeated

    # pre-emptive fight type
    pre_emp = CF.pre_emptive()
    
    if TESTING and pre_emp:
        print '\nPRE-EMPTIVE BATTLE!\n'

    # START ROUND LOOP
    while (in_combat):
    
    # # MAKE A COMMAND LIST HERE
    # commands = [
        # party_index,
        # command,
        # target
        # ]
    
        # START TURN LOOP
        for initiative in initiatives:
            
            # skips monster turn if pre-emptive
            if pre_emp == 1 and initiative[0] == 'm':
                    print 'monster skipped'
                    continue
            
            # skips hero turn if pre-emptive
            elif pre_emp == 2 and initiative[0] == 'p':
                    print 'hero skipped'
                    continue
            
            # sets member to the active character
            member = CF.get_member(initiative, party, monsters)
            
            if CF.party_is_dead(party):
                print 'The party has been defeated.'
                in_combat = False
                break
            
            # ends combat if all monsters are dead
            elif CF.monsters_are_dead(monsters):
                print 'The party is victorious!'
                in_combat = False

                # total exp gains grants to live party
                exp = CF.get_exp(monsters)
                gold = CF.get_gold(monsters)
                print 'The Party gains %s EXP and %s GOLD' % (exp, gold)
                for p in party:
                    if not p.is_dead:
                        p.EXP += exp
                        while(p.leveled()):
                            p.level_up()
                            if console:
                                print '\n%s has leveled up' % p.name
                                p.print_stats()
                
                # this breaks the turn for-loop
                break

            # skips dead member's combat turn
            elif member.is_dead:
                print '%s is dead!' % member.name
                continue

            # check for available commands
            else:
                print '%s\'s turn' % member.name
                
                # PARTY LOGIC
                if member in party:
                    CI.interface(party, monsters)
                
                # MONSTER LOGIC
                else:
                    target = member.choose_target(party)
                    print '%s attacks %s!' % (member.name, target.name)
            
            
            # END TURN FOR-LOOP


        # test block to end combat
        if TESTING:
            for m in monsters:
                m.is_dead = True
            print '\nend combat testing'
        # end test block
    
        # clears pre-emptive status
        pre_emp = 0
    
    # END ROUND WHILE-LOOP