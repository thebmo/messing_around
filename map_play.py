def main():
    nicks = {
        'bmo': 'BMO',
        'mike': 'Dickie',
        'tim': 'tduds',
        }

    def nick_checker(key):
        return nicks[key]
    nicks1 = map(nick_checker, nicks)
    
    print nicks1, type(nicks)
    print set(nicks1), type(nicks)
    print set(nicks1), type(set(nicks))
    
    nick_set = set(nicks1)
    print nick_set
    

if __name__ == '__main__':
    main()