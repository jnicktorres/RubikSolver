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
    
    fakeCube = theCube
    matchcol = fakeCube.get()[49] # color to be matched
    frontCenterColor = fakeCube.get()[4]
    rightCenterColor = fakeCube.get()[13]
    backCenterColor = fakeCube.get()[22]
    leftCenterColor = fakeCube.get()[31]
    
    result = ""
    dirs1 = [46,48,50,52] # in underneath squares
    dirs2 = [1, 10, 19, 28]# in top row of middle squares
    dirs3 = [32, 12, 5, 21, 14, 30, 23, 3]     # in middle row of middle squares
    dirs4 = [7, 16, 25, 34] # in bottom row of middle squares
    
    ##########################################################
    
    for _ in range(0,4):
        num = 0 #keeps track of amount of times we find an eligible square in the same orientation
        
        #solves middle daisy squares if directly underneath
        for i in dirs1:
            if fakeCube.get()[i] == matchcol:
                for _ in range(0, num):
                    fakeCube._rotateD()
                    result += 'D'
                    
                while fakeCube.get()[43] == matchcol:
                    fakeCube._rotateU()
                    result += 'U'
                    
                fakeCube._rotateF()
                fakeCube._rotateF()
                result += 'FF'
                break
            num+= 1            

             
        num = 0
        
        # finds colors in top row of middle squares
        for i in dirs2:
            if fakeCube.get()[i] == matchcol:
                for _ in range(0, num):
                    fakeCube._rotateU()
                    result += 'U'
                fakeCube._rotateF() 
                fakeCube._rotateu()  
                fakeCube._rotateR()    
                result += 'FuR'
            num += 1
        
        num = 0
        
        # finds colors in middle rows of middle squares
        for i in dirs3:
            if fakeCube.get()[i] == matchcol:
                ######  left and right of front face
                if i == 32:
                    while fakeCube.get()[43] == matchcol:
                        fakeCube._rotateU()
                        result += 'U'
                    fakeCube._rotateF()
                    result += 'F'
                    
                elif i == 12:
                    while fakeCube.get()[43] == matchcol:
                        fakeCube._rotateU()
                        result += 'U'
                    fakeCube._rotatef()
                    result += 'f'
                
                ###### left and right of front of left face                     
                elif i == 5:
                    while fakeCube.get()[41] == matchcol:
                        fakeCube._rotateU()
                        result += 'U'
                    fakeCube._rotateR()
                    result += 'R' 
                    
                elif i == 21:
                    while fakeCube.get()[41] == matchcol:
                        fakeCube._rotateU()
                        result += 'U'
                    fakeCube._rotater()
                    result += 'r' 
                
                ###### left and right of back of face      
                elif i == 14:
                    while fakeCube.get()[37] == matchcol:
                        fakeCube._rotateU()
                        result += 'U'
                    fakeCube._rotateB()
                    result += 'B'
                    
                elif i == 30: 
                    while fakeCube.get()[37] == matchcol:
                        fakeCube._rotateU()
                        result += 'U'
                    fakeCube._rotateb()
                    result += 'b'
                    
                ###### left and right of back of left face      
                elif i == 23:
                    while fakeCube.get()[39] == matchcol:
                        fakeCube._rotateU()
                        result += 'U'
                    fakeCube._rotateL()
                    result += 'L'
                    
                elif i == 3: 
                    while fakeCube.get()[39] == matchcol:
                        fakeCube._rotateU()
                        result += 'U'
                    fakeCube._rotatel()
                    result += 'l'             
                break  
                  

            # finds colors in bottom row of middle squares
        for i in dirs4:
            if fakeCube.get()[i] == matchcol:
                for _ in range(0, num):
                    fakeCube._rotateD()
                    result += 'D'
                
                while fakeCube.get()[43] == matchcol:
                    fakeCube._rotateU()
                    result += 'U'
                    
                fakeCube._rotateF() 
                fakeCube._rotateU()  
                fakeCube._rotatel()    
                result += 'FUl'
            num += 1    
        ## if we find daisy then break
        if (fakeCube.get()[37] == matchcol and fakeCube.get()[39] == matchcol and fakeCube.get()[41] == matchcol and fakeCube.get()[43] == matchcol):
            break
            
        
       
    ###################### FLIP DAISY TO BOTTOM
        
    #flips front face
    while fakeCube.get()[1] != frontCenterColor or fakeCube.get()[43] != matchcol:
        result += 'U'
        fakeCube._rotateU()
    fakeCube._rotateF()
    fakeCube._rotateF()
    result += 'FF'
    
    #flips right face
    while fakeCube.get()[10] != rightCenterColor or fakeCube.get()[41] != matchcol:
        result += 'U'
        fakeCube._rotateU()
    fakeCube._rotateR()
    fakeCube._rotateR()
    result += 'RR' 
    
    #flips back face
    while fakeCube.get()[19] != backCenterColor or fakeCube.get()[37] != matchcol:
        result += 'U'
        fakeCube._rotateU()
    fakeCube._rotateB()
    fakeCube._rotateB()
    result += 'BB'
    
    #flips left face    
    while fakeCube.get()[28] != leftCenterColor or fakeCube.get()[39] != matchcol:
        result += 'U'
        fakeCube._rotateU()
        
    fakeCube._rotateL()
    fakeCube._rotateL()
    result += 'LL'        
    ##############################               
                 
    return result 
