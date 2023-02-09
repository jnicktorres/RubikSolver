from rubik.model.cube import Cube

def rotate(parms):
    """Return rotated cube""" 
    result = {}

    encodedCube = parms.get('cube')
    theCube = Cube(encodedCube)




    
########### This part of the code is used to validate that cube is has correct colors and directions    ######

    result['cube'] = theCube.get()
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
        
        #Checks centers to see if they are unique
        for num in centers:
            if theCube.get()[num] not in checkCenter.keys():
                checkCenter[theCube.get()[num]] = 1
                
        if len(checkCenter) != 6:
            result['status'] = 'error: 123' 
            return result['status']     
     
     
    #part to validate cube directions
    dirs = ['F','f','R','r', 'B','b', 'L','l','U','u']               
    directions = parms.get('dir')
    
    if directions == None:
        #if directions are missing then set to F
        directions = 'F'
         
    else:       
        #iterate through directions and see if they are valid
        for i in directions:
            if i not in dirs:
                result['status'] = 'error: 123' 
                return result['status']     
    
   
#######################################################################################################   
 
    result['status'] = 'ok' 
    result['cube'] = theCube.rotate(directions)
    
                        
    return result