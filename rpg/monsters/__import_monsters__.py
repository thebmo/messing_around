import os

# deletes and rebuilds the init file for up to date
# __all__ variable
def main():
    mods = os.listdir(os.getcwd())
    monsters = []
    ignore = ['pyc', 'monster', '__init__', '__import_monsters__']
    # ignore = ['pyc', 'monster', '__']
    init = '__init__.py'
    for mod in mods:
        m = mod.split('.')
        if m[0] not in ignore and m[1] not in ignore:
            monsters.append(mod.split('.')[0])

    try:
        os.remove(init)

    except:
        print 'File did not exist, creating file'
        pass
    
    print 'Writing: %s' % monsters
    
    with open(init, 'w') as I:
        all = '__all__ = %s\n' % monsters
        I.write(all)


    raw_input('Finished!: press enter to close')
        

if __name__ == '__main__':
    main()