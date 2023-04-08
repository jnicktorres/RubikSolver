import rubik.model.constants
from rubik.model.cube import Cube

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
    
    
    
    
    return 'U'      #TODO:  remove this stubbed value





  
def crossPattern(fakeCube):
    if (fakeCube.get()[37] == fakeCube.get()[40] and fakeCube.get()[39] == fakeCube.get()[40] and fakeCube.get()[41] == fakeCube.get()[40] and fakeCube.get()[43] == fakeCube.get()[40] and fakeCube.get()[36] != fakeCube.get()[40] and fakeCube.get()[38] != fakeCube.get()[40] and fakeCube.get()[42] != fakeCube.get()[40] and fakeCube.get()[44] == fakeCube.get()[40]):
        return True

def hasUpperFacePattern(fakeCube):
    if (fakeCube.get()[36] == fakeCube.get()[40] and fakeCube.get()[37] == fakeCube.get()[40] and fakeCube.get()[38] == fakeCube.get()[40] and  fakeCube.get()[39] == fakeCube.get()[40] and fakeCube.get()[41] == fakeCube.get()[40] and  fakeCube.get()[42] == fakeCube.get()[40] and fakeCube.get()[43] == fakeCube.get()[40] and fakeCube.get()[44] == fakeCube.get()[40]):
        return True

def fishPattern(fakeCube):
    if(fakeCube.get()[37] == fakeCube.get()[40] and fakeCube.get()[39] == fakeCube.get()[40] and fakeCube.get()[41] == fakeCube.get()[40] and fakeCube.get()[43] == fakeCube.get()[40] and fakeCube.get()[36] == fakeCube.get()[40]):
        return "topleft"
    elif(fakeCube.get()[37] == fakeCube.get()[40] and fakeCube.get()[39] == fakeCube.get()[40] and fakeCube.get()[41] == fakeCube.get()[40] and fakeCube.get()[43] == fakeCube.get()[40] and fakeCube.get()[38] == fakeCube.get()[40]):
        return "topright"
    elif(fakeCube.get()[37] == fakeCube.get()[40] and fakeCube.get()[39] == fakeCube.get()[40] and fakeCube.get()[41] == fakeCube.get()[40] and fakeCube.get()[43] == fakeCube.get()[40] and fakeCube.get()[44] == fakeCube.get()[40]):
        return "botright"
    elif(fakeCube.get()[37] == fakeCube.get()[40] and fakeCube.get()[39] == fakeCube.get()[40] and fakeCube.get()[41] == fakeCube.get()[40] and fakeCube.get()[43] == fakeCube.get()[40] and fakeCube.get()[42] == fakeCube.get()[40]):
        return "botleft"
    else:
        return "None"
    


