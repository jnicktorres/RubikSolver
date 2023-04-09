import rubik.model.constants
from rubik.model.cube import Cube
from pickle import FALSE
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
    matchcol = inputCube.get()[49] # color to be matched
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
    
    for _ in range(0,4):
        num = 0 #keeps track of amount of times we find an eligible square in the same orientation
        
        #solves middle daisy squares if directly underneath
        for i in underSquares:
            if inputCube.get()[i] == matchcol:
                for _ in range(0, num):
                    inputCube._rotateD()
                    result += 'D'
                    
                while inputCube.get()[43] == matchcol:
                    inputCube._rotateU()
                    result += 'U'
                    
                inputCube._rotateF()
                inputCube._rotateF()
                result += 'FF'
                break
            num+= 1            

             
        num = 0
        
        # finds colors in top row of middle squares
        for i in topMiddleSquares:
            if inputCube.get()[i] == matchcol:
                for _ in range(0, num):
                    inputCube._rotateU()
                    result += 'U'
                inputCube._rotateF() 
                inputCube._rotateu()  
                inputCube._rotateR()    
                result += 'FuR'
            num += 1
        
        num = 0
        
        # finds colors in middle rows of middle squares
        for i in middleSquares:
            if inputCube.get()[i] == matchcol:
                ######  left and right of front face
                if i == 32:
                    while inputCube.get()[43] == matchcol:
                        inputCube._rotateU()
                        result += 'U'
                    inputCube._rotateF()
                    result += 'F'
                    
                elif i == 12:
                    while inputCube.get()[43] == matchcol:
                        inputCube._rotateU()
                        result += 'U'
                    inputCube._rotatef()
                    result += 'f'
                
                ###### left and right of front of left face                     
                elif i == 5:
                    while inputCube.get()[41] == matchcol:
                        inputCube._rotateU()
                        result += 'U'
                    inputCube._rotateR()
                    result += 'R' 
                    
                elif i == 21:
                    while inputCube.get()[41] == matchcol:
                        inputCube._rotateU()
                        result += 'U'
                    inputCube._rotater()
                    result += 'r' 
                
                ###### left and right of back of face      
                elif i == 14:
                    while inputCube.get()[37] == matchcol:
                        inputCube._rotateU()
                        result += 'U'
                    inputCube._rotateB()
                    result += 'B'
                    
                elif i == 30: 
                    while inputCube.get()[37] == matchcol:
                        inputCube._rotateU()
                        result += 'U'
                    inputCube._rotateb()
                    result += 'b'
                    
                ###### left and right of back of left face      
                elif i == 23:
                    while inputCube.get()[39] == matchcol:
                        inputCube._rotateU()
                        result += 'U'
                    inputCube._rotateL()
                    result += 'L'
                    
                elif i == 3: 
                    while inputCube.get()[39] == matchcol:
                        inputCube._rotateU()
                        result += 'U'
                    inputCube._rotatel()
                    result += 'l'             
                break  
                  

            # finds colors in bottom row of middle squares
        for i in botMiddleSquares:
            if inputCube.get()[i] == matchcol:
                for _ in range(0, num):
                    inputCube._rotateD()
                    result += 'D'
                
                while inputCube.get()[43] == matchcol:
                    inputCube._rotateU()
                    result += 'U'
                    
                inputCube._rotateF() 
                inputCube._rotateU()  
                inputCube._rotatel()    
                result += 'FUl'
            num += 1    
        ## if we find daisy then break
        if (inputCube.get()[37] == matchcol and inputCube.get()[39] == matchcol and inputCube.get()[41] == matchcol and inputCube.get()[43] == matchcol):
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
