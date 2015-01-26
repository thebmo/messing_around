import combat_functions as CF
from config import *


# def interface(hero, mosnters):
def interface(party, monsters):
    commands = [
        'Attack',
        'Spell',
        'Defend',
        'Item',
        'Run'
        ]

    
    if CONSOLE:
        enum_commands = print_commands(commands)
        accept_command(enum_commands)
        target_monster(monsters)


# prints available commands and returns an enumerated list
def print_commands(commands):
        # c_enum = []
        # for i, c in enumerate(commands):
            # print i+1, c
            # c_enum.append((str(i+1), c))
        commands = zip(
            range(
                1,
                len(commands)+1,
                ),
            commands
            )
        for c in commands:
            print c[0], c[1]
        # return c_enum
        return commands


# returns the chosen command as a string
def accept_command(c_enum):
    
    # creates a list of indices
    indices = []
    for i in c_enum:
        indices.append(i[0])


    # takes user import and converts to integer
    choice = ''
    while(choice not in indices):
        choice = raw_input('Choose your command(#): ')
        
        try: 
            choice = int(choice)
        
        except:
            pass

    # print 'You chose: %s ' % c_enum[choice][1]
    
    return c_enum[choice][1]


# takes a list of monsters, returns one that is targeted
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

        
# this is the logic to actually execute the issued command
# def execute_command(hero, target, command):