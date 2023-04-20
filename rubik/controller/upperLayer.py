import rubik.model.constants
from rubik.model.cube import Cube

def solveUpperLayer(theCube: Cube) -> str:
    '''
        This is the top-level function  for rotating
        a cube so that the entire upper layer is solved.
        
        input:  an instance of the cube class with up-face surface solved
        output: the rotations required to solve the upper layer  
    '''  
    #### Variables  
    inputCube = theCube
    result = ''
    frontFace = inputCube.get()[4]
    rightFace = inputCube.get()[13]
    backFace = inputCube.get()[22]
    leftFace = inputCube.get()[31]
    currentColor = 4
    ######
    
    
    # Does the Top Corners Method *******************************

    while checkTopCorners(inputCube) == False:
        if inputCube.get()[0] == inputCube.get()[2]:
            
            if inputCube.get()[0] == frontFace:
                result += "fUBuFUbBUbUBUUb"
                inputCube.rotate("fUBuFUbBUbUBUUb") 
                 
            elif inputCube.get()[0] == rightFace:
                result += "urULuRUlLUlULUUl"
                inputCube._rotateu()
                if(checkTopCorners(inputCube) == True):
                    break
                inputCube.rotate("rULuRUlLUlULUUl")  
                     
            elif inputCube.get()[0] == backFace:
                result += 'uubUFuBUfFUfUFUUf'
                inputCube._rotateu() 
                inputCube._rotateu() 
                if(checkTopCorners(inputCube) == True):
                    break
                inputCube.rotate('bUFuBUfFUfUFUUf')
                
            elif inputCube.get()[0] == leftFace:
                result += 'UlURuLUrRUrURUUr'
                inputCube._rotateU() 
                if(checkTopCorners(inputCube) == True):
                    break
                inputCube.rotate("lURuLUrRUrURUUr")
                
        #Solving for Right Face                          
        elif inputCube.get()[9] == inputCube.get()[11]:
            if inputCube.get()[9] == frontFace:
                result += "UfUBuFUbBUbUBUUb"
                inputCube._rotateU() 
                if(checkTopCorners(inputCube) == True):
                    break
                inputCube.rotate("fUBuFUbBUbUBUUb")  
                
            elif inputCube.get()[9] == rightFace:
                result += "rULuRUlLUlULUUl"
                inputCube.rotate("rULuRUlLUlULUUl")  
                
            elif inputCube.get()[9] == backFace:
                result += 'ubUFuBUfFUfUFUUf'
                inputCube._rotateu() 
                if(checkTopCorners(inputCube) == True):
                    break
                inputCube.rotate('bUFuBUfFUfUFUUf')
                
            elif inputCube.get()[9] == leftFace:
                result += 'uulURuLUrRUrURUUr'
                inputCube._rotateu()
                inputCube._rotateu()
                if(checkTopCorners(inputCube) == True):
                    break
                inputCube.rotate("lURuLUrRUrURUUr")
                
        #Solving for Back Face            
        elif inputCube.get()[18] == inputCube.get()[20]:
            if inputCube.get()[18] == frontFace:
                result += "uufUBuFUbBUbUBUUb"
                inputCube._rotateu() 
                inputCube._rotateu() 
                if(checkTopCorners(inputCube) == True):
                    break
                inputCube.rotate("fUBuFUbBUbUBUUb")     
            elif inputCube.get()[18] == rightFace:
                result += 'UrULuRUlLUlULUUl'
                inputCube._rotateU() 
                if(checkTopCorners(inputCube) == True):
                    break  
                inputCube.rotate("rULuRUlLUlULUUl")
                    
            elif inputCube.get()[18] == backFace:
                result += 'bUFuBUfFUfUFUUf'
                inputCube.rotate('bUFuBUfFUfUFUUf')
                 
            elif inputCube.get()[18] == leftFace:
                result += 'ulURuLUrRUrURUUr'
                inputCube._rotateu()
                if(checkTopCorners(inputCube) == True):
                    break
                inputCube.rotate("lURuLUrRUrURUUr")
        
        #Solving for left Face    
        elif inputCube.get()[27] == inputCube.get()[29]:
            if inputCube.get()[27] == frontFace:
                result += "ufUBuFUb"
                inputCube._rotateu() 
                if(checkTopCorners(inputCube) == True):
                    break
                inputCube.rotate("fUBuFUbBUbUBUUb")       
            elif inputCube.get()[27] == rightFace:
                result += "uurULuRUlLUlULUUl"
                inputCube._rotateu()   
                inputCube._rotateu()
                if(checkTopCorners(inputCube) == True):
                    break
                inputCube.rotate("rULuRUlLUlULUUl")      
            elif inputCube.get()[27] == backFace:
                result += 'bUFuBUfFUfUFUUf'
                inputCube._rotateU() 
                if(checkTopCorners(inputCube) == True):
                    break
                inputCube.rotate('bUFuBUfFUfUFUUf')
            elif inputCube.get()[27] == leftFace:
                result += 'lURuLUrRUrURUUr'
                inputCube.rotate("lURuLUrRUrURUUr")
        
        else:
            #if we have no matching pairs of corners, we line up a single corner and rotate
            while(inputCube.get()[2] != inputCube.get()[currentColor]):
                currentColor += 9
                 
            if currentColor == 4:
                result += "fUBuFUbBUbUBUUb"
                inputCube.rotate("fUBuFUbBUbUBUUb") 
                
            elif currentColor == 13:
                result += "rULuRUlLUlULUUl"
                inputCube.rotate("rULuRUlLUlULUUl") 
            
            elif currentColor == 22:
                result += 'bUFuBUfFUfUFUUf'
                inputCube.rotate('bUFuBUfFUfUFUUf')
            else:
                result += 'lURuLUrRUrURUUr'
                inputCube.rotate("lURuLUrRUrURUUr")
    # **********************************        

    # Solve for the Top Layer

    while isFinishedCube(inputCube) != True:
        if checkFullFace(inputCube) == "front":
            result += "BBulRBBrLuBB"
            inputCube.rotate("BBulRBBrLuBB")

        elif checkFullFace(inputCube) == "right":

            result += "LLufBLLbFuLL"
            inputCube.rotate("LLufBLLbFuLL")

        elif checkFullFace(inputCube) == "back":
            result += "FFurLFFlRuFF"
            inputCube.rotate("FFurLFFlRuFF")

        elif checkFullFace(inputCube) == "left":
            result += "RRubFRRfBuRR"
            inputCube.rotate("RRubFRRfBuRR")

        elif checkFullFace(inputCube) == "no face":
            result += "FFurLFFlRuFF"
            inputCube.rotate("FFurLFFlRuFF")

    return result
     
        
