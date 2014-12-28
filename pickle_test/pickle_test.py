import pickle
import shelve
FILE = 'pickle-this'
class Animal(object):
    
    def __init__(self, name, noise, color):
        # returns an animal name, color, and noise
        self.name = name
        self.noise = noise
        self.color = color
class Mammal(Animal):
    fur = True
        
def main():
    chicken = Animal('chicken', 'ba-GAWK', 'white')
    cheetah = Animal('cheetah', 'chee-chaw', 'orange')
    gorilla = Animal('gorilla', 'OO-OO', 'black')
    cow = Mammal('cow', 'moo', 'white')
    animals = [chicken, cheetah, gorilla]

    print cow.fur
    
    # # pickle.dump( chicken, open(FILE, "wb"))
    # with open(FILE, 'rb') as p:
        # chicken = pickle.load(p)
    for animal in animals:
        print 'A %s is %s and goes \'%s\'' % (animal.name, animal.color, animal.noise)

if __name__ == '__main__':
    main()
    raw_input('\npress any key to continue')