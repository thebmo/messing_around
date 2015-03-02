import unittest
from heroes import *
import heroes.party as party

class TestHeroes(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_cleric(self):
        c = cleric.Cleric(name='Cleric')
        self.assertEqual(c.name , 'Cleric')
        self.assertEqual(c.CLASS, 'Cleric')
    
    def test_fighter(self):
        f = fighter.Fighter(name='Fighter')
        self.assertEqual( f.name , 'Fighter')
        self.assertEqual(f.CLASS, 'Fighter')
    
    def test_wizard(self):
        w = wizard.Wizard(name='Wizard')
        self.assertEqual( w.name , 'Wizard')
        self.assertEqual(w.CLASS, 'Wizard')
    
    def test_rogue(self):
        r = rogue.Rogue(name='Rogue')
        self.assertEqual( r.name , 'Rogue')        
        self.assertEqual(r.CLASS, 'Rogue')
        
    def test_party(self):
        c = cleric.Cleric(name='Cleric')
        f = fighter.Fighter(name='Fighter')
        r = rogue.Rogue(name='Rogue')
        w = wizard.Wizard(name='Wizard')
        
        p = party.Party([c,f,r,w])
        
        self.assertEqual(len(p.heroes), 4)
        self.assertEqual(p.gold, 0)
    

 
if __name__ == '__main__':
    unittest.main()