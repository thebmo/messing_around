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
from config import *          # for global settings


# Main call to initiate combat.
# Party: party object (contains a list of hero objects)
# console: param to dictate if in a console window
def start_combat(Party, console=CONSOLE, monster_list=[], count=0):
    
    # converts the party object list into a local copy
    party = Party.heroes
    
    # initializes combat variables
    in_combat = True
    monsters = CF.random_encounter(console=console, monster_pool=monster_list, m_count=count)
    initiatives = CF.determine_initiative(party, monsters)
    # end combat initialization

    # pseudo code below for basic combat logic
    # monster/party death checks should be done in between
    # combat action. combat should end if party has fallen
    # or all monsters have been defeated

    # pre-emptive fight type
    pre_emp = CF.pre_emptive()
    
    if console and pre_emp:
        print '\nPRE-EMPTIVE BATTLE!'

    # START ROUND LOOP
    while (in_combat):
    
        # START TURN LOOP
        for initiative in initiatives:
            CI.cls()
            CI.print_stats(party)
            print ''
            CI.print_stats(monsters)
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
                print '\nThe party has been defeated.'
                in_combat = False
                break
            
            # ends combat if all monsters are dead
            elif CF.monsters_are_dead(monsters):
                print '\nThe party is victorious!'
                in_combat = False

                # total exp gains grants to live party
                exp = CF.get_exp(monsters)
                gold = CF.get_gold(monsters)
                print 'The Party gains %s EXP and %s GOLD' % (exp, gold)
                Party.gold += gold
                
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
                print '\n%s\'s turn' % member.name
                
                # PARTY LOGIC
                if member in party:
                    
                    # Clears the defending flag
                    member.is_defending = False
                    
                    CI.interface(member, monsters)
                
                # MONSTER LOGIC
                else:
                    
                    if CF.avg_level(party) - member.stats['level'] >= 5:
                        member.has_fled = True
                        print '%s flees!' % member.name
                    
                    else:
                        target = member.choose_target(party)
                        damage = member.attack(target)
                        print '\n%s attacks %s for %d damage!' % (member.name, target.name, damage)
                        if target.is_dead:
                            print '%s has been killed!' % target.name                        
            
            raw_input('\npress ENTER')
            # END TURN FOR-LOOP
            
        


        # test block to end combat inside while loop
        if TESTING:
            for m in monsters:
                m.is_dead = True
        # end test block
    
        # clears pre-emptive status
        pre_emp = 0

    # END ROUND WHILE-LOOP
    
    if TESTING: print '\nEnd combat testing'