def checkTopCorners(inputCube):  
    if(inputCube.get()[0] == inputCube.get()[4] and inputCube.get()[2] == inputCube.get()[4]):
        if(inputCube.get()[9] == inputCube.get()[13] and inputCube.get()[11] == inputCube.get()[13]):
            if(inputCube.get()[18] == inputCube.get()[22] and inputCube.get()[20] == inputCube.get()[22]):
                if(inputCube.get()[27] == inputCube.get()[31] and inputCube.get()[29] == inputCube.get()[31]):
                    return True
    return False

# If we find full face, tell which direction it is
def checkFullFace(inputCube):
    frontFace = inputCube.get()[4]
    rightFace = inputCube.get()[13]
    backFace = inputCube.get()[22]
    leftFace = inputCube.get()[31]
    
    if (inputCube.get()[0] == frontFace and inputCube.get()[1] == frontFace and inputCube.get()[2] == frontFace):
        return "front"
    elif (inputCube.get()[9] == rightFace and inputCube.get()[10] == rightFace and inputCube.get()[11] == rightFace):
        return "right"
    elif (inputCube.get()[18] == backFace and inputCube.get()[19] == backFace and inputCube.get()[20] == backFace):
        return "back"
    elif (inputCube.get()[27] == leftFace and inputCube.get()[28] == leftFace and inputCube.get()[29] == leftFace):
        return "left"

    return "no face"

def isFinishedCube(inputCube):
    if(inputCube.get()[45] == inputCube.get()[49] and inputCube.get()[46] == inputCube.get()[49] and inputCube.get()[47] == inputCube.get()[49] and inputCube.get()[48] == inputCube.get()[49] and inputCube.get()[50] == inputCube.get()[49] and inputCube.get()[51] == inputCube.get()[49] and inputCube.get()[52] == inputCube.get()[49] and inputCube.get()[53] == inputCube.get()[49]):
        if(inputCube.get()[0] == inputCube.get()[4] and inputCube.get()[1] == inputCube.get()[4] and inputCube.get()[2] == inputCube.get()[4]and inputCube.get()[3] == inputCube.get()[4] and inputCube.get()[5] == inputCube.get()[4] and inputCube.get()[6] == inputCube.get()[4] and inputCube.get()[7] == inputCube.get()[4] and inputCube.get()[8] == inputCube.get()[4]):
            if(inputCube.get()[9] == inputCube.get()[13] and inputCube.get()[10] == inputCube.get()[13] and inputCube.get()[11] == inputCube.get()[13] and inputCube.get()[12] == inputCube.get()[13] and inputCube.get()[14] == inputCube.get()[13] and inputCube.get()[15] == inputCube.get()[13] and inputCube.get()[16] == inputCube.get()[13] and inputCube.get()[17] == inputCube.get()[13]):
                if(inputCube.get()[18] == inputCube.get()[22] and inputCube.get()[19] == inputCube.get()[22] and inputCube.get()[20] == inputCube.get()[22] and inputCube.get()[21] == inputCube.get()[22] and inputCube.get()[23] == inputCube.get()[22] and inputCube.get()[24] == inputCube.get()[22] and inputCube.get()[25] == inputCube.get()[22] and inputCube.get()[26] == inputCube.get()[22]):
                    if(inputCube.get()[27] == inputCube.get()[31] and inputCube.get()[28] == inputCube.get()[31] and inputCube.get()[29] == inputCube.get()[31] and inputCube.get()[30] == inputCube.get()[31] and inputCube.get()[32] == inputCube.get()[31] and inputCube.get()[33] == inputCube.get()[31] and inputCube.get()[34] == inputCube.get()[31] and inputCube.get()[35] == inputCube.get()[31]):
                        return True

    

