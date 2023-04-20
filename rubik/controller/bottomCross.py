import rubik.model.constants
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
    matchcol = inputCube.get()[49] # color to be matched which is the bottom
    frontCenterColor = inputCube.get()[4]
    rightCenterColor = inputCube.get()[13]
    backCenterColor = inputCube.get()[22]
    leftCenterColor = inputCube.get()[31]
    result = ""
    underSquares = [46,48,50,52] # in underneath squares
    topMiddleSquares = [1, 10, 19, 28]# in top row of middle squares
    middleSquares = [32, 12, 5, 21, 14, 30, 23, 3]     # in middle row of middle squares
    botMiddleSquares = [7, 16, 25, 34] # in bottom row of middle squares
    
    
    ##########################################################
    
    while hasDaisyOnTop(inputCube,matchcol) == False:
        
        if hasDaisyOnTop(inputCube,matchcol) == True:
            break

        #Checks under squares for white tiles, if we find then flip to top
        for tile in underSquares:
            if inputCube.get()[tile] == matchcol and hasDaisyOnTop(inputCube,matchcol) == False:                
                if tile == 46:
                    while inputCube.get()[43] == matchcol:
                        inputCube._rotateU()
                        result += 'U'
                    inputCube.rotate('FF')
                    result += 'FF'
                    break
                elif tile == 50:
                    while inputCube.get()[41] == matchcol:
                        inputCube._rotateU()
                        result += 'U'
                    inputCube.rotate('RR')
                    result += 'RR'
                    break
                elif tile == 52:
                    while inputCube.get()[37] == matchcol:
                        inputCube._rotateU()
                        result += 'U'
                    inputCube.rotate('BB')
                    result += 'BB'
                    break
                    
                elif tile == 48:
                    while inputCube.get()[39] == matchcol:
                        inputCube._rotateU()
                        result += 'U'
                    inputCube.rotate('LL')
                    result += 'LL'
                    break
             
        count = 0     #Keeps track of how many rotations is needed for up
        if hasDaisyOnTop(inputCube,matchcol) == True:
            break
        
        # finds white tiles in top row of middle squares
        for tile in topMiddleSquares:
            if inputCube.get()[tile] == matchcol:
                for _ in range(0, count):
                    inputCube._rotateU()
                    result += 'U'
                inputCube.rotate('FuR')
                result += 'FuR'
            count += 1
        
        count = 0
        if hasDaisyOnTop(inputCube,matchcol) == True:
            break
        
        # finds white tiles in middle rows of middle squares
        for tile in middleSquares:
            if inputCube.get()[tile] == matchcol:
                ######  left and right of front face
                if tile == 32:
                    while inputCube.get()[43] == matchcol:
                        inputCube._rotateU()
                        result += 'U'
                    inputCube._rotateF()
                    result += 'F'
                    
                elif tile == 12:
                    while inputCube.get()[43] == matchcol:
                        inputCube._rotateU()
                        result += 'U'
                    inputCube._rotatef()
                    result += 'f'
                
                ###### left and right of front of left face                     
                elif tile == 5:
                    while inputCube.get()[41] == matchcol:
                        inputCube._rotateU()
                        result += 'U'
                    inputCube._rotateR()
                    result += 'R' 
                    
                elif tile == 21:
                    while inputCube.get()[41] == matchcol:
                        inputCube._rotateU()
                        result += 'U'
                    inputCube._rotater()
                    result += 'r' 
                
                ###### left and right of back of face      
                elif tile == 14:
                    while inputCube.get()[37] == matchcol:
                        inputCube._rotateU()
                        result += 'U'
                    inputCube._rotateB()
                    result += 'B'
                    
                elif tile == 30: 
                    while inputCube.get()[37] == matchcol:
                        inputCube._rotateU()
                        result += 'U'
                    inputCube._rotateb()
                    result += 'b'
                    
                ###### left and right of back of left face      
                elif tile == 23:
                    while inputCube.get()[39] == matchcol:
                        inputCube._rotateU()
                        result += 'U'
                    inputCube._rotateL()
                    result += 'L'
                    
                elif tile == 3: 
                    while inputCube.get()[39] == matchcol:
                        inputCube._rotateU()
                        result += 'U'
                    inputCube._rotatel()
                    result += 'l'             
                break  
                  

        if hasDaisyOnTop(inputCube,matchcol) == True:
            break    
        
        #Finds tiles in bot middle squares for white squares
        for tile in botMiddleSquares:
            if inputCube.get()[tile] == matchcol and hasDaisyOnTop(inputCube,matchcol) == False:
                if tile == 7: 
                    while inputCube.get()[43] == matchcol:
                        inputCube._rotateU()
                        result += 'U'
                        
                    inputCube.rotate('FUl')     
                    result += 'FUl'
                    
                elif tile == 16: 
                    while inputCube.get()[41] == matchcol:
                        inputCube._rotateU()
                        result += 'U'
                        
                    inputCube.rotate('RUf')   
                    result += 'RUf'    
                    
                elif tile == 25: 
                    while inputCube.get()[37] == matchcol:
                        inputCube._rotateU()
                        result += 'U'
                    inputCube.rotate('BUr')   
                    result += 'BUr' 
                    
                elif tile == 34: 
                    while inputCube.get()[39] == matchcol:
                        inputCube._rotateU()
                        result += 'U'
                    inputCube.rotate('LUb') 
                    result += 'LUb' 
                
                      
        ## if we find daisy then break
        if hasDaisyOnTop(inputCube,matchcol) == True:
            break
            
        
       
    ###################### FLIP DAISY TO BOTTOM
        
    #flips front face
    while inputCube.get()[1] != frontCenterColor or inputCube.get()[43] != matchcol:
        result += 'U'
        inputCube._rotateU()
    inputCube._rotateF()
    inputCube._rotateF()
    result += 'FF'
    
    #flips right face
    while inputCube.get()[10] != rightCenterColor or inputCube.get()[41] != matchcol:
        result += 'U'
        inputCube._rotateU()
    inputCube._rotateR()
    inputCube._rotateR()
    result += 'RR' 
    
    #flips back face
    while inputCube.get()[19] != backCenterColor or inputCube.get()[37] != matchcol:
        result += 'U'
        inputCube._rotateU()
    inputCube._rotateB()
    inputCube._rotateB()
    result += 'BB'
    
    #flips left face    
    while inputCube.get()[28] != leftCenterColor or inputCube.get()[39] != matchcol:
        result += 'U'
        inputCube._rotateU()
        
    inputCube._rotateL()
    inputCube._rotateL()
    result += 'LL'        
    ##############################               
                 
    return result 



def hasDaisyOnTop(inputCube,matchcol):
    if (inputCube.get()[37] == matchcol and inputCube.get()[39] == matchcol and inputCube.get()[41] == matchcol and inputCube.get()[43] == matchcol):
        return True
    return False