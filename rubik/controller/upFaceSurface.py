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
    fakeCube = theCube
    result = ''
    ######
 
    # Loop until we have face surface
    while hasUpperFacePattern(fakeCube) == False:
   
       
        if(hasUpperFacePattern(fakeCube) == True):
            return result
        
        
        # Check for cross pattern
        elif crossPattern(fakeCube) == True:
            for _ in range(0,4):
                result+='U'
                fakeCube._rotateU()
            result += "RUrURUUr"
            fakeCube._rotateR()
            fakeCube._rotateU()
            fakeCube._rotater()
            fakeCube._rotateU()
            fakeCube._rotateR()
            fakeCube._rotateU()
            fakeCube._rotateU()
            fakeCube._rotater()
        
        # Checks for tree patters **************************************************
        elif treePattern(fakeCube) == "up":
            result += "RUrURUUr"
            fakeCube._rotateR()
            fakeCube._rotateU()
            fakeCube._rotater()
            fakeCube._rotateU()
            fakeCube._rotateR()
            fakeCube._rotateU()
            fakeCube._rotateU()
            fakeCube._rotater()

        elif treePattern(fakeCube) == "right":
           
            result += "uRUrURUUr"
            fakeCube._rotateu()
            fakeCube._rotateR()
            fakeCube._rotateU()
            fakeCube._rotater()
            fakeCube._rotateU()
            fakeCube._rotateR()
            fakeCube._rotateU()
            fakeCube._rotateU()
            fakeCube._rotater()

        elif treePattern(fakeCube) == "down":
            result += "UURUrURUUr"
            fakeCube._rotateU()
            fakeCube._rotateU()
            fakeCube._rotateR()
            fakeCube._rotateU()
            fakeCube._rotater()
            fakeCube._rotateU()
            fakeCube._rotateR()
            fakeCube._rotateU()
            fakeCube._rotateU()
            fakeCube._rotater()

            
        elif treePattern(fakeCube) == "left":
            result += "URUrURUUr"
            fakeCube._rotateU()
            fakeCube._rotateR()
            fakeCube._rotateU()
            fakeCube._rotater()
            fakeCube._rotateU()
            fakeCube._rotateR()
            fakeCube._rotateU()
            fakeCube._rotateU()
            fakeCube._rotater()
        #**************************************************
    
        # Checks for Fish Patters **************************************************    
    
        elif fishPattern(fakeCube) == "topleft":
            result += "uRUrURUUr"
            fakeCube._rotateu()
            fakeCube._rotateR()
            fakeCube._rotateU()
            fakeCube._rotater()
            fakeCube._rotateU()
            fakeCube._rotateR()
            fakeCube._rotateU()
            fakeCube._rotateU()
            fakeCube._rotater()

        elif fishPattern(fakeCube) == "topright":
            result += "UURUrURUUr"
            fakeCube._rotateU()
            fakeCube._rotateU()
            fakeCube._rotateR()
            fakeCube._rotateU()
            fakeCube._rotater()
            fakeCube._rotateU()
            fakeCube._rotateR()
            fakeCube._rotateU()
            fakeCube._rotateU()
            fakeCube._rotater()

            
        elif fishPattern(fakeCube) == "botright":
            result += "URUrURUUr"
            fakeCube._rotateU()
            fakeCube._rotateR()
            fakeCube._rotateU()
            fakeCube._rotater()
            fakeCube._rotateU()
            fakeCube._rotateR()
            fakeCube._rotateU()
            fakeCube._rotateU()
            fakeCube._rotater()
  
        elif fishPattern(fakeCube) == "botleft":
            result += "RUrURUUr"
            fakeCube._rotateR()
            fakeCube._rotateU()
            fakeCube._rotater()
            fakeCube._rotateU()
            fakeCube._rotateR()
            fakeCube._rotateU()
            fakeCube._rotateU()
            fakeCube._rotater()
        # **************************************************
        
        # Checks for Double Fish Pattern **************************************************
        elif doubleFishPattern(fakeCube) == "leftdiagonal":
            result += "URUrURUUr"
            fakeCube._rotateU()
            fakeCube._rotateR()
            fakeCube._rotateU()
            fakeCube._rotater()
            fakeCube._rotateU()
            fakeCube._rotateR()
            fakeCube._rotateU()
            fakeCube._rotateU()
            fakeCube._rotater()
 
        elif doubleFishPattern(fakeCube) == "rightdiagonal":
            result += "RUrURUUr"
            fakeCube._rotateR()
            fakeCube._rotateU()
            fakeCube._rotater()
            fakeCube._rotateU()
            fakeCube._rotateR()
            fakeCube._rotateU()
            fakeCube._rotateU()
            fakeCube._rotater() 
        # **************************************************
        
        #if we come across cross pattern with no left facing yellow tile
        else: 
            result += "RUrURUUr"
            fakeCube._rotateR()
            fakeCube._rotateU()
            fakeCube._rotater()
            fakeCube._rotateU()
            fakeCube._rotateR()
            fakeCube._rotateU()
            fakeCube._rotateU()
            fakeCube._rotater()   
    return result







# Local Methods to check for different patterns

def crossPattern(fakeCube):
    if (fakeCube.get()[37] == fakeCube.get()[40] and fakeCube.get()[39] == fakeCube.get()[40] and fakeCube.get()[41] == fakeCube.get()[40] and fakeCube.get()[43] == fakeCube.get()[40] and fakeCube.get()[36] != fakeCube.get()[40] and fakeCube.get()[38] != fakeCube.get()[40] and fakeCube.get()[42] != fakeCube.get()[40] and fakeCube.get()[44] != fakeCube.get()[40]):
        return True
    return False
