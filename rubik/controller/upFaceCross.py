import rubik.model.constants
from rubik.model.cube import Cube

def solveUpCross(theCube: Cube) -> str:
    '''
        This is the top-level function  for rotating
        a cube into the up-face cross configuration.
        
        input:  an instance of the cube class with the middle layer solved
        output: the rotations required to solve the up-face cross  
    '''  
    #### Variables  
    fakeCube = theCube
    result = ''
    ######
    
    
    if crossPattern(fakeCube) == True:
        return result
        
    
    ## if no yellow top yellow tiles
    if noYellowPattern(fakeCube) == True:
        result += 'FURurf'
        fakeCube._rotateF()
        fakeCube._rotateU()
        fakeCube._rotateR()
        fakeCube._rotateu()
        fakeCube._rotater()
        fakeCube._rotatef()
        
    if crossPattern(fakeCube) == True:
        return result
        
        
    for _ in range(0,4):
        
        # Check if straight line pattern
        if straightLinePattern(fakeCube) == "Vertical":     
            result += 'FURurf'
            fakeCube._rotateF()
            fakeCube._rotateU()
            fakeCube._rotateR()
            fakeCube._rotateu()
            fakeCube._rotater()
            fakeCube._rotatef()
           
        elif straightLinePattern(fakeCube) == "Horizontal":      
            result += 'UFURurf'
            fakeCube._rotateU()
            fakeCube._rotateF()
            fakeCube._rotateU()
            fakeCube._rotateR()
            fakeCube._rotateu()
            fakeCube._rotater()
            fakeCube._rotatef()
    
        # check if we get Cross
        if crossPattern(fakeCube) == True:
            return result
     
     
        #Check if we get double corner and middle tile pattern
        if(doubleCornerPattern(fakeCube) == "topleft"):
            result += 'FURurf'
            fakeCube._rotateF()
            fakeCube._rotateU()
            fakeCube._rotateR()
            fakeCube._rotateu()
            fakeCube._rotater()
            fakeCube._rotatef()
        elif(doubleCornerPattern(fakeCube) == "topright"):
            result += 'uFURurf'
            fakeCube._rotateu()
            fakeCube._rotateF()
            fakeCube._rotateU()
            fakeCube._rotateR()
            fakeCube._rotateu()
            fakeCube._rotater()
            fakeCube._rotatef()
        elif(doubleCornerPattern(fakeCube) == "botright"):
            result += 'UUFURurf'
            fakeCube._rotateU()
            fakeCube._rotateU()
            fakeCube._rotateF()
            fakeCube._rotateU()
            fakeCube._rotateR()
            fakeCube._rotateu()
            fakeCube._rotater()
            fakeCube._rotatef()
        elif(doubleCornerPattern(fakeCube) == "botleft"):
            result += 'UFURurf'
            fakeCube._rotateU()
            fakeCube._rotateF()
            fakeCube._rotateU()
            fakeCube._rotateR()
            fakeCube._rotateu()
            fakeCube._rotater()
            fakeCube._rotatef()
            
        # check if we get Cross
        if crossPattern(fakeCube) == True:
            return result    
            
        if singleYellowPattern(fakeCube) == "top":
            result += 'FURurf'
            fakeCube._rotateF()
            fakeCube._rotateU()
            fakeCube._rotateR()
            fakeCube._rotateu()
            fakeCube._rotater()
            fakeCube._rotatef()
        elif singleYellowPattern(fakeCube) == "right":
            result += 'uFURurf'
            fakeCube._rotateu()
            fakeCube._rotateF()
            fakeCube._rotateU()
            fakeCube._rotateR()
            fakeCube._rotateu()
            fakeCube._rotater()
            fakeCube._rotatef()   
        elif singleYellowPattern(fakeCube) == "bottom":
            result += 'UUFURurf'
            fakeCube._rotateU()
            fakeCube._rotateU()
            fakeCube._rotateF()
            fakeCube._rotateU()
            fakeCube._rotateR()
            fakeCube._rotateu()
            fakeCube._rotater()
            fakeCube._rotatef() 
        elif singleYellowPattern(fakeCube) == "left":
            result += 'UFURurf'
            fakeCube._rotateU()
            fakeCube._rotateF()
            fakeCube._rotateU()
            fakeCube._rotateR()
            fakeCube._rotateu()
            fakeCube._rotater()
            fakeCube._rotatef()          
               
        if crossPattern(fakeCube) == True:
            return result                
        
    
    return result      

def straightLinePattern(fakeCube):
    if (fakeCube.get()[37] == fakeCube.get()[40] and fakeCube.get()[43] == fakeCube.get()[40]):
        return "Vertical"
    elif (fakeCube.get()[39] == fakeCube.get()[40] and fakeCube.get()[43] == fakeCube.get()[41]):
        return "Horizontal"
    else:
        return "No"
    
def crossPattern(fakeCube):
    if (fakeCube.get()[37] == fakeCube.get()[40] and fakeCube.get()[43] == fakeCube.get()[40] and fakeCube.get()[39] == fakeCube.get()[40] and  fakeCube.get()[43] == fakeCube.get()[41]):
        return True

def doubleCornerPattern(fakeCube):
    if(fakeCube.get()[37] == fakeCube.get()[40] and fakeCube.get()[39] == fakeCube.get()[40]):
        return "topleft"
    elif(fakeCube.get()[37] == fakeCube.get()[40] and fakeCube.get()[41] == fakeCube.get()[40]):
        return "topright"
    elif(fakeCube.get()[41] == fakeCube.get()[40] and fakeCube.get()[43] == fakeCube.get()[40]):
        return "botright"
    elif(fakeCube.get()[39] == fakeCube.get()[40] and fakeCube.get()[43] == fakeCube.get()[40]):
        return "botleft"
    else:
        return "None"
    
def singleYellowPattern(fakeCube):
    if fakeCube.get()[37] == fakeCube.get()[40]:
        return "top"
    if fakeCube.get()[39] == fakeCube.get()[40]:
        return "left"
    if fakeCube.get()[41] == fakeCube.get()[40]:
        return "right"
    if fakeCube.get()[43] == fakeCube.get()[40]:
        return "bot"

def noYellowPattern(fakeCube):
    if (fakeCube.get()[37] != fakeCube.get()[40] and fakeCube.get()[43] != fakeCube.get()[40] and fakeCube.get()[39] != fakeCube.get()[40] and  fakeCube.get()[41] != fakeCube.get()[40]):
        return True   
    return False 