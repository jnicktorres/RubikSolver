from rubik.model.cube import Cube

def rotate(parms):
    """Return rotated cube""" 
    result = {}

    encodedCube = parms.get('cube')
    theCube = Cube(encodedCube)



    result['cube'] = theCube.get()
    checkUnique = {}
    checkCenter = {}
    centers = [4,13,22,31,40,49]
    
    if theCube.get() == 'None': 
        result['status'] = 'error'
        return result
    
    
    if theCube.get() != 'None': 
        
        if len(theCube.get()) != 54 or theCube.get().isalnum() == False:
            result['status'] = 'error'
            return result
               
        #Checks to see if there are no more than 6 unique numbers in string
        for letter in theCube.get():
            if letter not in checkUnique.keys():
                checkUnique[letter] = 1
                
        if len(checkUnique) != 6:
            result['status'] = 'error' 
            return result
        
            
        for num in centers:
            if theCube.get()[num] in checkCenter.keys():
                result['status'] = 'error'
                return result
            else:
                checkCenter[theCube.get()[num]] = 1
                 
        
                
    #directions = parms.get('dir')
    #theCube.rotate(directions)
    
    result['status'] = 'ok'                     
    return result