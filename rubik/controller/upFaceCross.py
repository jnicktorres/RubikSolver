from rubik.model.constants import *
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
        
    
    ## if no top yellow tiles
    if noYellowPattern(inputCube) == True:
        result += 'FURurf'
        inputCube.rotate('FURurf')
        
    if crossPattern(inputCube) == True:
        return result
        
        
    for _ in range(0,4):
        
        # Check if straight line pattern
        if straightLinePattern(inputCube) == "Vertical":     
            result += 'FURurf'
            inputCube.rotate('FURurf')
            
        elif straightLinePattern(inputCube) == "Horizontal":      
            result += 'UFURurf'
            inputCube.rotate('UFURurf')
            
        # check if we get Cross
        if crossPattern(inputCube) == True:
            return result
     
     
        #Check if we get double corner and middle tile pattern
        if(doubleCornerPattern(inputCube) == "top left"):           
            result += 'FURurf'
            inputCube.rotate('FURurf')
            
        elif(doubleCornerPattern(inputCube) == "top right"):
            result += 'uFURurf'
            inputCube.rotate('uFURurf')
            
        elif(doubleCornerPattern(inputCube) == "bottom right"):
            result += 'UUFURurf'
            inputCube.rotate('UUFURurf')
            
        elif(doubleCornerPattern(inputCube) == "bottom left"):
            result += 'UFURurf'
            inputCube.rotate('UFURurf')
            
        # check if we get Cross
        if crossPattern(inputCube) == True:
            return result    
            
        if singleYellowPattern(inputCube) == "top":
            result += 'FURurf'
            inputCube.rotate('FURurf')
            
        elif singleYellowPattern(inputCube) == "right":
            result += 'uFURurf'
            inputCube.rotate('uFURurf')  
            
        elif singleYellowPattern(inputCube) == "bottom":
            result += 'UUFURurf'
            inputCube.rotate('UUFURurf')
            
        elif singleYellowPattern(inputCube) == "left":
            result += 'UFURurf'
            inputCube.rotate('UFURurf')         
               
        if crossPattern(inputCube) == True:
            return result                
        
    
    return result      

def straightLinePattern(inputCube):
    if (inputCube.get()[UTM] == inputCube.get()[UMM] and inputCube.get()[UBM] == inputCube.get()[UMM]):
        return "Vertical"
    elif (inputCube.get()[UML] == inputCube.get()[UMM] and inputCube.get()[UMR] == inputCube.get()[UMM]):
        return "Horizontal"
    else:
        return "No"
    
def crossPattern(inputCube):
    if (inputCube.get()[UTM] == inputCube.get()[UMM] and inputCube.get()[UML] == inputCube.get()[UMM] and inputCube.get()[UMR] == inputCube.get()[UMM] and  inputCube.get()[UBM] == inputCube.get()[UMM]):
        return True

def doubleCornerPattern(inputCube):
    if(inputCube.get()[UTM] == inputCube.get()[UMM] and inputCube.get()[UML] == inputCube.get()[UMM]):
        return "top left"
    elif(inputCube.get()[UTM] == inputCube.get()[UMM] and inputCube.get()[UMR] == inputCube.get()[UMM]):
        return "top right"
    elif(inputCube.get()[UMR] == inputCube.get()[UMM] and inputCube.get()[UBM] == inputCube.get()[UMM]):
        return "bottom right"
    elif(inputCube.get()[UML] == inputCube.get()[UMM] and inputCube.get()[UBM] == inputCube.get()[UMM]):
        return "bottom left"
    else:
        return "None"
    
def singleYellowPattern(inputCube):
    if inputCube.get()[UTM] == inputCube.get()[UMM]:
        return "top"
    if inputCube.get()[UML] == inputCube.get()[UMM]:
        return "left"
    if inputCube.get()[UMR] == inputCube.get()[UMM]:
        return "right"
    if inputCube.get()[UBM] == inputCube.get()[UMM]:
        return "bottom"

def noYellowPattern(inputCube):
    if (inputCube.get()[UTM] != inputCube.get()[UMM] and inputCube.get()[UBM] != inputCube.get()[UMM] and inputCube.get()[UML] != inputCube.get()[UMM] and  inputCube.get()[UMR] != inputCube.get()[UMM]):
        return True   
    return False 