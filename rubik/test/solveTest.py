from unittest import TestCase
from rubik.view.solve import solve
 

class SolveTest(TestCase):
        
# Happy path
#    Test that the stubbed solve returns the correct result
    def test100_solve_returnStubbedSolution(self):
        parms = {}
        parms['cube'] = 'bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        result = solve(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertIn('integrity', result)
        self.assertEqual('FRBLUD', result.get('solution'))
    

    #test if cube is missing    
    def test110_solve_validateCube_missingCube(self):
        encodedCube = None 
        parms = {}
        parms['cube'] = encodedCube
        result = solve(parms)
        self.assertEqual('error: 123', result)
    
    #test that less than 54 characters in cube    
    def test120_solve_validateCube_lessThan54(self):
        encodedCube = 'bbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        parms = {}
        parms['cube'] = encodedCube
        result = solve(parms)
        self.assertEqual('error: 123', result)
        
    #test if invalid characters in cube          
    def test130_solve_validateCube_invalidValue(self):
        encodedCube = 'bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyy;;;;;;;;;'
        parms = {}
        parms['cube'] = encodedCube
        result = solve(parms)
        self.assertEqual('error: 123', result)
        
    #test if more or less than 6 unique Values in cube            
    def test140_solve_validateCube_UniqueValue(self):
        encodedCube = 'bbbbbbbbbrrrrrrrrroooooooo1ggggggggyyyyyyyyy1111111112'
        parms = {}
        parms['cube'] = encodedCube
        result = solve(parms)
        self.assertEqual('error: 123', result)
        
    def test150_solve_validateCube_UniqueCenters(self):
        encodedCube = 'bbbbbbbborrrrrrrrroooobooogggggggggyyyyyyyyywwwwwwwww'
        parms = {}
        parms['cube'] = encodedCube
        result = solve(parms)
        self.assertEqual('error: 123', result)
    
    def test160_solve_CorrectRotations(self):
        encodedCube = 'ooowbrrgywobwrggygwgbwgryywrwybobgywyrroybbybgorbwgoro'
        parms = {}
        parms['cube'] = encodedCube
        result = solve(parms)
        self.assertEqual('lfrbuFFRRBBLL', result['solution'])