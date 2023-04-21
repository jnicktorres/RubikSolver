from rubik.model.constants import *
from rubik.model.cube import Cube


def solveUpSurface(theCube: Cube) -> str:
    '''
        This is the top-level function  for rotating
        a cube so that the up face is solved.
        
        input:  an instance of the cube class with up-face cross solved
        output: the rotations required to solve the up surface  
    '''  
    #### Variables  
    inputCube = theCube
    result = ''
    ######
 
    # Loop until we have face surface
    while hasUpperFacePattern(inputCube) == False:
   
        if(hasUpperFacePattern(inputCube) == True):
            return result
        
        
        # Check for cross pattern
        elif crossPattern(inputCube) == True:
            # only rotate 4 times to see each side
            for _ in range(0,4):
                result+='U'
                inputCube._rotateU()
            result += "RUrURUUr"
            inputCube.rotate("RUrURUUr")
        
        # Checks for tree patterns **************************************************
        elif treePattern(inputCube) == "up":
            result += "RUrURUUr"
            inputCube.rotate("RUrURUUr")

        elif treePattern(inputCube) == "right":
           
            result += "uRUrURUUr"
            inputCube.rotate("uRUrURUUr")

        elif treePattern(inputCube) == "down":
            result += "UURUrURUUr"
            inputCube.rotate("UURUrURUUr")

            
        elif treePattern(inputCube) == "left":
            result += "URUrURUUr"
            inputCube.rotate("URUrURUUr")
        #**************************************************
    
        # Checks for Fish Patterns **************************************************    
    
        elif fishPattern(inputCube) == "top left":
            result += "uRUrURUUr"
            inputCube.rotate("uRUrURUUr")

        elif fishPattern(inputCube) == "top right":
            result += "UURUrURUUr"
            inputCube.rotate("UURUrURUUr")

            
        elif fishPattern(inputCube) == "bottom right":
            result += "URUrURUUr"
            inputCube.rotate("URUrURUUr")
  
        elif fishPattern(inputCube) == "bottom left":
            result += "RUrURUUr"
            inputCube.rotate("RUrURUUr")
        # **************************************************
        
        # Checks for Double Fish Pattern **************************************************
        elif doubleFishPattern(inputCube) == "left diagonal":
            result += "URUrURUUr"
            inputCube.rotate("URUrURUUr")
 
        elif doubleFishPattern(inputCube) == "right diagonal":
            result += "RUrURUUr"
            inputCube.rotate("RUrURUUr")
        # **************************************************
        
        #if we come across cross pattern with no left facing yellow tile
        else: 
            result += "RUrURUUr"
            inputCube.rotate("RUrURUUr") 
    return result







# Local Methods to check for different patterns

def crossPattern(inputCube):
    if (inputCube.get()[UTM] == inputCube.get()[UMM] and inputCube.get()[UML] == inputCube.get()[UMM] and inputCube.get()[UMR] == inputCube.get()[UMM] and inputCube.get()[UBM] == inputCube.get()[UMM] and inputCube.get()[UTL] != inputCube.get()[UMM] and inputCube.get()[UTR] != inputCube.get()[UMM] and inputCube.get()[UBL] != inputCube.get()[UMM] and inputCube.get()[UBR] != inputCube.get()[UMM]):
        return True
    return False
def hasUpperFacePattern(inputCube):
    if (inputCube.get()[UTL] == inputCube.get()[UMM] and inputCube.get()[UTM] == inputCube.get()[UMM] and inputCube.get()[UTR] == inputCube.get()[UMM] and  inputCube.get()[UML] == inputCube.get()[UMM] and inputCube.get()[UMR] == inputCube.get()[UMM] and  inputCube.get()[UBL] == inputCube.get()[UMM] and inputCube.get()[UBM] == inputCube.get()[UMM] and inputCube.get()[UBR] == inputCube.get()[UMM]):
        return True
    return False
