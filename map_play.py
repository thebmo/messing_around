
def main():
    nicks = {
        1: 'BMO',
        2: 'Dickie',
        3: 'tduds',
        4: 'brendz84',
        }
    
 
    
    # Using maps technique
    def nick_checker(key):
        return nicks[key]
        
    nicks1 = map(nick_checker, nicks)
    
    
    # Using For iteration
    nicks2 = [nicks[k] for k in nicks]
    
    print 'nicks1:', nicks1
    print 'nicks2:', nicks2
    
    
    # print nicks1, type(nicks)
    # print set(nicks1), type(nicks)
    # print set(nicks1), type(set(nicks))
    
    # nick_set = set(nicks1)
    # print nick_set
    

if __name__ == '__main__':
    main()