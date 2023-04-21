from rubik.model.constants import *
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
    
    ######  Iterate 4 times since thats how many times we have to rotate for a complete circle
    
    for _ in range(0,4):
        
        if(hasMiddle(inputCube) == True):
            return result
        #Check to see if we have any incorrect tiles on right sides, and if we do correct them
    
        if not (inputCube.get()[FMR] in [inputCube.get()[FMM], inputCube.get()[UMM]]) and not (inputCube.get()[RML] in [inputCube.get()[RMM],inputCube.get()[UMM]]):
            result+= 'URurufUF'
            inputCube.rotate('URurufUF')
              
        if not(inputCube.get()[RMR] in [inputCube.get()[RMM],inputCube.get()[UMM]]) and not (inputCube.get()[BML] in [inputCube.get()[BMM], inputCube.get()[UMM]]):
            result += 'UBuburUR'
            inputCube.rotate('UBuburUR')
            
        if not (inputCube.get()[BMR] in [inputCube.get()[BMM],inputCube.get()[UMM]]) and not (inputCube.get()[LML] in [inputCube.get()[LMM], inputCube.get()[UMM]]):
            result += 'ULulubUB'
            inputCube.rotate('ULulubUB')
            
        if not(inputCube.get()[LMR] in [inputCube.get()[LMM],inputCube.get()[UMM]]) and not (inputCube.get()[FML] in [inputCube.get()[FMM],inputCube.get()[UMM]]):
            result += 'UFufulUL'
            inputCube.rotate('UFufulUL')
        
        #Check to see if we have any incorrect tiles on left sides, and if we do correct them 
        
        if(hasMiddle(inputCube) == True):
            return result
        if not (inputCube.get()[FML] in [inputCube.get()[FMM], inputCube.get()[UMM]]) and not (inputCube.get()[LMR] in [inputCube.get()[LMM],inputCube.get()[UMM]]):
            result += 'ulULUFuf'
            inputCube.rotate('ulULUFuf')        
              
        if not(inputCube.get()[RML] in [inputCube.get()[RMM],inputCube.get()[UMM]]) and not (inputCube.get()[FMR] in [inputCube.get()[FMM], inputCube.get()[UMM]]):
            result += 'ufUFURur'
            inputCube.rotate('ufUFURur')  
            
        if not (inputCube.get()[BML] in [inputCube.get()[BMM],inputCube.get()[UMM]]) and not (inputCube.get()[RMR] in [inputCube.get()[RMM], inputCube.get()[UMM]]):
            result += 'urURUBub'
            inputCube.rotate('urURUBub') 
            
        if not(inputCube.get()[LML] in [inputCube.get()[LMM],inputCube.get()[UMM]]) and not (inputCube.get()[BMR] in [inputCube.get()[BMM],inputCube.get()[UMM]]):
            result += 'ubUBULul'
            inputCube.rotate('ubUBULul')       
        
        
    ## check to see if we have solved layer after correction
        if(hasMiddle(inputCube) == True):
            return result
            
            
        for _ in range (0,3):
            # Checks to see where we have matching face and top and rotate to move color to the side  of left
            #### Checks Front and left
            if (inputCube.get()[FTM] == inputCube.get()[FMM]) and (inputCube.get()[UBM] == inputCube.get()[LMM]):
                result += 'ulULUFuf'
                inputCube.rotate('ulULUFuf') 
                
            ####Checks Right and front
            if (inputCube.get()[RTM] == inputCube.get()[RMM]) and (inputCube.get()[UMR] == inputCube.get()[FMM]):
                result += 'ufUFURur'
                inputCube.rotate('ufUFURur') 
            ####Checks Back and right 
            if (inputCube.get()[BTM] == inputCube.get()[BMM]) and (inputCube.get()[UTM] == inputCube.get()[RMM]):
                result += 'urURUBub'
                inputCube.rotate('urURUBub') 
            #checks left and back    
            if (inputCube.get()[LTM] == inputCube.get()[LMM]) and (inputCube.get()[UML] == inputCube.get()[BMM]):
                result += 'ubUBULul'
                inputCube.rotate('ubUBULul')
                
            ######### check front top and upper bottom side and see if we rotate to right matching tile
            ## Checks front and right
            if (inputCube.get()[FTM] == inputCube.get()[FMM]) and (inputCube.get()[UBM] == inputCube.get()[RMM]):
                result+= 'URurufUF'
                inputCube.rotate('URurufUF')
            #checks right and back
            if (inputCube.get()[RTM] == inputCube.get()[RMM]) and (inputCube.get()[UMR] == inputCube.get()[BMM]):
                result += 'UBuburUR'
                inputCube.rotate('UBuburUR')
            #checks back and left
            if (inputCube.get()[BTM] == inputCube.get()[BMM]) and (inputCube.get()[UTM] == inputCube.get()[LMM]):
                result += 'ULulubUB'
                inputCube.rotate('ULulubUB')
            #checks left and front   
            if (inputCube.get()[LTM] == inputCube.get()[LMM]) and (inputCube.get()[UML] == inputCube.get()[FMM]):
                result += 'UFufulUL'
                inputCube.rotate('UFufulUL')  
            result += 'U'
            inputCube._rotateU()
            
           
    return result


def hasMiddle(inputCube):
    #Do a check to see if we already have middle layer
    if(inputCube.get()[DTL] == inputCube.get()[DMM] and inputCube.get()[DTM] == inputCube.get()[DMM] and inputCube.get()[DTR] == inputCube.get()[DMM] and inputCube.get()[DML] == inputCube.get()[DMM] and inputCube.get()[DMR] == inputCube.get()[DMM] and inputCube.get()[DBL] == inputCube.get()[DMM] and inputCube.get()[DBM] == inputCube.get()[DMM] and inputCube.get()[DBR] == inputCube.get()[DMM]):
        if(inputCube.get()[FML] == inputCube.get()[FMM] and inputCube.get()[FMR] == inputCube.get()[FMM] and inputCube.get()[FBL] == inputCube.get()[FMM] and inputCube.get()[FBM] == inputCube.get()[FMM] and inputCube.get()[FBR] == inputCube.get()[FMM]):
            if(inputCube.get()[RML] == inputCube.get()[RMM] and inputCube.get()[RMR] == inputCube.get()[RMM] and inputCube.get()[RBL] == inputCube.get()[RMM] and inputCube.get()[RBM] == inputCube.get()[RMM] and inputCube.get()[RBR] == inputCube.get()[RMM]):
                if(inputCube.get()[BML] == inputCube.get()[BMM] and inputCube.get()[BMR] == inputCube.get()[BMM] and inputCube.get()[BBL] == inputCube.get()[BMM] and inputCube.get()[BBM] == inputCube.get()[BMM] and inputCube.get()[BBR] == inputCube.get()[BMM]):
                    if(inputCube.get()[LML] == inputCube.get()[LMM] and inputCube.get()[LMR] == inputCube.get()[LMM] and inputCube.get()[LBL] == inputCube.get()[LMM] and inputCube.get()[LBM] == inputCube.get()[LMM] and inputCube.get()[LBR] == inputCube.get()[LMM]):
                        return True
    return False