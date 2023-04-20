import rubik.model.constants
from rubik.model.cube import Cube

def solveMiddleLayer(theCube: Cube) -> str:
    '''
        This is the top-level function  for rotating
        a cube so that the middle layer is solved.
        
        input:  an instance of the cube class with the bottom layer solved
        output: the rotations required to solve the middle layer  
    '''  
    #### Variables  
    inputCube = theCube
    result = ''
    
    ######
    
    for _ in range(0,4):
        
        if(hasMiddle(inputCube) == True):
            return result
        #Check to see if we have any incorrect tiles on right sides, and if we do correct them
    
        if not (inputCube.get()[5] in [inputCube.get()[4], inputCube.get()[40]]) and not (inputCube.get()[12] in [inputCube.get()[13],inputCube.get()[40]]):
            result+= 'URurufUF'
            inputCube.rotate('URurufUF')
              
        if not(inputCube.get()[14] in [inputCube.get()[13],inputCube.get()[40]]) and not (inputCube.get()[21] in [inputCube.get()[22], inputCube.get()[40]]):
            result += 'UBuburUR'
            inputCube.rotate('UBuburUR')
            
        if not (inputCube.get()[23] in [inputCube.get()[22],inputCube.get()[40]]) and not (inputCube.get()[30] in [inputCube.get()[31], inputCube.get()[40]]):
            result += 'ULulubUB'
            inputCube.rotate('ULulubUB')
            
        if not(inputCube.get()[32] in [inputCube.get()[31],inputCube.get()[40]]) and not (inputCube.get()[3] in [inputCube.get()[4],inputCube.get()[40]]):
            result += 'UFufulUL'
            inputCube.rotate('UFufulUL')
        
        #Check to see if we have any incorrect tiles on left sides, and if we do correct them 
        
        if(hasMiddle(inputCube) == True):
            return result
        if not (inputCube.get()[3] in [inputCube.get()[4], inputCube.get()[40]]) and not (inputCube.get()[32] in [inputCube.get()[31],inputCube.get()[40]]):
            result += 'ulULUFuf'
            inputCube.rotate('ulULUFuf')        
              
        if not(inputCube.get()[12] in [inputCube.get()[13],inputCube.get()[40]]) and not (inputCube.get()[5] in [inputCube.get()[4], inputCube.get()[40]]):
            result += 'ufUFURur'
            inputCube.rotate('ufUFURur')  
            
        if not (inputCube.get()[21] in [inputCube.get()[22],inputCube.get()[40]]) and not (inputCube.get()[14] in [inputCube.get()[13], inputCube.get()[40]]):
            result += 'urURUBub'
            inputCube.rotate('urURUBub') 
            
        if not(inputCube.get()[30] in [inputCube.get()[31],inputCube.get()[40]]) and not (inputCube.get()[23] in [inputCube.get()[22],inputCube.get()[40]]):
            result += 'ubUBULul'
            inputCube.rotate('ubUBULul')       
        
        
    ## check to see if we have solved layer after correction
        if(hasMiddle(inputCube) == True):
            return result
            
            
        for _ in range (0,3):
            # Checks to see where we have matching face and top and rotate to move color to the side  of left
            #### Checks Front and left
            if (inputCube.get()[1] == inputCube.get()[4]) and (inputCube.get()[43] == inputCube.get()[31]):
                result += 'ulULUFuf'
                inputCube.rotate('ulULUFuf') 
                
            ####Checks Right and front
            if (inputCube.get()[10] == inputCube.get()[13]) and (inputCube.get()[41] == inputCube.get()[4]):
                result += 'ufUFURur'
                inputCube.rotate('ufUFURur') 
            ####Checks Back and right 
            if (inputCube.get()[19] == inputCube.get()[22]) and (inputCube.get()[37] == inputCube.get()[13]):
                result += 'urURUBub'
                inputCube.rotate('urURUBub') 
            #checks left and back    
            if (inputCube.get()[28] == inputCube.get()[31]) and (inputCube.get()[39] == inputCube.get()[22]):
                result += 'ubUBULul'
                inputCube.rotate('ubUBULul')
                
            ######### check front top and upper bottom side and see if we rotate to right matching tile
            ## Checks front and right
            if (inputCube.get()[1] == inputCube.get()[4]) and (inputCube.get()[43] == inputCube.get()[13]):
                result+= 'URurufUF'
                inputCube.rotate('URurufUF')
            #checks right and back
            if (inputCube.get()[10] == inputCube.get()[13]) and (inputCube.get()[41] == inputCube.get()[22]):
                result += 'UBuburUR'
                inputCube.rotate('UBuburUR')
            #checks back and left
            if (inputCube.get()[19] == inputCube.get()[22]) and (inputCube.get()[37] == inputCube.get()[31]):
                result += 'ULulubUB'
                inputCube.rotate('ULulubUB')
            #checks left and front   
            if (inputCube.get()[28] == inputCube.get()[31]) and (inputCube.get()[39] == inputCube.get()[4]):
                result += 'UFufulUL'
                inputCube.rotate('UFufulUL')  
            result += 'U'
            inputCube._rotateU()
            
           
    return result


def hasMiddle(inputCube):
    #Do a check to see if we already have middle layer
    if(inputCube.get()[45] == inputCube.get()[49] and inputCube.get()[46] == inputCube.get()[49] and inputCube.get()[47] == inputCube.get()[49] and inputCube.get()[48] == inputCube.get()[49] and inputCube.get()[50] == inputCube.get()[49] and inputCube.get()[51] == inputCube.get()[49] and inputCube.get()[52] == inputCube.get()[49] and inputCube.get()[53] == inputCube.get()[49]):
        if(inputCube.get()[3] == inputCube.get()[4] and inputCube.get()[5] == inputCube.get()[4] and inputCube.get()[6] == inputCube.get()[4] and inputCube.get()[7] == inputCube.get()[4] and inputCube.get()[8] == inputCube.get()[4]):
            if(inputCube.get()[12] == inputCube.get()[13] and inputCube.get()[14] == inputCube.get()[13] and inputCube.get()[15] == inputCube.get()[13] and inputCube.get()[16] == inputCube.get()[13] and inputCube.get()[17] == inputCube.get()[13]):
                if(inputCube.get()[21] == inputCube.get()[22] and inputCube.get()[23] == inputCube.get()[22] and inputCube.get()[24] == inputCube.get()[22] and inputCube.get()[25] == inputCube.get()[22] and inputCube.get()[26] == inputCube.get()[22]):
                    if(inputCube.get()[30] == inputCube.get()[31] and inputCube.get()[32] == inputCube.get()[31] and inputCube.get()[33] == inputCube.get()[31] and inputCube.get()[34] == inputCube.get()[31] and inputCube.get()[35] == inputCube.get()[31]):
                        return True
    return False