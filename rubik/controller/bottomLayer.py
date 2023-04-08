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
    fakeCube = theCube
    matchcol = fakeCube.get()[49] # color to be matched
    result = ""
    centers = [4,13,22,31]
    rightcorn = [2,11, 20,29]
    leftcorn = [0,9, 18,27]
    topcorn = [36,38,42,44]
    result = ''
    
    
    
    ## start
    
    for _ in range(0,4):
        
    ################## if white tiles are on bottom layer or white tile on bottom is wrong then move ########################################
        if (matchcol in fakeCube.get()[6] or matchcol in fakeCube.get()[35]) or (matchcol == fakeCube.get()[45] and fakeCube.get()[6] != fakeCube.get()[4]):
            fakeCube._rotatel()
            fakeCube._rotateu()
            fakeCube._rotateL()
            result += 'luL'
            
               
        elif (matchcol in fakeCube.get()[33] or matchcol in fakeCube.get()[26]) or (matchcol == fakeCube.get()[51] and fakeCube.get()[33] != fakeCube.get()[31]):
            fakeCube._rotateb()
            fakeCube._rotateu()
            fakeCube._rotateB()
            result += 'buB'
        elif  (matchcol in fakeCube.get()[8] or matchcol in fakeCube.get()[15]) or (matchcol == fakeCube.get()[47] and fakeCube.get()[15] != fakeCube.get()[13]):
            fakeCube._rotatef()
            fakeCube._rotateu()
            fakeCube._rotateF()
            result += 'fuF'
               
        elif  (matchcol in fakeCube.get()[17] or matchcol in fakeCube.get()[24]) or (matchcol == fakeCube.get()[53] and fakeCube.get()[24] != fakeCube.get()[22]):
            fakeCube._rotater()
            fakeCube._rotateu()
            fakeCube._rotateR()
            result += 'ruR'
        
             
        ################## if white tiles are on top then move to middle of cube ########################################    
        for tile in topcorn:
            if fakeCube.get()[tile] == matchcol:
                for _ in range(0,4):     
                    if fakeCube.get()[36] == matchcol and fakeCube.get()[51] != matchcol:
                        result += 'Lul'
                        fakeCube._rotateL()
                        fakeCube._rotateu()
                        fakeCube._rotatel()
                    elif fakeCube.get()[38] == matchcol and fakeCube.get()[53] != matchcol:
                        result += 'Bub'
                        fakeCube._rotateB()
                        fakeCube._rotateu()
                        fakeCube._rotateb()    
                    elif fakeCube.get()[42] == matchcol and fakeCube.get()[45] != matchcol:
                        result += 'Fuf'
                        fakeCube._rotateF()
                        fakeCube._rotateu()
                        fakeCube._rotatef()
                    elif fakeCube.get()[44] == matchcol and fakeCube.get()[47] != matchcol:
                        result += 'Rur'
                        fakeCube._rotateR()
                        fakeCube._rotateu()
                        fakeCube._rotater()         
                    else:
                        result += 'U'
                        fakeCube._rotateU()
                break
        
        ############################### Move Left Corner Tiles #################################################  
            
        for tile in leftcorn:      
            if fakeCube.get()[tile] == matchcol:
                #finding opposite corner of white corner
                if tile == 0:
                    temp = fakeCube.get()[29]
                    for c in centers:
                        if(fakeCube.get()[c] == temp and c == 4):                    
                            fakeCube._rotateu()
                            fakeCube._rotateR()
                            fakeCube._rotateU()
                            fakeCube._rotater()               
                            result += 'uRUr'
                            break    
                        elif(fakeCube.get()[c] == temp and c == 31):
                            fakeCube._rotateF()
                            fakeCube._rotateU()
                            fakeCube._rotatef()
                            result += 'FUf'
                            break                      
                        elif(fakeCube.get()[c] == temp and c == 13):
                            fakeCube._rotateu()
                            fakeCube._rotateu()
                            fakeCube._rotateB()
                            fakeCube._rotateU()
                            fakeCube._rotateb()
                            result += 'uuBUb'
                            break        
                        elif(fakeCube.get()[c] == temp and c == 22):
                            fakeCube._rotateU()
                            fakeCube._rotateL()
                            fakeCube._rotateU()
                            fakeCube._rotatel()
                            result += 'ULUl'
                            break
                            
                elif tile == 27:
                    
                    temp = fakeCube.get()[20]
                    for c in centers:
                        if(fakeCube.get()[c] == temp and c == 4):                    
                            fakeCube._rotateu()
                            fakeCube._rotateu()
                            fakeCube._rotateR()
                            fakeCube._rotateU()
                            fakeCube._rotater()               
                            result += 'uuRUr'
                            break    
                        elif(fakeCube.get()[c] == temp and c == 31):
                            fakeCube._rotateu()
                            fakeCube._rotateF()
                            fakeCube._rotateU()
                            fakeCube._rotatef()
                            result += 'uFUf'
                            break        
                                    
                        elif(fakeCube.get()[c] == temp and c == 13):
                            fakeCube._rotateU()
                            fakeCube._rotateB()
                            fakeCube._rotateU()
                            fakeCube._rotateb()
                            result += 'UBUb'
                            break
                                
                        elif(fakeCube.get()[c] == temp and c == 22):
                            fakeCube._rotateL()
                            fakeCube._rotateU()
                            fakeCube._rotatel()
                            result += 'LUl'
                            break 
                            
                elif tile == 18:
                            
                    temp = fakeCube.get()[11]
                            
                    for c in centers:
                        if(fakeCube.get()[c] == temp and c == 4):                    
                            fakeCube._rotateU()
                            fakeCube._rotateR()
                            fakeCube._rotateU()
                            fakeCube._rotater()               
                            result += 'URUr'
                            break    
                        elif(fakeCube.get()[c] == temp and c == 31):
                            fakeCube._rotateu()
                            fakeCube._rotateu()
                            fakeCube._rotateF()
                            fakeCube._rotateU()
                            fakeCube._rotatef()
                            result += 'uuFUf'
                            break        
                                    
                        elif(fakeCube.get()[c] == temp and c == 13):
                            fakeCube._rotateB()
                            fakeCube._rotateU()
                            fakeCube._rotateb()
                            result += 'BUb'
                            break        
                        elif(fakeCube.get()[c] == temp and c == 22):
                                
                            fakeCube._rotateu()                            
                            fakeCube._rotateL()
                            fakeCube._rotateU()
                            fakeCube._rotatel()
                            result += 'uLUl'
            
                            break
                else:
                            
                    temp = fakeCube.get()[2]
                             
                    for c in centers:
                        if(fakeCube.get()[c] == temp and c == 4):                    
                            fakeCube._rotateR()
                            fakeCube._rotateU()
                            fakeCube._rotater()               
                            result += 'RUr'
                            break
                                
                        elif(fakeCube.get()[c] == temp and c == 31):
                            fakeCube._rotateU()
                            fakeCube._rotateF()
                            fakeCube._rotateU()
                            fakeCube._rotatef()
                            result += 'UFUf'
                            break        
                                    
                        elif(fakeCube.get()[c] == temp and c == 13):
                            fakeCube._rotateu()   
                            fakeCube._rotateB()
                            fakeCube._rotateU()
                            fakeCube._rotateb()
                            result += 'uBUb'
                            break        
                        elif(fakeCube.get()[c] == temp and c == 22):
                            fakeCube._rotateu()
                            fakeCube._rotateu()                              
                            fakeCube._rotateL()
                            fakeCube._rotateU()
                            fakeCube._rotatel()
                            result += 'uuLUl'
                            break            
                break
        
        ################## Move Right Corner Tiles######################################## 
            
        for tile in rightcorn:            #finding opposite corner of white corner
            if fakeCube.get()[tile] == matchcol:
                if tile == 2:
                    temp = fakeCube.get()[9]
                    for c in centers:
                        if(fakeCube.get()[c] == temp and c == 4):                    
                            fakeCube._rotateU()
                            fakeCube._rotatel()
                            fakeCube._rotateu()
                            fakeCube._rotateL()               
                            result += 'UluL'
                            break
                                
                        elif(fakeCube.get()[c] == temp and c == 13):
                            fakeCube._rotatef()
                            fakeCube._rotateu()
                            fakeCube._rotateF()
                            result += 'fuF'
                            break        
                                    
                        elif(fakeCube.get()[c] == temp and c == 22):
                            fakeCube._rotateu()
                            fakeCube._rotater()
                            fakeCube._rotateu()
                            fakeCube._rotateR()
                            result += 'uruR'
                            break        
                        elif(fakeCube.get()[c] == temp and c == 31):
                            fakeCube._rotateU()
                            fakeCube._rotateU()
                            fakeCube._rotateb()
                            fakeCube._rotateu()
                            fakeCube._rotateB()
                            result += 'UUbuB'
                            break
                            
                elif tile == 11:                   
                    temp = fakeCube.get()[18]
                    for c in centers:
                        if(fakeCube.get()[c] == temp and c == 4):
                            fakeCube._rotateU()
                            fakeCube._rotateU()                    
                            fakeCube._rotatel()
                            fakeCube._rotateu()
                            fakeCube._rotateL()               
                            result += 'UUluL'
                            break    
                        elif(fakeCube.get()[c] == temp and c == 13):
                            fakeCube._rotateU()
                            fakeCube._rotatef()
                            fakeCube._rotateu()
                            fakeCube._rotateF()
                            result += 'UfuF'
                            break        
                                    
                        elif(fakeCube.get()[c] == temp and c == 22):
                            fakeCube._rotater()
                            fakeCube._rotateu()
                            fakeCube._rotateR()
                            result += 'ruR'
                            break
                                    
                        elif(fakeCube.get()[c] == temp and c == 31):
                            fakeCube._rotateu()
                            fakeCube._rotateb()
                            fakeCube._rotateu()
                            fakeCube._rotateB()
                            result += 'ubuB'
                            break
                             
                            
                elif tile == 20:
                            
                    temp = fakeCube.get()[27]
                            
                    for c in centers:
                        if(fakeCube.get()[c] == temp and c == 4):
                            fakeCube._rotateu()                   
                            fakeCube._rotatel()
                            fakeCube._rotateu()
                            fakeCube._rotateL()               
                            result += 'uluL'
                            break
                            
                        elif(fakeCube.get()[c] == temp and c == 13):
                            fakeCube._rotateU()
                            fakeCube._rotateU()
                            fakeCube._rotatef()
                            fakeCube._rotateu()
                            fakeCube._rotateF()
                            result += 'UUfuF'
                            break        
                                    
                        elif(fakeCube.get()[c] == temp and c == 22):
                            fakeCube._rotateU()
                            fakeCube._rotater()
                            fakeCube._rotateu()
                            fakeCube._rotateR()
                            result += 'UruR'
                            break
                                
                        elif(fakeCube.get()[c] == temp and c == 31):
                            fakeCube._rotateb()
                            fakeCube._rotateu()
                            fakeCube._rotateB()
                            result += 'buB'
                            break
                else:
                    temp = fakeCube.get()[0]
                    for c in centers:     
                        if(fakeCube.get()[c] == temp and c == 4):                 
                            fakeCube._rotatel()
                            fakeCube._rotateu()
                            fakeCube._rotateL()               
                            result += 'luL'
                            break            
                        elif(fakeCube.get()[c] == temp and c == 13):
                            fakeCube._rotateu()
                            fakeCube._rotatef()
                            fakeCube._rotateu()
                            fakeCube._rotateF()
                            result += 'ufuF'
                            break            
                                        
                        elif(fakeCube.get()[c] == temp and c == 22):
                            fakeCube._rotateU()
                            fakeCube._rotateU()
                            fakeCube._rotater()
                            fakeCube._rotateu()
                            fakeCube._rotateR()
                            result += 'UUruR'
                            break
                                    
                        elif(fakeCube.get()[c] == temp and c == 31):
                            fakeCube._rotateU()
                            fakeCube._rotateb()
                            fakeCube._rotateu()
                            fakeCube._rotateB()
                            result += 'UbuB'
                            break          
                break
        
       
            
    return result    
        
   
   

