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
    inputCube = theCube
    result = ''
    ######
    
    
    if crossPattern(inputCube) == True:
        return result
        
    
    ## if no yellow top yellow tiles
    if noYellowPattern(inputCube) == True:
        result += 'FURurf'
        inputCube._rotateF()
        inputCube._rotateU()
        inputCube._rotateR()
        inputCube._rotateu()
        inputCube._rotater()
        inputCube._rotatef()
        
    if crossPattern(inputCube) == True:
        return result
        
        
    for _ in range(0,4):
        
        # Check if straight line pattern
        if straightLinePattern(inputCube) == "Vertical":     
            result += 'FURurf'
            inputCube._rotateF()
            inputCube._rotateU()
            inputCube._rotateR()
            inputCube._rotateu()
            inputCube._rotater()
            inputCube._rotatef()
           
        elif straightLinePattern(inputCube) == "Horizontal":      
            result += 'UFURurf'
            inputCube._rotateU()
            inputCube._rotateF()
            inputCube._rotateU()
            inputCube._rotateR()
            inputCube._rotateu()
            inputCube._rotater()
            inputCube._rotatef()
    
        # check if we get Cross
        if crossPattern(inputCube) == True:
            return result
     
     
        #Check if we get double corner and middle tile pattern
        if(doubleCornerPattern(inputCube) == "topleft"):
            result += 'FURurf'
            inputCube._rotateF()
            inputCube._rotateU()
            inputCube._rotateR()
            inputCube._rotateu()
            inputCube._rotater()
            inputCube._rotatef()
        elif(doubleCornerPattern(inputCube) == "topright"):
            result += 'uFURurf'
            inputCube._rotateu()
            inputCube._rotateF()
            inputCube._rotateU()
            inputCube._rotateR()
            inputCube._rotateu()
            inputCube._rotater()
            inputCube._rotatef()
        elif(doubleCornerPattern(inputCube) == "botright"):
            result += 'UUFURurf'
            inputCube._rotateU()
            inputCube._rotateU()
            inputCube._rotateF()
            inputCube._rotateU()
            inputCube._rotateR()
            inputCube._rotateu()
            inputCube._rotater()
            inputCube._rotatef()
        elif(doubleCornerPattern(inputCube) == "botleft"):
            result += 'UFURurf'
            inputCube._rotateU()
            inputCube._rotateF()
            inputCube._rotateU()
            inputCube._rotateR()
            inputCube._rotateu()
            inputCube._rotater()
            inputCube._rotatef()
            
        # check if we get Cross
        if crossPattern(inputCube) == True:
            return result    
            
        if singleYellowPattern(inputCube) == "top":
            result += 'FURurf'
            inputCube._rotateF()
            inputCube._rotateU()
            inputCube._rotateR()
            inputCube._rotateu()
            inputCube._rotater()
            inputCube._rotatef()
        elif singleYellowPattern(inputCube) == "right":
            result += 'uFURurf'
            inputCube._rotateu()
            inputCube._rotateF()
            inputCube._rotateU()
            inputCube._rotateR()
            inputCube._rotateu()
            inputCube._rotater()
            inputCube._rotatef()   
        elif singleYellowPattern(inputCube) == "bottom":
            result += 'UUFURurf'
            inputCube._rotateU()
            inputCube._rotateU()
            inputCube._rotateF()
            inputCube._rotateU()
            inputCube._rotateR()
            inputCube._rotateu()
            inputCube._rotater()
            inputCube._rotatef() 
        elif singleYellowPattern(inputCube) == "left":
            result += 'UFURurf'
            inputCube._rotateU()
            inputCube._rotateF()
            inputCube._rotateU()
            inputCube._rotateR()
            inputCube._rotateu()
            inputCube._rotater()
            inputCube._rotatef()          
               
        if crossPattern(inputCube) == True:
            return result                
        
    
    return result      

def straightLinePattern(inputCube):
    if (inputCube.get()[37] == inputCube.get()[40] and inputCube.get()[43] == inputCube.get()[40]):
        return "Vertical"
    elif (inputCube.get()[39] == inputCube.get()[40] and inputCube.get()[41] == inputCube.get()[40]):
        return "Horizontal"
    else:
        return "No"
    
def crossPattern(inputCube):
    if (inputCube.get()[37] == inputCube.get()[40] and inputCube.get()[39] == inputCube.get()[40] and inputCube.get()[41] == inputCube.get()[40] and  inputCube.get()[43] == inputCube.get()[40]):
        return True

def doubleCornerPattern(inputCube):
    if(inputCube.get()[37] == inputCube.get()[40] and inputCube.get()[39] == inputCube.get()[40]):
        return "topleft"
    elif(inputCube.get()[37] == inputCube.get()[40] and inputCube.get()[41] == inputCube.get()[40]):
        return "topright"
    elif(inputCube.get()[41] == inputCube.get()[40] and inputCube.get()[43] == inputCube.get()[40]):
        return "botright"
    elif(inputCube.get()[39] == inputCube.get()[40] and inputCube.get()[43] == inputCube.get()[40]):
        return "botleft"
    else:
        return "None"
    
def singleYellowPattern(inputCube):
    if inputCube.get()[37] == inputCube.get()[40]:
        return "top"
    if inputCube.get()[39] == inputCube.get()[40]:
        return "left"
    if inputCube.get()[41] == inputCube.get()[40]:
        return "right"
    if inputCube.get()[43] == inputCube.get()[40]:
        return "bot"

def noYellowPattern(inputCube):
    if (inputCube.get()[37] != inputCube.get()[40] and inputCube.get()[43] != inputCube.get()[40] and inputCube.get()[39] != inputCube.get()[40] and  inputCube.get()[41] != inputCube.get()[40]):
        return True   
    return False 