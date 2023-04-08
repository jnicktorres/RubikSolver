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
    result = ''
    loop1 = 0
    loop2 = 0
    ######
    
    while loop1 < 4:
        
        #Check to see if we have any incorrect tiles on right sides, and if we do correct them
        
        if not (fakeCube.get()[5] in [fakeCube.get()[4], fakeCube.get()[40]]) and not (fakeCube.get()[12] in [fakeCube.get()[13],fakeCube.get()[40]]):
            result+= 'URurufUF'
            fakeCube._rotateU()
            fakeCube._rotateR()
            fakeCube._rotateu()
            fakeCube._rotater()
            fakeCube._rotateu()
            fakeCube._rotatef()
            fakeCube._rotateU()
            fakeCube._rotateF()
              
        if not(fakeCube.get()[14] in [fakeCube.get()[13],fakeCube.get()[40]]) and not (fakeCube.get()[21] in [fakeCube.get()[22], fakeCube.get()[40]]):
            result += 'UBuburUR'
            fakeCube._rotateU()
            fakeCube._rotateB()
            fakeCube._rotateu()
            fakeCube._rotateb()
            fakeCube._rotateu()
            fakeCube._rotater()
            fakeCube._rotateU()
            fakeCube._rotateR()
            
        if not (fakeCube.get()[23] in [fakeCube.get()[22],fakeCube.get()[40]]) and not (fakeCube.get()[30] in [fakeCube.get()[31], fakeCube.get()[40]]):
            result += 'ULulubUB'
            fakeCube._rotateU()
            fakeCube._rotateL()
            fakeCube._rotateu()
            fakeCube._rotatel()
            fakeCube._rotateu()
            fakeCube._rotateb()
            fakeCube._rotateU()
            fakeCube._rotateB()
            
        if not(fakeCube.get()[32] in [fakeCube.get()[31],fakeCube.get()[40]]) and not (fakeCube.get()[3] in [fakeCube.get()[4],fakeCube.get()[40]]):
            result += 'UFufulUL'
            fakeCube._rotateU()
            fakeCube._rotateF()
            fakeCube._rotateu()
            fakeCube._rotatef()
            fakeCube._rotateu()
            fakeCube._rotatel()
            fakeCube._rotateU()
            fakeCube._rotateL()
        
        #Check to see if we have any incorrect tiles on left sides, and if we do correct them 
        
        if not (fakeCube.get()[3] in [fakeCube.get()[4], fakeCube.get()[40]]) and not (fakeCube.get()[32] in [fakeCube.get()[31],fakeCube.get()[40]]):
            result += 'ulULUFuf'
            fakeCube._rotateu()
            fakeCube._rotatel()
            fakeCube._rotateU()
            fakeCube._rotateL()
            fakeCube._rotateU()
            fakeCube._rotateF()
            fakeCube._rotateu()
            fakeCube._rotatef()            
              
        if not(fakeCube.get()[12] in [fakeCube.get()[13],fakeCube.get()[40]]) and not (fakeCube.get()[5] in [fakeCube.get()[4], fakeCube.get()[40]]):
            result += 'ufUFURur'
            fakeCube._rotateu()
            fakeCube._rotatef()
            fakeCube._rotateU()
            fakeCube._rotateF()
            fakeCube._rotateU()
            fakeCube._rotateR()
            fakeCube._rotateu()
            fakeCube._rotater()  
            
        if not (fakeCube.get()[21] in [fakeCube.get()[22],fakeCube.get()[40]]) and not (fakeCube.get()[14] in [fakeCube.get()[13], fakeCube.get()[40]]):
            result += 'urURUBub'
            fakeCube._rotateu()
            fakeCube._rotater()
            fakeCube._rotateU()
            fakeCube._rotateR()
            fakeCube._rotateU()
            fakeCube._rotateB()
            fakeCube._rotateu()
            fakeCube._rotateb()
            
        if not(fakeCube.get()[30] in [fakeCube.get()[31],fakeCube.get()[40]]) and not (fakeCube.get()[23] in [fakeCube.get()[22],fakeCube.get()[40]]):
            result += 'ubUBULul'
            fakeCube._rotateu()
            fakeCube._rotateb()
            fakeCube._rotateU()
            fakeCube._rotateB()
            fakeCube._rotateU()
            fakeCube._rotateL()
            fakeCube._rotateu()
            fakeCube._rotatel()       
        
        
    ## check to see if we have solved layer after correction
        if(hasMiddle(fakeCube) == True):
            return result
            
            
        while loop2 < 3:
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
            if (fakeCube.get()[28] == fakeCube.get()[31]) and (fakeCube.get()[39] == fakeCube.get()[22]):
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
            #checks right and back
            if (fakeCube.get()[10] == fakeCube.get()[13]) and (fakeCube.get()[41] == fakeCube.get()[22]):
                result += 'UBuburUR'
                fakeCube._rotateU()
                fakeCube._rotateB()
                fakeCube._rotateu()
                fakeCube._rotateb()
                fakeCube._rotateu()
                fakeCube._rotater()
                fakeCube._rotateU()
                fakeCube._rotateR()
            #checks back and left
            if (fakeCube.get()[19] == fakeCube.get()[22]) and (fakeCube.get()[37] == fakeCube.get()[31]):
                result += 'ULulubUB'
                fakeCube._rotateU()
                fakeCube._rotateL()
                fakeCube._rotateu()
                fakeCube._rotatel()
                fakeCube._rotateu()
                fakeCube._rotateb()
                fakeCube._rotateU()
                fakeCube._rotateB()
            #checks left and front   
            if (fakeCube.get()[28] == fakeCube.get()[31]) and (fakeCube.get()[39] == fakeCube.get()[4]):
                result += 'UFufulUL'
                fakeCube._rotateU()
                fakeCube._rotateF()
                fakeCube._rotateu()
                fakeCube._rotatef()
                fakeCube._rotateu()
                fakeCube._rotatel()
                fakeCube._rotateU()
                fakeCube._rotateL()    
            result += 'U'
            fakeCube._rotateU()
           
        loop1 += 1    
    return result


