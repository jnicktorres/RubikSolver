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
    
    
        def test_rotate_010_ShouldRotate(self):
            cubeToRotate = 'boggbrybrroobrywwwworrgbgrrggooowbrgyybyygywwoybwwbygo'
            theCube = cube.Cube(cubeToRotate)
            rotatedCube = theCube._rotateF()
            self.assertEqual(rotatedCube, 'ygbbborrgyoowrywwwworrgbgrrggoooybrbyybyyggwowbrwwbygo')
            
        def test_rotate_020_ShouldRotate (self):
            cubeToRotate = 'boggbrybrroobrywwwworrgbgrrggooowbrgyybyygywwoybwwbygo'
            theCube = cube.Cube(cubeToRotate)
            rotatedCube = theCube._rotatef()
            self.assertEqual(rotatedCube, 'grrobbbgybooyryowwworrgbgrrggwoowbryyybyygrbwowgwwbygo')
            
            
        def test_rotate_030_ShouldRotate (self):
            cubeToRotate = 'boggbrybrroobrywwwworrgbgrrggooowbrgyybyygywwoybwwbygo'
            theCube = cube.Cube(cubeToRotate)
            rotatedCube = theCube._rotateR()
            self.assertEqual(rotatedCube, 'bobgbbybowbrwrowyoworggbbrrggooowbrgyygyyrywroygwwrygw')
            
            
        def test_rotate_040_ShouldRotate (self):
            cubeToRotate = 'boggbrybrroobrywwwworrgbgrrggooowbrgyybyygywwoybwwbygo'
            theCube = cube.Cube(cubeToRotate)
            rotatedCube = theCube._rotater()
            self.assertEqual(rotatedCube, 'bobgbgybwoyworwrbwoorbgbbrrggooowbrgyygyyrywwoygwwrygr')
            
            
        def test_rotate_050_ShouldRotate (self):
            cubeToRotate = 'boggbrybrroobrywwwworrgbgrrggooowbrgyybyygywwoybwwbygo'
            theCube = cube.Cube(cubeToRotate)
            rotatedCube = theCube._rotateB()
            self.assertEqual(rotatedCube, 'boggbrybrroobrgwwygrwrgorbrbgoyowyrgoywyygywwoybwwbgob')
            
        def test_rotate_060_ShouldRotate (self):
            cubeToRotate = 'boggbrybrroobrywwwworrgbgrrggooowbrgyybyygywwoybwwbygo'
            theCube = cube.Cube(cubeToRotate)
            rotatedCube = theCube._rotateb()
            self.assertEqual(rotatedCube, 'boggbrybrroybrywwbrbrogrwrgygogoworgbogyygywwoybwwbwyo')
            
        def test_rotate_070_ShouldRotate (self):
            cubeToRotate = 'boggbrybrroobrywwwworrgbgrrggooowbrgyybyygywwoybwwbygo'
            theCube = cube.Cube(cubeToRotate)
            rotatedCube = theCube._rotateL()
            self.assertEqual(rotatedCube, 'yogybrybrroobrywwwwoyrgwgrobogroggworybbygrwwbybgwbygo')
            
        def test_rotate_080_ShouldRotate (self):
            cubeToRotate = 'boggbrybrroobrywwwworrgbgrrggooowbrgyybyygywwoybwwbygo'
            theCube = cube.Cube(cubeToRotate)
            rotatedCube = theCube._rotatel()
            self.assertEqual(rotatedCube, 'oogwbrybrroobrywwwwoyrgygryowggorgobbybgygywwrybbwbrgo')
            
        def test_rotate_090_ShouldRotate (self):
            cubeToRotate = 'boggbrybrroobrywwwworrgbgrrggooowbrgyybyygywwoybwwbygo'
            theCube = cube.Cube(cubeToRotate)
            rotatedCube = theCube._rotateU()
            self.assertEqual(rotatedCube, 'roogbrybrworbrywwwggorgbgrrbogoowbrgyyywyywgboybwwbygo')
            
            
        def test_rotate_100_ShouldRotate (self):
            cubeToRotate = 'boggbrybrroobrywwwworrgbgrrggooowbrgyybyygywwoybwwbygo'
            theCube = cube.Cube(cubeToRotate)
            rotatedCube = theCube._rotateu()
            self.assertEqual(rotatedCube, 'ggogbrybrbogbrywwwroorgbgrrworoowbrgbgwyywyyyoybwwbygo')
        
        def test_rotate_110_ShouldRotate (self):
            cubeToRotate = 'boggbrybrroobrywwwworrgbgrrggooowbrgyybyygywwoybwwbygo'
            theCube = cube.Cube(cubeToRotate)
            rotatedCube = theCube._rotateD()
            self.assertEqual(rotatedCube, 'boggbrbrgroobryybrworrgbwwwggooowgrryybyygywwywogwyobb') 
            
        def test_rotate_111_ShouldRotate (self):
            cubeToRotate = 'boggbrybrroobrywwwworrgbgrrggooowbrgyybyygywwoybwwbygo'
            theCube = cube.Cube(cubeToRotate)
            rotatedCube = theCube._rotated()
            self.assertEqual(rotatedCube, 'boggbrwwwroobrygrrworrgbbrgggooowybryybyygywwbboywgowy')                         