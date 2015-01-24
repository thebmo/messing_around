import combat_functions as CF
from config import *


# def interface(hero, mosnters):
def interface():
    commands = [
        'Attack',
        'Spells',
        'Defend',
        'Item'
        ]

    
    if CONSOLE:
        c_enum = print_commands(commands)
        accept_command(c_enum)
        
        


# prints available commands and returns an enumerated list
def print_commands(commands):
        c_enum = []
        for i, c in enumerate(commands):
            print i+1, c
            c_enum.append((str(i+1), c))

        return c_enum


# this is  kludgey
# returns the chosen command
def accept_command(c_enum):
    
    # creates a list of indices
    indices = []
    for i in c_enum:
        indices.append(i[0])

    choice = ''
    while(choice not in indices):
        choice = raw_input('Choose your command(#): ')
    
    choice = int(choice)-1
    print 'You chose: %s ' % c_enum[choice][1]
    
    return c_enum