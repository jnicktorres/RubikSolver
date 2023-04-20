from unittest import TestCase
from rubik.view.rotate import rotate
 
class RotateTest(TestCase):
        
# Happy path
#    Test that the stubbed rotate returns the correct result
    def test110_rotate_returnStubbedSolution(self):
        encodedCube = 'bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'F'
        result = rotate(parms)
        self.assertEqual('ok', result['status'])
        self.assertEqual('bbbbbbbbbyrryrryrroooooooooggwggwggwyyyyyygggrrrwwwwww', result.get('cube'))

#test that less than 54 characters in cube    

    def test120_rotate_validateCube_lessThan54(self):
        encodedCube = 'bbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        parms = {}
        parms['cube'] = encodedCube
        result = rotate(parms)
        self.assertEqual('error: Invalid Values in Cube or Invalid Length of Cube', result['status'])
    
        
#test if more or less than 6 unique Values in cube            
    def test130_rotate_validateCube_UniqueValue(self):
        encodedCube = 'bbbbbbbbbrrrrrrrrroooooooo1ggggggggyyyyyyyyy1111111112'
        parms = {}
        parms['cube'] = encodedCube
        result = rotate(parms)
        self.assertEqual('error: Invalid Unique Values', result['status'])
          

#test if more or less than 6 unique Values in Center index of cube
 
    def test140_rotate_validateCube_UniqueCenters(self):
        encodedCube = 'bbbbbbbbbrrrrrrrrroooobooogggggggggyyyyyyyyywwwwwwwww'
        parms = {}
        parms['cube'] = encodedCube
        result = rotate(parms)
        self.assertEqual('error: Invalid Values in Cube or Invalid Length of Cube', result['status'])
        
#test to see if missing direction will set to F

#test to see if wrong direction is detected          
    def test160_rotate_validateCube_WrongDirections(self):
        encodedCube = 'bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'FbLZ'
        result = rotate(parms)
        self.assertEqual('error: Invalid Directions', result['status'])
    def test170_rotate_validateCube_EmptyDirection(self):
        encodedCube = 'bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = ''
        result = rotate(parms)
        self.assertEqual('bbbbbbbbbyrryrryrroooooooooggwggwggwyyyyyygggrrrwwwwww', result['cube'])
    def test180_rotate_validateCube_WrongDirection2(self):
        encodedCube = 'bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'd'
        result = rotate(parms)
        self.assertEqual('error: Invalid Directions', result['status'])
    
    def test190_rotate_validateCube_WrongDirection3(self):
        encodedCube = 'bbbbbbbbbrrrrrrrrrooooooooogggggggggyyyyyyyyywwwwwwwww'
        parms = {}
        parms['cube'] = encodedCube
        parms['dir'] = 'FfRrBbLlUuDd'
        result = rotate(parms)
        self.assertEqual('error: Invalid Directions', result['status'])