def hasMiddle(fakeCube):
    #Do a check to see if we already have middle layer
    if(fakeCube.get()[45] == fakeCube.get()[49] and fakeCube.get()[46] == fakeCube.get()[49] and fakeCube.get()[47] == fakeCube.get()[49] and fakeCube.get()[48] == fakeCube.get()[49] and fakeCube.get()[50] == fakeCube.get()[49] and fakeCube.get()[51] == fakeCube.get()[49] and fakeCube.get()[52] == fakeCube.get()[49] and fakeCube.get()[53] == fakeCube.get()[49]):
        if(fakeCube.get()[3] == fakeCube.get()[4] and fakeCube.get()[5] == fakeCube.get()[4] and fakeCube.get()[6] == fakeCube.get()[4] and fakeCube.get()[7] == fakeCube.get()[4] and fakeCube.get()[8] == fakeCube.get()[4]):
            if(fakeCube.get()[12] == fakeCube.get()[13] and fakeCube.get()[14] == fakeCube.get()[13] and fakeCube.get()[15] == fakeCube.get()[13] and fakeCube.get()[16] == fakeCube.get()[13] and fakeCube.get()[17] == fakeCube.get()[13]):
                if(fakeCube.get()[21] == fakeCube.get()[22] and fakeCube.get()[23] == fakeCube.get()[22] and fakeCube.get()[24] == fakeCube.get()[22] and fakeCube.get()[25] == fakeCube.get()[22] and fakeCube.get()[26] == fakeCube.get()[22]):
                    if(fakeCube.get()[30] == fakeCube.get()[31] and fakeCube.get()[32] == fakeCube.get()[31] and fakeCube.get()[33] == fakeCube.get()[31] and fakeCube.get()[34] == fakeCube.get()[31] and fakeCube.get()[35] == fakeCube.get()[31]):
                        return True
    return False