def hasUpperFacePattern(fakeCube):
    if (fakeCube.get()[36] == fakeCube.get()[40] and fakeCube.get()[37] == fakeCube.get()[40] and fakeCube.get()[38] == fakeCube.get()[40] and  fakeCube.get()[39] == fakeCube.get()[40] and fakeCube.get()[41] == fakeCube.get()[40] and  fakeCube.get()[42] == fakeCube.get()[40] and fakeCube.get()[43] == fakeCube.get()[40] and fakeCube.get()[44] == fakeCube.get()[40]):
        return True
    return False
def fishPattern(fakeCube):
    if(fakeCube.get()[37] == fakeCube.get()[40] and fakeCube.get()[39] == fakeCube.get()[40] and fakeCube.get()[41] == fakeCube.get()[40] and fakeCube.get()[43] == fakeCube.get()[40] and fakeCube.get()[36] == fakeCube.get()[40] and fakeCube.get()[38] != fakeCube.get()[40] and fakeCube.get()[42] != fakeCube.get()[40] and fakeCube.get()[44] != fakeCube.get()[40]):
        return "topleft"
    elif(fakeCube.get()[37] == fakeCube.get()[40] and fakeCube.get()[39] == fakeCube.get()[40] and fakeCube.get()[41] == fakeCube.get()[40] and fakeCube.get()[43] == fakeCube.get()[40] and fakeCube.get()[38] == fakeCube.get()[40] and fakeCube.get()[36] != fakeCube.get()[40] and fakeCube.get()[42] != fakeCube.get()[40] and fakeCube.get()[44] != fakeCube.get()[40]):
        return "topright"
    elif(fakeCube.get()[37] == fakeCube.get()[40] and fakeCube.get()[39] == fakeCube.get()[40] and fakeCube.get()[41] == fakeCube.get()[40] and fakeCube.get()[43] == fakeCube.get()[40] and fakeCube.get()[44] == fakeCube.get()[40] and fakeCube.get()[36] != fakeCube.get()[40] and fakeCube.get()[38] != fakeCube.get()[40] and fakeCube.get()[42] != fakeCube.get()[40]):
        return "botright"
    elif(fakeCube.get()[37] == fakeCube.get()[40] and fakeCube.get()[39] == fakeCube.get()[40] and fakeCube.get()[41] == fakeCube.get()[40] and fakeCube.get()[43] == fakeCube.get()[40] and fakeCube.get()[42] == fakeCube.get()[40] and fakeCube.get()[36] != fakeCube.get()[40] and fakeCube.get()[38] != fakeCube.get()[40] and fakeCube.get()[44] != fakeCube.get()[40]):
        return "botleft"
    else:
        return "None"
    
def treePattern(fakeCube):
    if(fakeCube.get()[37] == fakeCube.get()[40] and fakeCube.get()[39] == fakeCube.get()[40] and fakeCube.get()[41] == fakeCube.get()[40] and fakeCube.get()[43] == fakeCube.get()[40] and fakeCube.get()[36] == fakeCube.get()[40] and fakeCube.get()[38] == fakeCube.get()[40]):
        return "up"
    elif(fakeCube.get()[37] == fakeCube.get()[40] and fakeCube.get()[39] == fakeCube.get()[40] and fakeCube.get()[41] == fakeCube.get()[40] and fakeCube.get()[43] == fakeCube.get()[40] and fakeCube.get()[42] == fakeCube.get()[40] and fakeCube.get()[44] == fakeCube.get()[40]):
        return "down"
    elif(fakeCube.get()[37] == fakeCube.get()[40] and fakeCube.get()[39] == fakeCube.get()[40] and fakeCube.get()[41] == fakeCube.get()[40] and fakeCube.get()[43] == fakeCube.get()[40] and fakeCube.get()[36] == fakeCube.get()[40] and fakeCube.get()[42] == fakeCube.get()[40]):
        return "left"
    elif(fakeCube.get()[37] == fakeCube.get()[40] and fakeCube.get()[39] == fakeCube.get()[40] and fakeCube.get()[41] == fakeCube.get()[40] and fakeCube.get()[43] == fakeCube.get()[40] and fakeCube.get()[44] == fakeCube.get()[40] and fakeCube.get()[38] == fakeCube.get()[40]):
        return "right"
    else:
        return "None"
    
def doubleFishPattern(fakeCube):
    if (fakeCube.get()[37] == fakeCube.get()[40] and fakeCube.get()[39] == fakeCube.get()[40] and fakeCube.get()[41] == fakeCube.get()[40] and fakeCube.get()[43] == fakeCube.get()[40] and fakeCube.get()[36] == fakeCube.get()[40] and fakeCube.get()[44] == fakeCube.get()[40] and fakeCube.get()[38] != fakeCube.get()[40] and fakeCube.get()[42] != fakeCube.get()[40]):
        return "leftdiagonal"
    elif(fakeCube.get()[37] == fakeCube.get()[40] and fakeCube.get()[39] == fakeCube.get()[40] and fakeCube.get()[41] == fakeCube.get()[40] and fakeCube.get()[43] == fakeCube.get()[40] and fakeCube.get()[38] == fakeCube.get()[40] and fakeCube.get()[42] == fakeCube.get()[40] and fakeCube.get()[36] != fakeCube.get()[40] and fakeCube.get()[44] != fakeCube.get()[40]):
        return "rightdiagonal"
