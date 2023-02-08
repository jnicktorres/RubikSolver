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
        
    #test that less than 54 characters in cube    
    def test110_solve_validateCube_lessThan54(self):
        encodedCube = 'bbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        parms = {}
        parms['cube'] = encodedCube
        result = solve(parms)
        self.assertEqual('error: 123', result['status'])
    
        
    # #test if more or less than 6 unique Values in cube            
    # def test130_solve_validateCube_UniqueValue(self):
    #     encodedCube = 'bbbbbbbbbrrrrrrrrroooooooo1ggggggggyyyyyyyyy1111111112'
    #     parms = {}
    #     parms['cube'] = encodedCube
    #     result = rotate(parms)
    #     self.assertEqual('error: 123', result)
    #
    #
    # #test if more or less than 6 unique Values in Center index of cube
    # def test140_rotate_validateCube_UniqueCenters(self):
    #     encodedCube = 'bbbbbbbbbrrrrrrrrroooobooogggggggggyyyyyyyyywwwwwwwww'
    #     parms = {}
    #     parms['cube'] = encodedCube
    #     result = rotate(parms)
    #     self.assertEqual('error: 123', result)