from unittest import TestCase
from rubik.view.rotate import rotate
 
class RotateTest(TestCase):
        
# Happy path
#    Test that the stubbed rotate returns the correct result
    def test_rotate_010_ShouldRotate(self):
        cubeToRotate = 'boggbrybrroobrywwwworrgbgrrggooowbrgyybyygywwoybwwbygo'
        parms = {}
        parms['cube'] = cubeToRotate
        parms['dir'] = "F"
        result = rotate(parms)
        self.assertEqual(result.get('cube'), 'ygbbborrgyoowrywwwworrgbgrrggoooybrbyybyyggwowbrwwbygo')