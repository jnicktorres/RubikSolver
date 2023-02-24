from unittest import TestCase
from rubik.view.solve import solve
from rubik.view.rotate import rotate
from rubik.model.cube import Cube
 

class SolveTest(TestCase):
        
    
    #test if cube is missing    
    def test110_solve_validateCube_missingCube(self):
        encodedCube = None 
        parms = {}
        parms['cube'] = encodedCube
        result = solve(parms)
        error = {'status': 'error: 123'}
        self.assertEqual(error, result)
    
    #test that less than 54 characters in cube    
    def test120_solve_validateCube_lessThan54(self):
        encodedCube = 'bbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        parms = {}
        parms['cube'] = encodedCube
        result = solve(parms)
        error = {'status': 'error: 123'}
        self.assertEqual(error, result)
        
    #test if invalid characters in cube          
    def test130_solve_validateCube_invalidValue(self):
        encodedCube = 'bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyy;;;;;;;;;'
        parms = {}
        parms['cube'] = encodedCube
        result = solve(parms)
        error = {'status': 'error: 123'}
        self.assertEqual(error, result)
        
    #test if more or less than 6 unique Values in cube            
    def test140_solve_validateCube_UniqueValue(self):
        encodedCube = 'bbbbbbbbbrrrrrrrrroooooooo1ggggggggyyyyyyyyy1111111112'
        parms = {}
        parms['cube'] = encodedCube
        result = solve(parms)
        error = {'status': 'error: 123'}
        self.assertEqual(error, result)
        
    #test to make sure cube has unique center values
    def test150_solve_validateCube_UniqueCenters(self):
        encodedCube = 'bbbbbbbborrrrrrrrroooobooogggggggggyyyyyyyyywwwwwwwww'
        parms = {}
        parms['cube'] = encodedCube
        result = solve(parms)
        error = {'status': 'error: 123'}
        self.assertEqual(error, result)
    
    # tests to see if cross is created after rotate
    def test160_solve_cross(self):
        encodedCube = 'ooowbrrgywobwrggygwgbwgryywrwybobgywyrroybbybgorbwgoro'
        parms = {}
        parms['cube'] = encodedCube
        dirs = solve(parms)
        parms['dir'] = dirs['solution']
        result = rotate(parms)
        self.assertEqual('w', result.get('cube')[46])
        self.assertEqual('w', result.get('cube')[48])
        self.assertEqual('w', result.get('cube')[50])
        self.assertEqual('w', result.get('cube')[52])
        self.assertEqual(result.get('cube')[4], result.get('cube')[7])
        self.assertEqual(result.get('cube')[13], result.get('cube')[16])
        self.assertEqual(result.get('cube')[22], result.get('cube')[25])
        self.assertEqual(result.get('cube')[31], result.get('cube')[34])