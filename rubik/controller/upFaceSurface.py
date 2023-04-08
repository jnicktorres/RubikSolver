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
    print("Start")
    print(fakeCube.get())
    
    
    while hasUpperFacePattern(fakeCube) == False:
        print("inside")
       
        if(hasUpperFacePattern(fakeCube) == True):
            return result
        
        elif crossPattern(fakeCube) == True:
            while(fakeCube.get()[29] != fakeCube.get()[40]):
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
            print("cross")
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
            print("upt")
        elif treePattern(fakeCube) == "right":
            print(fakeCube.get())
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
            print("rightt")
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
            print("downt")
            
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
            print("leftt")
    
    # Find Fish       
    
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
            print("topleftf")
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
            print("toprightf")
            
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
            print("botrightf")
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
            print("botleftf")
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
            print("doublefishleft")
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
            print("doublefishright")   
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
    return result     #TODO:  remove this stubbed value







  
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
