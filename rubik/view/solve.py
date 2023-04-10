from rubik.controller.bottomCross import solveBottomCross
from rubik.controller.bottomLayer import solveBottomLayer
from rubik.controller.middleLayer import solveMiddleLayer
from rubik.controller.upFaceCross import solveUpCross
from rubik.controller.upFaceSurface import solveUpSurface
from rubik.controller.upperLayer import solveUpperLayer
from rubik.view.rotate import rotate
from rubik.model.cube import Cube
import hashlib
import random
from ctypes.wintypes import WORD

def solve(parms):
    """Return rotates needed to solve input cube"""
    result = {}
     
    encodedCube = parms.get('cube')
    theCube = Cube(encodedCube)
    
########### This part of the code is used to validate that cube is has correct colors ######   
   
    checkUnique = {}
    checkCenter = {}
    centers = [4,13,22,31,40,49]
    
    if parms.get('cube') == None: 
        result['status'] = 'error: Empty Cube'
        return result
    
    if parms.get('cube') != None: 
        
        if len(theCube.get()) != 54 or theCube.get().isalnum() == False:
            result['status'] = 'error: Invalid Values in Cube or Invalid Length of Cube'
            return result
        
        #Checks to see if there are no more than 6 unique numbers in string
        for letter in theCube.get():
            if letter not in checkUnique.keys():
                checkUnique[letter] = 1
            else:
                checkUnique[letter] = checkUnique[letter] + 1
        
        for key in checkUnique:
            if checkUnique[key] != 9:
                result['status'] = 'error: Invalid Unique Elements Count' 
                return result
                    
        if len(checkUnique) != 6:
            result['status'] = 'error: Invalid Unique Elements' 
            return result
        
        for num in centers:
            if theCube.get()[num] not in checkCenter.keys():
                checkCenter[theCube.get()[num]] = 1
                
        if len(checkCenter) != 6:
            result['status'] = 'error: Not Enough Unique Centers' 
            return result
#################################################################################################     




    rotations = ""
    rotations += solveBottomCross(theCube)      #iteration 2
    rotations += solveBottomLayer(theCube)      #iteration 3
    rotations += solveMiddleLayer(theCube)      #iteration 4
    rotations += solveUpCross(theCube)          #iteration 5
    rotations += solveUpSurface(theCube)        #iteration 5
    print(theCube.get())
    rotations += solveUpperLayer(theCube)       #iteration 6
    print(theCube.get())
    
    result['solution'] = rotations
    result['status'] = 'ok'    
    
    result['integrity'] = createIntegrityString(theCube,rotations)               #iteration 3
                   
    return result

def createIntegrityString(theCube, rotations):
    wordToToken = theCube.get() + rotations + 'jnt0024'
    sha256Hash = hashlib.sha256()
    sha256Hash.update(wordToToken.encode())
    fullToken = sha256Hash.hexdigest()
    #getting all possible substrings of length 8 from fullToken
    integrityArray = [fullToken[i: j] for i in range(len(fullToken)) for j in range(i + 1, len(fullToken) + 1) if len(fullToken[i:j]) == 8]
    #pick random substring from array 
    randomNum = random.randrange(8)
    return integrityArray[randomNum]
    