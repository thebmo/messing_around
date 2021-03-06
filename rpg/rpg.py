import argparse
import combat
import cPickle as pickle


# Main call, defines any options that may be
def main():
    # Parser options
    parser = argparse.ArgumentParser(description='Process arguments')
    parser.add_argument('-l', '--levels', metavar='L', dest='levels',
        type=int, help='sets the number of levels to boost the party')
    parser.add_argument('-c', '--count', metavar='C', dest='count',
        type=int, default=0, help='sets the number of monsters')
    parser.add_argument('-m', '--monsters', metavar='M', dest='monsters',
        help='sets the type of monsters (comma separated)')
        
    parser.add_argument('-s', '--save',
        help='saves the party after combat', action='store_true')    
    parser.add_argument('-n', '--new',
        help='creates a fresh party on startup', action='store_true')
    parser.add_argument('-p', '--stats',
        help='prints party stats after combat', action='store_true')
    parser.add_argument('--heal', action='store_true',
        help='heals the party to full before combat')

    args = parser.parse_args()
    # End parser options
    
    # Prints out args
    if args:
        if args.levels: print 'level boost:', args.levels
        if args.count: print 'monster count:', args.count
        if args.monsters:
            if ',' in args.monsters:
                monsters = args.monsters.lower().split(',')
            else:
                monsters = [args.monsters.lower()]
            
            print 'loading:', monsters
        else:
            monsters = []
            
            
        print 'save:', args.save
        print 'new party', args.new
        print 'print stats', args.stats
    

    #Loads the specified party
    if args.new:
        P_FILE = 'new.p'
    
    else:
        P_FILE = 'party.p'
        
    party = pickle.load(open(P_FILE, 'rb'))
    
    # Levels up the party based on boost option
    if args.levels:
        for r in range(args.levels):
            party.level_up()
    
    # Heals party
    if args.heal:
        party.heal()
    
    # Starts combat
    raw_input('starting combat...')
    combat.start_combat(party, monster_list=monsters, count=args.count)
    if args.stats:
        party.print_stats()
        print '\nGOLD:', party.gold
    
    # Saves the party if specified
    if args.save:
        pickle.dump(party, open('party.p', 'wb'))


if __name__ == '__main__':
    main()
    
