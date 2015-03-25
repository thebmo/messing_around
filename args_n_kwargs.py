# Prints any number of arguments
def print_args(*args):
    if args:
        for a in args:
            print a

# Prints exactly 3 arguments
def print_three(a, b, c):
    print a, b, c, 'as easy as 1 2 3'
    
    
if __name__ == '__main__':
    myList = ['Bmo', 'Juju', 'Jared']
    print_args(myList, 'turkey', 'tofu')
    print ''
    print_three(*myList)