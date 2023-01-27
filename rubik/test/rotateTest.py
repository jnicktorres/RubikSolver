from unittest import TestCase
from rubik.view.rotate import rotate
 
class RotateTest(TestCase):
        
# Happy path
#    Test that the stubbed rotate returns the correct result
    def test100_rotate_returnStubbedSolution(self):
        encodedCube = 'bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'F'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertEqual(encodedCube, result.get('cube'))

#test that less than 54 characters in cube    

    def test_rotate_validateCube_lessThan54(self):
        encodedCube = 'bbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        parms = {}
        parms['cube'] = encodedCube
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('error: 123', result['status'])
        self.assertEqual(encodedCube, result.get('cube'))
        
#test if more or less than 6 unique Values in cube            
    def test_rotate_validateCube_UniqueValue(self):
        encodedCube = 'bbbbbbbbbrrrrrrrrroooooooo1ggggggggyyyyyyyyy1111111112'
        parms = {}
        parms['cube'] = encodedCube
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('error: 123', result['status'])
        self.assertEqual(encodedCube, result.get('cube'))    

#test if more or less than 6 unique Values in Center index of cube
 
    def test_rotate_validateCube_UniqueCenters(self):
        encodedCube = 'bbbbbbbbbrrrrrrrrroooobooogggggggggyyyyyyyyywwwwwwwww'
        parms = {}
        parms['cube'] = encodedCube
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('error: 123', result['status'])
        self.assertEqual(encodedCube, result.get('cube')) 
        
#test to see if missing direction will set to F
        
    def test_rotate_validateCube_MissingDirection(self):
        encodedCube = 'bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = ''
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('ok', result['status'])
        self.assertEqual(encodedCube, result.get('cube'))

#test to see if wrong direction is detected          
    def test_rotate_validateCube_WrongDirections(self):
        encodedCube = 'bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'FbLZ'
        result = rotate(parms)
        self.assertIn('status', result)
        self.assertEqual('error: 123', result['status'])
        self.assertEqual(encodedCube, result.get('cube'))