def fishPattern(inputCube):
    if(inputCube.get()[UTM] == inputCube.get()[UMM] and inputCube.get()[UML] == inputCube.get()[UMM] and inputCube.get()[UMR] == inputCube.get()[UMM] and inputCube.get()[UBM] == inputCube.get()[UMM] and inputCube.get()[UTL] == inputCube.get()[UMM] and inputCube.get()[UTR] != inputCube.get()[UMM] and inputCube.get()[UBL] != inputCube.get()[UMM] and inputCube.get()[UBR] != inputCube.get()[UMM]):
        return "top left"
    elif(inputCube.get()[UTM] == inputCube.get()[UMM] and inputCube.get()[UML] == inputCube.get()[UMM] and inputCube.get()[UMR] == inputCube.get()[UMM] and inputCube.get()[UBM] == inputCube.get()[UMM] and inputCube.get()[UTR] == inputCube.get()[UMM] and inputCube.get()[UTL] != inputCube.get()[UMM] and inputCube.get()[UBL] != inputCube.get()[UMM] and inputCube.get()[UBR] != inputCube.get()[UMM]):
        return "top right"
    elif(inputCube.get()[UTM] == inputCube.get()[UMM] and inputCube.get()[UML] == inputCube.get()[UMM] and inputCube.get()[UMR] == inputCube.get()[UMM] and inputCube.get()[UBM] == inputCube.get()[UMM] and inputCube.get()[UBR] == inputCube.get()[UMM] and inputCube.get()[UTL] != inputCube.get()[UMM] and inputCube.get()[UTR] != inputCube.get()[UMM] and inputCube.get()[UBL] != inputCube.get()[UMM]):
        return "bottom right"
    elif(inputCube.get()[UTM] == inputCube.get()[UMM] and inputCube.get()[UML] == inputCube.get()[UMM] and inputCube.get()[UMR] == inputCube.get()[UMM] and inputCube.get()[UBM] == inputCube.get()[UMM] and inputCube.get()[UBL] == inputCube.get()[UMM] and inputCube.get()[UTL] != inputCube.get()[UMM] and inputCube.get()[UTR] != inputCube.get()[UMM] and inputCube.get()[UBR] != inputCube.get()[UMM]):
        return "bottom left"
    else:
        return "None"
    
def treePattern(inputCube):
    if(inputCube.get()[UTM] == inputCube.get()[UMM] and inputCube.get()[UML] == inputCube.get()[UMM] and inputCube.get()[UMR] == inputCube.get()[UMM] and inputCube.get()[UBM] == inputCube.get()[UMM] and inputCube.get()[UTL] == inputCube.get()[UMM] and inputCube.get()[UTR] == inputCube.get()[UMM]):
        return "up"
    elif(inputCube.get()[UTM] == inputCube.get()[UMM] and inputCube.get()[UML] == inputCube.get()[UMM] and inputCube.get()[UMR] == inputCube.get()[UMM] and inputCube.get()[UBM] == inputCube.get()[UMM] and inputCube.get()[UBL] == inputCube.get()[UMM] and inputCube.get()[UBR] == inputCube.get()[UMM]):
        return "down"
    elif(inputCube.get()[UTM] == inputCube.get()[UMM] and inputCube.get()[UML] == inputCube.get()[UMM] and inputCube.get()[UMR] == inputCube.get()[UMM] and inputCube.get()[UBM] == inputCube.get()[UMM] and inputCube.get()[UTL] == inputCube.get()[UMM] and inputCube.get()[UBL] == inputCube.get()[UMM]):
        return "left"
    elif(inputCube.get()[UTM] == inputCube.get()[UMM] and inputCube.get()[UML] == inputCube.get()[UMM] and inputCube.get()[UMR] == inputCube.get()[UMM] and inputCube.get()[UBM] == inputCube.get()[UMM] and inputCube.get()[UBR] == inputCube.get()[UMM] and inputCube.get()[UTR] == inputCube.get()[UMM]):
        return "right"
    else:
        return "None"
    
def doubleFishPattern(inputCube):
    if (inputCube.get()[UTM] == inputCube.get()[UMM] and inputCube.get()[UML] == inputCube.get()[UMM] and inputCube.get()[UMR] == inputCube.get()[UMM] and inputCube.get()[UBM] == inputCube.get()[UMM] and inputCube.get()[UTL] == inputCube.get()[UMM] and inputCube.get()[UBR] == inputCube.get()[UMM] and inputCube.get()[UTR] != inputCube.get()[UMM] and inputCube.get()[UBL] != inputCube.get()[UMM]):
        return "left diagonal"
    elif(inputCube.get()[UTM] == inputCube.get()[UMM] and inputCube.get()[UML] == inputCube.get()[UMM] and inputCube.get()[UMR] == inputCube.get()[UMM] and inputCube.get()[UBM] == inputCube.get()[UMM] and inputCube.get()[UTR] == inputCube.get()[UMM] and inputCube.get()[UBL] == inputCube.get()[UMM] and inputCube.get()[UTL] != inputCube.get()[UMM] and inputCube.get()[UBR] != inputCube.get()[UMM]):
        return "right diagonal"
