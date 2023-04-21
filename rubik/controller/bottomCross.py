from rubik.model.constants import *
from rubik.model.cube import Cube
from pickle import FALSE, TRUE
from re import match

def solveBottomCross(theCube: Cube) -> str:
    '''
        This is the top-level function  for rotating
        a cube into the down-face cross configuration.
        
        input:  an instance of the cube class
        output: the rotations required to transform the input cube into the down-face cross 
    '''
    
    #### Variables
    
    inputCube = theCube
    matchcol = inputCube.get()[DMM] # color to be matched which is the bottom
    frontCenterColor = inputCube.get()[FMM]
    rightCenterColor = inputCube.get()[RMM]
    backCenterColor = inputCube.get()[BMM]
    leftCenterColor = inputCube.get()[LMM]
    result = ""
    underSquares = [DTM,DML,DMR,DBM] # in underneath squares
    topMiddleSquares = [FTM, RTM, BTM, LTM]# in top row of middle squares
    middleSquares = [LMR, RML, FMR, BML, RMR, LML, BMR, FML]     # in middle row of middle squares
    botMiddleSquares = [FBM, RBM, BBM, LBM] # in bottom row of middle squares
    
    
    ##########################################################
    
    while hasDaisyOnTop(inputCube,matchcol) == False:
        
        if hasDaisyOnTop(inputCube,matchcol) == True:
            break

        #Checks under squares for white tiles, if we find then flip to top
        for tile in underSquares:
            if inputCube.get()[tile] == matchcol and hasDaisyOnTop(inputCube,matchcol) == False:                
                if tile == DTM:
                    while inputCube.get()[UBM] == matchcol:
                        inputCube._rotateU()
                        result += 'U'
                    inputCube.rotate('FF')
                    result += 'FF'
                    break
                elif tile == DMR:
                    while inputCube.get()[UMR] == matchcol:
                        inputCube._rotateU()
                        result += 'U'
                    inputCube.rotate('RR')
                    result += 'RR'
                    break
                elif tile == DBM:
                    while inputCube.get()[UTM] == matchcol:
                        inputCube._rotateU()
                        result += 'U'
                    inputCube.rotate('BB')
                    result += 'BB'
                    break
                    
                elif tile == DML:
                    while inputCube.get()[UML] == matchcol:
                        inputCube._rotateU()
                        result += 'U'
                    inputCube.rotate('LL')
                    result += 'LL'
                    break
             
        currentIterations = 0     #Keeps track of how many rotations is needed for up
        if hasDaisyOnTop(inputCube,matchcol) == True:
            break
        
        # finds white tiles in top row of middle squares
        for tile in topMiddleSquares:
            if inputCube.get()[tile] == matchcol:
                for _ in range(0, currentIterations):
                    inputCube._rotateU()
                    result += 'U'
                inputCube.rotate('FuR')
                result += 'FuR'
            currentIterations += 1
        
        currentIterations = 0
        if hasDaisyOnTop(inputCube,matchcol) == True:
            break
        
        # finds white tiles in middle rows of middle squares
        for tile in middleSquares:
            if inputCube.get()[tile] == matchcol:
                ######  left and right of front face
                if tile == LMR:
                    while inputCube.get()[UBM] == matchcol:
                        inputCube._rotateU()
                        result += 'U'
                    inputCube._rotateF()
                    result += 'F'
                    
                elif tile == RML:
                    while inputCube.get()[UBM] == matchcol:
                        inputCube._rotateU()
                        result += 'U'
                    inputCube._rotatef()
                    result += 'f'
                
                ###### left and right of front of left face                     
                elif tile == FMR:
                    while inputCube.get()[UMR] == matchcol:
                        inputCube._rotateU()
                        result += 'U'
                    inputCube._rotateR()
                    result += 'R' 
                    
                elif tile == BML:
                    while inputCube.get()[UMR] == matchcol:
                        inputCube._rotateU()
                        result += 'U'
                    inputCube._rotater()
                    result += 'r' 
                
                ###### left and right of back of face      
                elif tile == RMR:
                    while inputCube.get()[UTM] == matchcol:
                        inputCube._rotateU()
                        result += 'U'
                    inputCube._rotateB()
                    result += 'B'
                    
                elif tile == LML: 
                    while inputCube.get()[UTM] == matchcol:
                        inputCube._rotateU()
                        result += 'U'
                    inputCube._rotateb()
                    result += 'b'
                    
                ###### left and right of back of left face      
                elif tile == BMR:
                    while inputCube.get()[UML] == matchcol:
                        inputCube._rotateU()
                        result += 'U'
                    inputCube._rotateL()
                    result += 'L'
                    
                elif tile == FML: 
                    while inputCube.get()[UML] == matchcol:
                        inputCube._rotateU()
                        result += 'U'
                    inputCube._rotatel()
                    result += 'l'             
                break  
                  

        if hasDaisyOnTop(inputCube,matchcol) == True:
            break    
        
        #Finds tiles in bottom middle squares for white squares
        for tile in botMiddleSquares:
            if inputCube.get()[tile] == matchcol and hasDaisyOnTop(inputCube,matchcol) == False:
                if tile == FBM: 
                    while inputCube.get()[UBM] == matchcol:
                        inputCube._rotateU()
                        result += 'U'
                        
                    inputCube.rotate('FUl')     
                    result += 'FUl'
                    
                elif tile == RBM: 
                    while inputCube.get()[UMR] == matchcol:
                        inputCube._rotateU()
                        result += 'U'
                        
                    inputCube.rotate('RUf')   
                    result += 'RUf'    
                    
                elif tile == BBM: 
                    while inputCube.get()[UTM] == matchcol:
                        inputCube._rotateU()
                        result += 'U'
                    inputCube.rotate('BUr')   
                    result += 'BUr' 
                    
                elif tile == LBM: 
                    while inputCube.get()[UML] == matchcol:
                        inputCube._rotateU()
                        result += 'U'
                    inputCube.rotate('LUb') 
                    result += 'LUb' 
                
                      
        ## if we find daisy then break
        if hasDaisyOnTop(inputCube,matchcol) == True:
            break
            
        
       
    ###################### FLIP DAISY TO BOTTOM
        
    #flips front face
    while inputCube.get()[FTM] != frontCenterColor or inputCube.get()[UBM] != matchcol:
        result += 'U'
        inputCube._rotateU()
    inputCube._rotateF()
    inputCube._rotateF()
    result += 'FF'
    
    #flips right face
    while inputCube.get()[RTM] != rightCenterColor or inputCube.get()[UMR] != matchcol:
        result += 'U'
        inputCube._rotateU()
    inputCube._rotateR()
    inputCube._rotateR()
    result += 'RR' 
    
    #flips back face
    while inputCube.get()[BTM] != backCenterColor or inputCube.get()[UTM] != matchcol:
        result += 'U'
        inputCube._rotateU()
    inputCube._rotateB()
    inputCube._rotateB()
    result += 'BB'
    
    #flips left face    
    while inputCube.get()[LTM] != leftCenterColor or inputCube.get()[UML] != matchcol:
        result += 'U'
        inputCube._rotateU()
        
    inputCube._rotateL()
    inputCube._rotateL()
    result += 'LL'        
    ##############################               
                 
    return result 



def hasDaisyOnTop(inputCube,matchcol):
    if (inputCube.get()[UTM] == matchcol and inputCube.get()[UML] == matchcol and inputCube.get()[UMR] == matchcol and inputCube.get()[UBM] == matchcol):
        return True
    return False