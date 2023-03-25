import rubik.model.constants
from rubik.model.cube import Cube

def solveMiddleLayer(theCube: Cube) -> str:
    '''
        This is the top-level function  for rotating
        a cube so that the middle layer is solved.
        
        input:  an instance of the cube class with the bottom layer solved
        output: the rotations required to solve the middle layer  
    '''  
    #### Variables  
    fakeCube = theCube
    matchcol = fakeCube.get()[40] # color to be matched
    result = ""
    centers = [4,13,22,31]
    rightcorn = [2,11, 20,29]
    leftcorn = [0,9, 18,27]
    topcorn = [36,38,42,44]
    result = ''
    count = 0
    x = 0
    while count < 4:
        while x < 3:
            # Checks to see where we have matching face and top and rotate to move color to the side  of left
            #### Checks Front and left
            if (fakeCube.get()[1] == fakeCube.get()[4]) and (fakeCube.get()[43] == fakeCube.get()[31]):
                result += 'ulULUFuf'
                fakeCube._rotateu()
                fakeCube._rotatel()
                fakeCube._rotateU()
                fakeCube._rotateL()
                fakeCube._rotateU()
                fakeCube._rotateF()
                fakeCube._rotateu()
                fakeCube._rotatef()
                
            ####Checks Right and front
            if (fakeCube.get()[10] == fakeCube.get()[13]) and (fakeCube.get()[41] == fakeCube.get()[4]):
                result += 'ufUFURur'
                fakeCube._rotateu()
                fakeCube._rotatef()
                fakeCube._rotateU()
                fakeCube._rotateF()
                fakeCube._rotateU()
                fakeCube._rotateR()
                fakeCube._rotateu()
                fakeCube._rotater()
            ####Checks Back and right 
            if (fakeCube.get()[19] == fakeCube.get()[22]) and (fakeCube.get()[37] == fakeCube.get()[13]):
                result += 'urURUBub'
                fakeCube._rotateu()
                fakeCube._rotater()
                fakeCube._rotateU()
                fakeCube._rotateR()
                fakeCube._rotateU()
                fakeCube._rotateB()
                fakeCube._rotateu()
                fakeCube._rotateb()
            #checks left and back    
            if (fakeCube.get()[28] == fakeCube.get()[31]) and (fakeCube.get()[39] == fakeCube.get()[4]):
                result += 'ubUBULul'
                fakeCube._rotateu()
                fakeCube._rotateb()
                fakeCube._rotateU()
                fakeCube._rotateB()
                fakeCube._rotateU()
                fakeCube._rotateL()
                fakeCube._rotateu()
                fakeCube._rotatel()
                
            ######### check front top and upper bottom side and see if we rotate to right matching tile
            ## Checks front and right
            if (fakeCube.get()[1] == fakeCube.get()[4]) and (fakeCube.get()[43] == fakeCube.get()[13]):
                result+= 'URurufUF'
                fakeCube._rotateU()
                fakeCube._rotateR()
                fakeCube._rotateu()
                fakeCube._rotater()
                fakeCube._rotateu()
                fakeCube._rotatef()
                fakeCube._rotateU()
                fakeCube._rotateF()
            #checks 
            if (fakeCube.get()[10] == fakeCube.get()[13]) and (fakeCube.get()[41] == fakeCube.get()[4]):
                result += 'UBuburUR'
                fakeCube._rotateU()
                fakeCube._rotateB()
                fakeCube._rotateu()
                fakeCube._rotateb()
                fakeCube._rotateu()
                fakeCube._rotater()
                fakeCube._rotateU()
                fakeCube._rotateR()
            if (fakeCube.get()[19] == fakeCube.get()[22]) and (fakeCube.get()[37] == fakeCube.get()[31]):
                result += 'urURUBub'
                fakeCube._rotateu()
                fakeCube._rotater()
                fakeCube._rotateU()
                fakeCube._rotateR()
                fakeCube._rotateU()
                fakeCube._rotateB()
                fakeCube._rotateu()
                fakeCube._rotateb()
                
            if (fakeCube.get()[28] == fakeCube.get()[31]) and (fakeCube.get()[39] == fakeCube.get()[4]):
                result += 'ubUBULul'
                fakeCube._rotateu()
                fakeCube._rotateb()
                fakeCube._rotateU()
                fakeCube._rotateB()
                fakeCube._rotateU()
                fakeCube._rotateL()
                fakeCube._rotateu()
                fakeCube._rotatel()    
            result += 'U'
            fakeCube._rotateU()
            x+= 1
        
        
        
        count+= 1
    return 'B'      #TODO:  remove this stubbed value
