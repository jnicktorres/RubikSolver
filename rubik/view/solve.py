from rubik.controller.bottomCross import solveBottomCross
from rubik.controller.bottomLayer import solveBottomLayer
from rubik.controller.middleLayer import solveMiddleLayer
from rubik.controller.upFaceCross import solveUpCross
from rubik.controller.upFaceSurface import solveUpSurface
from rubik.controller.upperLayer import solveUpperLayer
from rubik.model.cube import Cube

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
        result['status'] = 'error: 123'
        return result['status']
    
    if parms.get('cube') != None: 
        
        if len(theCube.get()) != 54 or theCube.get().isalnum() == False:
            result['status'] = 'error: 123'
            return result['status']    
        
        #Checks to see if there are no more than 6 unique numbers in string
        for letter in theCube.get():
            if letter not in checkUnique.keys():
                checkUnique[letter] = 1
            else:
                checkUnique[letter] = checkUnique[letter] + 1
        
        for key in checkUnique:
            if checkUnique[key] != 9:
                result['status'] = 'error: 123' 
                return result['status']
                    
        if len(checkUnique) != 6:
            result['status'] = 'error: 123' 
            return result['status']
        
        for num in centers:
            if theCube.get()[num] not in checkCenter.keys():
                checkCenter[theCube.get()[num]] = 1
                
        if len(checkCenter) != 6:
            result['status'] = 'error: 123' 
            return result['status']
        
#################################################################################################       
    rotations = ""
    rotations += solveBottomCross(theCube)      #iteration 2
    # rotations += solveBottomLayer(theCube)      #iteration 3
    # rotations += solveMiddleLayer(theCube)      #iteration 4
    # rotations += solveUpCross(theCube)          #iteration 5
    # rotations += solveUpSurface(theCube)        #iteration 5
    # rotations += solveUpperLayer(theCube)       #iteration 6
    
    result['solution'] = rotations
    result['status'] = 'ok'  
    result['integrity'] = ''                    #iteration 3
                     
    return result