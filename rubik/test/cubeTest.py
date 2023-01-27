'''
Created on Jan 26, 2023

@author: jnich
'''


import unittest
import rubik.model.cube as cube 

class CubeTest(unittest.TestCase):
    
    # Analysis of Cube
    #
    #    Cube: class, instance of a state machine, maintain internal state
    #    Methods:    __init__    constructs cube from a serialized string
    #                get         yields serialized string of a internal representation
    #                rotate      performs rotations on the cube per 'dir' key
    #
    #    Analysis:    Cube.rotate
    #        inputs: 
    #            directions:    string, len .GE. 0, [FfRrBbLlUu]; optional, defaulting to F if missing; unvalidated
    #        outputs:
    #            side-effects:     no external effects: internal state change
    #            nominal:
    #                return serialized rotated cube
    #            abnormal:
    #                raise DirException
    
    
        def test_rotate_010_ShouldRotate (self):
            cubeToRotate = 'ygrwbgyggbobrryrrwobrggrgwywyryorbbggwwbyybwwooyowbooo'
            theCube = cube.Cube(cubeToRotate)
            rotatedCube = theCube.rotate('F')
            self.assertEqual(rotatedCube, 'ywygbgggrbobwrywrwobrggrgwywyoyoobbygwwbyygrrrrbowbooo')
                    