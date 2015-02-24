"""
    This is the GUI for selecting and displaying hero combat comands.
    This module should never be called direclty and always be imported.
"""

import combat_functions as CF
from config import *


# def interface(hero, mosnters):
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
            print '%s attacks %s for %d damage!' % (hero.name, target.name, damage)
            if target.is_dead:
                print '%s has been killed!' % target.name 


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
            print e

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
    for monster in live_monsters:
        print monster[0], ':', monster[1]
    
    choice = ''
    choices = {str(x) for x in range(1, len(live_monsters)+1)}
    
    while(choice not in choices):
        choice = raw_input('Select target: ')
    choice = int(choice)
    
    return live_monsters[choice-1][1]
        
        
# this is the logic to actually execute the issued command
# def execute_command(hero, target, command):