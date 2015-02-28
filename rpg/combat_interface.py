"""
    This is the GUI for selecting and displaying hero combat comands.
    This module should never be called direclty and always be imported.
"""

import combat_functions as CF
import subprocess
from config import *


# The main interface call
def interface(hero, monsters):
    commands = [
        'Attack',
        'Spell',
        'Defend',
        'Item',
        'Run'
        ]

    
    if CONSOLE:
        enum_commands = print_commands(commands)
        player_command = accept_command(enum_commands)
        
        if player_command == 'Attack':
            target = target_monster(monsters)
            damage = hero.attack(target)
            print '\n%s attacks %s for %d damage!' % (hero.name, target.name, damage)
            if target.is_dead:
                print '\n%s has been killed!' % target.name
        
        # elif player_command == 'Spell':
        elif player_command == 'Defend':
            hero.is_defending = True
            print '\n%s is defending!' % hero.name
        # elif player_command == 'Item':
        # elif player_command == 'Run':


# Prints available commands and returns an enumerated list
def print_commands(commands):

        commands = zip(
            range(
                1,
                len(commands)+1,
                ),
            commands
            )
        for c in commands:
            print c[0], c[1]

        return commands


# Returns the chosen command as a string
def accept_command(c_enum):
    
    # creates a list of indices
    indices = []
    for i in c_enum:
        indices.append(i[0])


    # Takes user import and converts to integer
    choice = ''
    while(choice not in indices):
        choice = raw_input('Choose your command(#): ')
        
        try: 
            choice = int(choice)
        
        except Exception as e:
            # print e
            pass

    # print 'You chose: %s ' % c_enum[choice-1][1]
    
    return c_enum[choice-1][1]


# Takes a list of monsters, returns one that is targeted
def target_monster(monsters):
    live_monsters = []
    
    # adds living monsters to the list
    for m in monsters:
        if m.is_dead:
            continue
        else:
            live_monsters.append(m)
    
    # enumerates the monsters by way of zip()
    live_monsters = zip(
        range(
            1, 
            len(live_monsters)+1),
        live_monsters
        )
    print ''
    for monster in live_monsters:
        print monster[0], ':', monster[1]
    
    choice = ''
    choices = {str(x) for x in range(1, len(live_monsters)+1)}
    
    while(choice not in choices):
        choice = raw_input('Select target: ')
    choice = int(choice)
    
    return live_monsters[choice-1][1]
        

# Clears the screen        
def cls():
    subprocess.call("cls", shell=True)


# Prints out member stats
# Accepts a list of  members
def print_stats(members):
    print ' | '.join(('{: >10}'.format(m.name) for m in members))
    print ' | '.join(('{: >10}'.format('HP ' + str(m.hp) + '/' + str(m.stats['max_hp'])) for m in members))
    print ' | '.join(('{: >10}'.format('AP ' + str(m.ap) + '/' + str(m.stats['max_ap'])) for m in members))
