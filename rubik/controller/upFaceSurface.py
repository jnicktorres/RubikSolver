import rubik.model.constants
from rubik.model.cube import Cube
from test.test_importlib.stubs import fake_filesystem_unittest

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
            for _ in range(0,4):
                result+='U'
                inputCube._rotateU()
            result += "RUrURUUr"
            inputCube._rotateR()
            inputCube._rotateU()
            inputCube._rotater()
            inputCube._rotateU()
            inputCube._rotateR()
            inputCube._rotateU()
            inputCube._rotateU()
            inputCube._rotater()
        
        # Checks for tree patters **************************************************
        elif treePattern(inputCube) == "up":
            result += "RUrURUUr"
            inputCube._rotateR()
            inputCube._rotateU()
            inputCube._rotater()
            inputCube._rotateU()
            inputCube._rotateR()
            inputCube._rotateU()
            inputCube._rotateU()
            inputCube._rotater()

        elif treePattern(inputCube) == "right":
           
            result += "uRUrURUUr"
            inputCube._rotateu()
            inputCube._rotateR()
            inputCube._rotateU()
            inputCube._rotater()
            inputCube._rotateU()
            inputCube._rotateR()
            inputCube._rotateU()
            inputCube._rotateU()
            inputCube._rotater()

        elif treePattern(inputCube) == "down":
            result += "UURUrURUUr"
            inputCube._rotateU()
            inputCube._rotateU()
            inputCube._rotateR()
            inputCube._rotateU()
            inputCube._rotater()
            inputCube._rotateU()
            inputCube._rotateR()
            inputCube._rotateU()
            inputCube._rotateU()
            inputCube._rotater()

            
        elif treePattern(inputCube) == "left":
            result += "URUrURUUr"
            inputCube._rotateU()
            inputCube._rotateR()
            inputCube._rotateU()
            inputCube._rotater()
            inputCube._rotateU()
            inputCube._rotateR()
            inputCube._rotateU()
            inputCube._rotateU()
            inputCube._rotater()
        #**************************************************
    
        # Checks for Fish Patters **************************************************    
    
        elif fishPattern(inputCube) == "topleft":
            result += "uRUrURUUr"
            inputCube._rotateu()
            inputCube._rotateR()
            inputCube._rotateU()
            inputCube._rotater()
            inputCube._rotateU()
            inputCube._rotateR()
            inputCube._rotateU()
            inputCube._rotateU()
            inputCube._rotater()

        elif fishPattern(inputCube) == "topright":
            result += "UURUrURUUr"
            inputCube._rotateU()
            inputCube._rotateU()
            inputCube._rotateR()
            inputCube._rotateU()
            inputCube._rotater()
            inputCube._rotateU()
            inputCube._rotateR()
            inputCube._rotateU()
            inputCube._rotateU()
            inputCube._rotater()

            
        elif fishPattern(inputCube) == "botright":
            result += "URUrURUUr"
            inputCube._rotateU()
            inputCube._rotateR()
            inputCube._rotateU()
            inputCube._rotater()
            inputCube._rotateU()
            inputCube._rotateR()
            inputCube._rotateU()
            inputCube._rotateU()
            inputCube._rotater()
  
        elif fishPattern(inputCube) == "botleft":
            result += "RUrURUUr"
            inputCube._rotateR()
            inputCube._rotateU()
            inputCube._rotater()
            inputCube._rotateU()
            inputCube._rotateR()
            inputCube._rotateU()
            inputCube._rotateU()
            inputCube._rotater()
        # **************************************************
        
        # Checks for Double Fish Pattern **************************************************
        elif doubleFishPattern(inputCube) == "leftdiagonal":
            result += "URUrURUUr"
            inputCube._rotateU()
            inputCube._rotateR()
            inputCube._rotateU()
            inputCube._rotater()
            inputCube._rotateU()
            inputCube._rotateR()
            inputCube._rotateU()
            inputCube._rotateU()
            inputCube._rotater()
 
        elif doubleFishPattern(inputCube) == "rightdiagonal":
            result += "RUrURUUr"
            inputCube._rotateR()
            inputCube._rotateU()
            inputCube._rotater()
            inputCube._rotateU()
            inputCube._rotateR()
            inputCube._rotateU()
            inputCube._rotateU()
            inputCube._rotater() 
        # **************************************************
        
        #if we come across cross pattern with no left facing yellow tile
        else: 
            result += "RUrURUUr"
            inputCube._rotateR()
            inputCube._rotateU()
            inputCube._rotater()
            inputCube._rotateU()
            inputCube._rotateR()
            inputCube._rotateU()
            inputCube._rotateU()
            inputCube._rotater()   
    return result







# Local Methods to check for different patterns

def crossPattern(inputCube):
    if (inputCube.get()[37] == inputCube.get()[40] and inputCube.get()[39] == inputCube.get()[40] and inputCube.get()[41] == inputCube.get()[40] and inputCube.get()[43] == inputCube.get()[40] and inputCube.get()[36] != inputCube.get()[40] and inputCube.get()[38] != inputCube.get()[40] and inputCube.get()[42] != inputCube.get()[40] and inputCube.get()[44] != inputCube.get()[40]):
        return True
    return False
