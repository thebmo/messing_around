def create():
    creating = True
    party = []
    while(creating):
        character_class = ''
        name = ''
        while(len(name) <1 or len(name) > 8):
            name =raw_input('Please enter hero name (8 or less characters):')
        
        while(character_class not in ['1','2','3','4']):
            print '\nPlease choose a class by number for %s:' % name
            print '1 - Fighter\n2 - Rogue\n3 - Cleric\n4 - Wizard'
            character_class = raw_input('Choose which class for %s?: ' % name) 

        if character_class == '1':
            from heroes.fighter import Fighter
            party.append(Fighter(name=name))
        elif character_class == '2':
            from heroes.rogue import Rogue
            party.append(Rogue(name=name))
        elif character_class == '3':
            from heroes.cleric import Cleric
            party.append(Cleric(name=name))
        elif character_class == '4':
            from heroes.wizard import Wizard
            party.append(Wizard(name=name))
        else:
            print 'uknown error'
            break
        
        add_more = ' '
        while(add_more[0] != 'y' and add_more[0] != 'n' and len(party) < 4):
            add_more = raw_input('Add more party members (4 max)? (y/n)').lower()
        if add_more[0] == 'y':
            print '\n'
            continue
        else:
            creating = False
                
            for p in party:
                p.print_stats()

        return party

def main():
    party = create()
    for p in party:
        p.level_up()
        p.print_stats()
    


if __name__ == '__main__':
    main()