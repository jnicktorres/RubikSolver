import rubik.model.constants
from rubik.model.cube import Cube

def solveBottomLayer(theCube: Cube) -> str:
    '''
        This is the top-level function  for rotating
        a cube so that the bottom layer is solved.
        
        input:  an instance of the cube class with the down-face cross solved
        output: the rotations required to solve the bottom layer  
    '''   
    #### Variables  
    inputCube = theCube
    matchcol = inputCube.get()[49] # color to be matched
    centers = [4,13,22,31]
    rightcorn = [2,11, 20,29]
    leftcorn = [0,9, 18,27]
    topcorn = [36,38,42,44]
    result = ''
    
    
    
    ## start
    
    for _ in range(0,4):
        
    ################## if white tiles are on bottom layer or white tile on bottom is wrong then move ########################################
        if (matchcol in inputCube.get()[6] or matchcol in inputCube.get()[35]) or (matchcol == inputCube.get()[45] and inputCube.get()[6] != inputCube.get()[4]):
            inputCube._rotatel()
            inputCube._rotateu()
            inputCube._rotateL()
            result += 'luL'
            
               
        elif (matchcol in inputCube.get()[33] or matchcol in inputCube.get()[26]) or (matchcol == inputCube.get()[51] and inputCube.get()[33] != inputCube.get()[31]):
            inputCube._rotateb()
            inputCube._rotateu()
            inputCube._rotateB()
            result += 'buB'
        elif  (matchcol in inputCube.get()[8] or matchcol in inputCube.get()[15]) or (matchcol == inputCube.get()[47] and inputCube.get()[15] != inputCube.get()[13]):
            inputCube._rotatef()
            inputCube._rotateu()
            inputCube._rotateF()
            result += 'fuF'
               
        elif  (matchcol in inputCube.get()[17] or matchcol in inputCube.get()[24]) or (matchcol == inputCube.get()[53] and inputCube.get()[24] != inputCube.get()[22]):
            inputCube._rotater()
            inputCube._rotateu()
            inputCube._rotateR()
            result += 'ruR'
        
             
        ################## if white tiles are on top then move to middle of cube ########################################    
        for tile in topcorn:
            if inputCube.get()[tile] == matchcol:
                for _ in range(0,4):     
                    if inputCube.get()[36] == matchcol and inputCube.get()[51] != matchcol:
                        result += 'Lul'
                        inputCube._rotateL()
                        inputCube._rotateu()
                        inputCube._rotatel()
                    elif inputCube.get()[38] == matchcol and inputCube.get()[53] != matchcol:
                        result += 'Bub'
                        inputCube._rotateB()
                        inputCube._rotateu()
                        inputCube._rotateb()    
                    elif inputCube.get()[42] == matchcol and inputCube.get()[45] != matchcol:
                        result += 'Fuf'
                        inputCube._rotateF()
                        inputCube._rotateu()
                        inputCube._rotatef()
                    elif inputCube.get()[44] == matchcol and inputCube.get()[47] != matchcol:
                        result += 'Rur'
                        inputCube._rotateR()
                        inputCube._rotateu()
                        inputCube._rotater()         
                    else:
                        result += 'U'
                        inputCube._rotateU()
                break
        
        ############################### Move Left Corner Tiles #################################################  
            
        for tile in leftcorn:      
            if inputCube.get()[tile] == matchcol:
                #finding opposite corner of white corner
                if tile == 0:
                    temp = inputCube.get()[29]
                    for c in centers:
                        if(inputCube.get()[c] == temp and c == 4):                    
                            inputCube._rotateu()
                            inputCube._rotateR()
                            inputCube._rotateU()
                            inputCube._rotater()               
                            result += 'uRUr'
                            break    
                        elif(inputCube.get()[c] == temp and c == 31):
                            inputCube._rotateF()
                            inputCube._rotateU()
                            inputCube._rotatef()
                            result += 'FUf'
                            break                      
                        elif(inputCube.get()[c] == temp and c == 13):
                            inputCube._rotateu()
                            inputCube._rotateu()
                            inputCube._rotateB()
                            inputCube._rotateU()
                            inputCube._rotateb()
                            result += 'uuBUb'
                            break        
                        elif(inputCube.get()[c] == temp and c == 22):
                            inputCube._rotateU()
                            inputCube._rotateL()
                            inputCube._rotateU()
                            inputCube._rotatel()
                            result += 'ULUl'
                            break
                            
                elif tile == 27:
                    
                    temp = inputCube.get()[20]
                    for c in centers:
                        if(inputCube.get()[c] == temp and c == 4):                    
                            inputCube._rotateu()
                            inputCube._rotateu()
                            inputCube._rotateR()
                            inputCube._rotateU()
                            inputCube._rotater()               
                            result += 'uuRUr'
                            break    
                        elif(inputCube.get()[c] == temp and c == 31):
                            inputCube._rotateu()
                            inputCube._rotateF()
                            inputCube._rotateU()
                            inputCube._rotatef()
                            result += 'uFUf'
                            break        
                                    
                        elif(inputCube.get()[c] == temp and c == 13):
                            inputCube._rotateU()
                            inputCube._rotateB()
                            inputCube._rotateU()
                            inputCube._rotateb()
                            result += 'UBUb'
                            break
                                
                        elif(inputCube.get()[c] == temp and c == 22):
                            inputCube._rotateL()
                            inputCube._rotateU()
                            inputCube._rotatel()
                            result += 'LUl'
                            break 
                            
                elif tile == 18:
                            
                    temp = inputCube.get()[11]
                            
                    for c in centers:
                        if(inputCube.get()[c] == temp and c == 4):                    
                            inputCube._rotateU()
                            inputCube._rotateR()
                            inputCube._rotateU()
                            inputCube._rotater()               
                            result += 'URUr'
                            break    
                        elif(inputCube.get()[c] == temp and c == 31):
                            inputCube._rotateu()
                            inputCube._rotateu()
                            inputCube._rotateF()
                            inputCube._rotateU()
                            inputCube._rotatef()
                            result += 'uuFUf'
                            break        
                                    
                        elif(inputCube.get()[c] == temp and c == 13):
                            inputCube._rotateB()
                            inputCube._rotateU()
                            inputCube._rotateb()
                            result += 'BUb'
                            break        
                        elif(inputCube.get()[c] == temp and c == 22):
                                
                            inputCube._rotateu()                            
                            inputCube._rotateL()
                            inputCube._rotateU()
                            inputCube._rotatel()
                            result += 'uLUl'
            
                            break
                else:
                            
                    temp = inputCube.get()[2]
                             
                    for c in centers:
                        if(inputCube.get()[c] == temp and c == 4):                    
                            inputCube._rotateR()
                            inputCube._rotateU()
                            inputCube._rotater()               
                            result += 'RUr'
                            break
                                
                        elif(inputCube.get()[c] == temp and c == 31):
                            inputCube._rotateU()
                            inputCube._rotateF()
                            inputCube._rotateU()
                            inputCube._rotatef()
                            result += 'UFUf'
                            break        
                                    
                        elif(inputCube.get()[c] == temp and c == 13):
                            inputCube._rotateu()   
                            inputCube._rotateB()
                            inputCube._rotateU()
                            inputCube._rotateb()
                            result += 'uBUb'
                            break        
                        elif(inputCube.get()[c] == temp and c == 22):
                            inputCube._rotateu()
                            inputCube._rotateu()                              
                            inputCube._rotateL()
                            inputCube._rotateU()
                            inputCube._rotatel()
                            result += 'uuLUl'
                            break            
                break
        
        ################## Move Right Corner Tiles######################################## 
            
        for tile in rightcorn:            #finding opposite corner of white corner
            if inputCube.get()[tile] == matchcol:
                if tile == 2:
                    temp = inputCube.get()[9]
                    for c in centers:
                        if(inputCube.get()[c] == temp and c == 4):                    
                            inputCube._rotateU()
                            inputCube._rotatel()
                            inputCube._rotateu()
                            inputCube._rotateL()               
                            result += 'UluL'
                            break
                                
                        elif(inputCube.get()[c] == temp and c == 13):
                            inputCube._rotatef()
                            inputCube._rotateu()
                            inputCube._rotateF()
                            result += 'fuF'
                            break        
                                    
                        elif(inputCube.get()[c] == temp and c == 22):
                            inputCube._rotateu()
                            inputCube._rotater()
                            inputCube._rotateu()
                            inputCube._rotateR()
                            result += 'uruR'
                            break        
                        elif(inputCube.get()[c] == temp and c == 31):
                            inputCube._rotateU()
                            inputCube._rotateU()
                            inputCube._rotateb()
                            inputCube._rotateu()
                            inputCube._rotateB()
                            result += 'UUbuB'
                            break
                            
                elif tile == 11:                   
                    temp = inputCube.get()[18]
                    for c in centers:
                        if(inputCube.get()[c] == temp and c == 4):
                            inputCube._rotateU()
                            inputCube._rotateU()                    
                            inputCube._rotatel()
                            inputCube._rotateu()
                            inputCube._rotateL()               
                            result += 'UUluL'
                            break    
                        elif(inputCube.get()[c] == temp and c == 13):
                            inputCube._rotateU()
                            inputCube._rotatef()
                            inputCube._rotateu()
                            inputCube._rotateF()
                            result += 'UfuF'
                            break        
                                    
                        elif(inputCube.get()[c] == temp and c == 22):
                            inputCube._rotater()
                            inputCube._rotateu()
                            inputCube._rotateR()
                            result += 'ruR'
                            break
                                    
                        elif(inputCube.get()[c] == temp and c == 31):
                            inputCube._rotateu()
                            inputCube._rotateb()
                            inputCube._rotateu()
                            inputCube._rotateB()
                            result += 'ubuB'
                            break
                             
                            
                elif tile == 20:
                            
                    temp = inputCube.get()[27]
                            
                    for c in centers:
                        if(inputCube.get()[c] == temp and c == 4):
                            inputCube._rotateu()                   
                            inputCube._rotatel()
                            inputCube._rotateu()
                            inputCube._rotateL()               
                            result += 'uluL'
                            break
                            
                        elif(inputCube.get()[c] == temp and c == 13):
                            inputCube._rotateU()
                            inputCube._rotateU()
                            inputCube._rotatef()
                            inputCube._rotateu()
                            inputCube._rotateF()
                            result += 'UUfuF'
                            break        
                                    
                        elif(inputCube.get()[c] == temp and c == 22):
                            inputCube._rotateU()
                            inputCube._rotater()
                            inputCube._rotateu()
                            inputCube._rotateR()
                            result += 'UruR'
                            break
                                
                        elif(inputCube.get()[c] == temp and c == 31):
                            inputCube._rotateb()
                            inputCube._rotateu()
                            inputCube._rotateB()
                            result += 'buB'
                            break
                else:
                    temp = inputCube.get()[0]
                    for c in centers:     
                        if(inputCube.get()[c] == temp and c == 4):                 
                            inputCube._rotatel()
                            inputCube._rotateu()
                            inputCube._rotateL()               
                            result += 'luL'
                            break            
                        elif(inputCube.get()[c] == temp and c == 13):
                            inputCube._rotateu()
                            inputCube._rotatef()
                            inputCube._rotateu()
                            inputCube._rotateF()
                            result += 'ufuF'
                            break            
                                        
                        elif(inputCube.get()[c] == temp and c == 22):
                            inputCube._rotateU()
                            inputCube._rotateU()
                            inputCube._rotater()
                            inputCube._rotateu()
                            inputCube._rotateR()
                            result += 'UUruR'
                            break
                                    
                        elif(inputCube.get()[c] == temp and c == 31):
                            inputCube._rotateU()
                            inputCube._rotateb()
                            inputCube._rotateu()
                            inputCube._rotateB()
                            result += 'UbuB'
                            break          
                break
        
       
            
    return result    
        
   
   