def hasUpperFacePattern(inputCube):
    if (inputCube.get()[36] == inputCube.get()[40] and inputCube.get()[37] == inputCube.get()[40] and inputCube.get()[38] == inputCube.get()[40] and  inputCube.get()[39] == inputCube.get()[40] and inputCube.get()[41] == inputCube.get()[40] and  inputCube.get()[42] == inputCube.get()[40] and inputCube.get()[43] == inputCube.get()[40] and inputCube.get()[44] == inputCube.get()[40]):
        return True
    return False
def fishPattern(inputCube):
    if(inputCube.get()[37] == inputCube.get()[40] and inputCube.get()[39] == inputCube.get()[40] and inputCube.get()[41] == inputCube.get()[40] and inputCube.get()[43] == inputCube.get()[40] and inputCube.get()[36] == inputCube.get()[40] and inputCube.get()[38] != inputCube.get()[40] and inputCube.get()[42] != inputCube.get()[40] and inputCube.get()[44] != inputCube.get()[40]):
        return "topleft"
    elif(inputCube.get()[37] == inputCube.get()[40] and inputCube.get()[39] == inputCube.get()[40] and inputCube.get()[41] == inputCube.get()[40] and inputCube.get()[43] == inputCube.get()[40] and inputCube.get()[38] == inputCube.get()[40] and inputCube.get()[36] != inputCube.get()[40] and inputCube.get()[42] != inputCube.get()[40] and inputCube.get()[44] != inputCube.get()[40]):
        return "topright"
    elif(inputCube.get()[37] == inputCube.get()[40] and inputCube.get()[39] == inputCube.get()[40] and inputCube.get()[41] == inputCube.get()[40] and inputCube.get()[43] == inputCube.get()[40] and inputCube.get()[44] == inputCube.get()[40] and inputCube.get()[36] != inputCube.get()[40] and inputCube.get()[38] != inputCube.get()[40] and inputCube.get()[42] != inputCube.get()[40]):
        return "botright"
    elif(inputCube.get()[37] == inputCube.get()[40] and inputCube.get()[39] == inputCube.get()[40] and inputCube.get()[41] == inputCube.get()[40] and inputCube.get()[43] == inputCube.get()[40] and inputCube.get()[42] == inputCube.get()[40] and inputCube.get()[36] != inputCube.get()[40] and inputCube.get()[38] != inputCube.get()[40] and inputCube.get()[44] != inputCube.get()[40]):
        return "botleft"
    else:
        return "None"
    
def treePattern(inputCube):
    if(inputCube.get()[37] == inputCube.get()[40] and inputCube.get()[39] == inputCube.get()[40] and inputCube.get()[41] == inputCube.get()[40] and inputCube.get()[43] == inputCube.get()[40] and inputCube.get()[36] == inputCube.get()[40] and inputCube.get()[38] == inputCube.get()[40]):
        return "up"
    elif(inputCube.get()[37] == inputCube.get()[40] and inputCube.get()[39] == inputCube.get()[40] and inputCube.get()[41] == inputCube.get()[40] and inputCube.get()[43] == inputCube.get()[40] and inputCube.get()[42] == inputCube.get()[40] and inputCube.get()[44] == inputCube.get()[40]):
        return "down"
    elif(inputCube.get()[37] == inputCube.get()[40] and inputCube.get()[39] == inputCube.get()[40] and inputCube.get()[41] == inputCube.get()[40] and inputCube.get()[43] == inputCube.get()[40] and inputCube.get()[36] == inputCube.get()[40] and inputCube.get()[42] == inputCube.get()[40]):
        return "left"
    elif(inputCube.get()[37] == inputCube.get()[40] and inputCube.get()[39] == inputCube.get()[40] and inputCube.get()[41] == inputCube.get()[40] and inputCube.get()[43] == inputCube.get()[40] and inputCube.get()[44] == inputCube.get()[40] and inputCube.get()[38] == inputCube.get()[40]):
        return "right"
    else:
        return "None"
    
def doubleFishPattern(inputCube):
    if (inputCube.get()[37] == inputCube.get()[40] and inputCube.get()[39] == inputCube.get()[40] and inputCube.get()[41] == inputCube.get()[40] and inputCube.get()[43] == inputCube.get()[40] and inputCube.get()[36] == inputCube.get()[40] and inputCube.get()[44] == inputCube.get()[40] and inputCube.get()[38] != inputCube.get()[40] and inputCube.get()[42] != inputCube.get()[40]):
        return "leftdiagonal"
    elif(inputCube.get()[37] == inputCube.get()[40] and inputCube.get()[39] == inputCube.get()[40] and inputCube.get()[41] == inputCube.get()[40] and inputCube.get()[43] == inputCube.get()[40] and inputCube.get()[38] == inputCube.get()[40] and inputCube.get()[42] == inputCube.get()[40] and inputCube.get()[36] != inputCube.get()[40] and inputCube.get()[44] != inputCube.get()[40]):
        return "rightdiagonal"
