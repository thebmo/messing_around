# normal dict
names = {
    'bmo': 'BMO',
    'fred': 'Fred',
    'hoydis': 'Michael',
    'richard': 'Richard',
    'robert': 'Robert',
    'lauren': 'lauren',
    'melissa': 'missah',
    'dickie': 'Dickie',
    'jared': 'jared',
    'tim': 'tduds',
    'mendel': 'Butters',
    'chua': 'chewer',
    'zoey': 'zoe'
    }

# creates a nested dict
for name in names:
    names[name] = {
        'nick': names[name],
        'num' : '5555555555',
        'email': 'null@void.net',
        }

# prints the dict
def print_dict(names):
    for name in names:
        print '{: >10}'.format(name), '|', names[name]
    

# creats a reverse dict
rnames = {}
for k, v in names.items():
    rnames[v['nick']] = k
 
print_dict(rnames)