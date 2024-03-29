from rubik.model.cube import Cube

def rotate(parms):
    """Return rotated cube""" 
    result = {}

    encodedCube = parms.get('cube')
    theCube = Cube(encodedCube)




    
########### This part of the code is used to validate that cube is has correct colors and directions    ######

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
                result['status'] = 'error: Invalid Unique Values' 
                return result
                    
        if len(checkUnique) != 6:
            result['status'] = 'error: Invalid Unique Values' 
            return result
        
        #Checks centers to see if they are unique
        for num in centers:
            if theCube.get()[num] not in checkCenter.keys():
                checkCenter[theCube.get()[num]] = 1
                
        if len(checkCenter) != 6:
            result['status'] = 'error: Not Enough Unique Centers' 
            return result     
     
     
    #part to validate cube directions
    dirs = ['F','f','R','r', 'B','b', 'L','l','U','u']               
    directions = parms.get('dir')
    
    if directions == None or len(directions) == 0:
        #if directions are missing then set to F
        directions = 'F'
         
    else:       
        #iterate through directions and see if they are valid
        for i in directions:
            if i not in dirs:
                result['status'] = 'error: Invalid Directions' 
                return result
    
   
#######################################################################################################   
    
    result['status'] = 'ok' 
    result['cube'] = theCube.rotate(directions)
    
                        
    return result