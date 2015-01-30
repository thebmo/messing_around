"""
    this is the config file, below are globals for the
    whole application
"""


TESTING = True
CONSOLE = True
MAX_MONSTERS = 4
MAX_PARTY = 4

def main():
    
    print TESTING
    print CONSOLE
    raw_input('Prese Return to exit')
    
if __name__ == '__main__':
    main()