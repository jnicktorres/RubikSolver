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
            inputCube.rotate('luL') 
            result += 'luL'
            
               
        elif (matchcol in inputCube.get()[33] or matchcol in inputCube.get()[26]) or (matchcol == inputCube.get()[51] and inputCube.get()[33] != inputCube.get()[31]):
            inputCube.rotate('buB') 
            result += 'buB'
        elif  (matchcol in inputCube.get()[8] or matchcol in inputCube.get()[15]) or (matchcol == inputCube.get()[47] and inputCube.get()[15] != inputCube.get()[13]):
            inputCube.rotate('fuF') 
            result += 'fuF'
               
        elif  (matchcol in inputCube.get()[17] or matchcol in inputCube.get()[24]) or (matchcol == inputCube.get()[53] and inputCube.get()[24] != inputCube.get()[22]):
            inputCube.rotate('ruR') 
            result += 'ruR'
        
             
        ################## if white tiles are on top then move to middle of cube ########################################    
        for tile in topcorn:
            if inputCube.get()[tile] == matchcol:
                for _ in range(0,4):     
                    if inputCube.get()[36] == matchcol and inputCube.get()[51] != matchcol:
                        result += 'Lul'
                        inputCube.rotate('Lul') 
                    elif inputCube.get()[38] == matchcol and inputCube.get()[53] != matchcol:
                        result += 'Bub'
                        inputCube.rotate('Bub')   
                    elif inputCube.get()[42] == matchcol and inputCube.get()[45] != matchcol:
                        result += 'Fuf'
                        inputCube.rotate('Fuf')   
                    elif inputCube.get()[44] == matchcol and inputCube.get()[47] != matchcol:
                        result += 'Rur'
                        inputCube.rotate('Rur')        
                    else:
                        result += 'U'
                        inputCube._rotateU()
                break
        
        ############################### Move Left Corner Tiles #################################################  
            
        for tile in leftcorn:      
            if inputCube.get()[tile] == matchcol:
                #finding opposite corner of white corner
                if tile == 0:
                    currentColor = inputCube.get()[29]
                    for center in centers:
                        if(inputCube.get()[center] == currentColor and center == 4):                    
                            inputCube.rotate('uRUr')             
                            result += 'uRUr'
                            break    
                        elif(inputCube.get()[center] == currentColor and center == 31):
                            inputCube.rotate('FUf') 
                            result += 'FUf'
                            break                      
                        elif(inputCube.get()[center] == currentColor and center == 13):
                            inputCube.rotate('uuBUb') 
                            result += 'uuBUb'
                            break        
                        elif(inputCube.get()[center] == currentColor and center == 22):
                            inputCube.rotate('ULUl') 
                            result += 'ULUl'
                            break
                            
                elif tile == 27:
                    
                    currentColor = inputCube.get()[20]
                    for center in centers:
                        if(inputCube.get()[center] == currentColor and center == 4):                    
                            inputCube.rotate('uuRUr')             
                            result += 'uuRUr'
                            break    
                        elif(inputCube.get()[center] == currentColor and center == 31):
                            inputCube.rotate('uFUf')
                            result += 'uFUf'
                            break        
                                    
                        elif(inputCube.get()[center] == currentColor and center == 13):
                            inputCube.rotate('UBUb')  
                            result += 'UBUb'
                            break
                                
                        elif(inputCube.get()[center] == currentColor and center == 22):
                            inputCube.rotate('LUl')  
                            result += 'LUl'
                            break 
                            
                elif tile == 18:
                            
                    currentColor = inputCube.get()[11]
                            
                    for center in centers:
                        if(inputCube.get()[center] == currentColor and center == 4):                    
                            inputCube.rotate('URUr')            
                            result += 'URUr'
                            break    
                        elif(inputCube.get()[center] == currentColor and center == 31):
                            inputCube.rotate('uuFUf')   
                            result += 'uuFUf'
                            break        
                                    
                        elif(inputCube.get()[center] == currentColor and center == 13):
                            inputCube.rotate('BUb')   
                            result += 'BUb'
                            break        
                        elif(inputCube.get()[center] == currentColor and center == 22):
                                
                            inputCube.rotate('uLUl')    
                            result += 'uLUl'
            
                            break
                else:
                            
                    currentColor = inputCube.get()[2]
                             
                    for center in centers:
                        if(inputCube.get()[center] == currentColor and center == 4):                    
                            inputCube.rotate('RUr')              
                            result += 'RUr'
                            break
                                
                        elif(inputCube.get()[center] == currentColor and center == 31):
                            inputCube.rotate('UFUf')  
                            result += 'UFUf'
                            break        
                                    
                        elif(inputCube.get()[center] == currentColor and center == 13):
                            inputCube.rotate('uBUb')  
                            result += 'uBUb'
                            break        
                        elif(inputCube.get()[center] == currentColor and center == 22):
                            inputCube.rotate('uuLUl')  
                            result += 'uuLUl'
                            break            
                break
        
        ################## Move Right Corner Tiles######################################## 
            
        for tile in rightcorn:            #finding opposite corner of white corner
            if inputCube.get()[tile] == matchcol:
                if tile == 2:
                    currentColor = inputCube.get()[9]
                    for center in centers:
                        if(inputCube.get()[center] == currentColor and center == 4):                    
                            inputCube.rotate('UluL')               
                            result += 'UluL'
                            break
                                
                        elif(inputCube.get()[center] == currentColor and center == 13):
                            inputCube.rotate('fuF') 
                            result += 'fuF'
                            break        
                                    
                        elif(inputCube.get()[center] == currentColor and center == 22):
                            inputCube.rotate('uruR') 
                            result += 'uruR'
                            break        
                        elif(inputCube.get()[center] == currentColor and center == 31):
                            inputCube.rotate('UUbuB') 
                            result += 'UUbuB'
                            break
                            
                elif tile == 11:                   
                    currentColor = inputCube.get()[18]
                    for center in centers:
                        if(inputCube.get()[center] == currentColor and center == 4):
                            inputCube.rotate('UUluL')             
                            result += 'UUluL'
                            break    
                        elif(inputCube.get()[center] == currentColor and center == 13):
                            inputCube.rotate('UfuF')
                            result += 'UfuF'
                            break        
                                    
                        elif(inputCube.get()[center] == currentColor and center == 22):
                            inputCube.rotate('ruR')
                            result += 'ruR'
                            break
                                    
                        elif(inputCube.get()[center] == currentColor and center == 31):
                            inputCube.rotate('ubuB')
                            result += 'ubuB'
                            break
                             
                            
                elif tile == 20:
                            
                    currentColor = inputCube.get()[27]
                            
                    for center in centers:
                        if(inputCube.get()[center] == currentColor and center == 4):
                            inputCube.rotate('uluL')            
                            result += 'uluL'
                            break
                            
                        elif(inputCube.get()[center] == currentColor and center == 13):
                            inputCube.rotate('UUfuF')
                            result += 'UUfuF'
                            break        
                                    
                        elif(inputCube.get()[center] == currentColor and center == 22):
                            inputCube.rotate('UruR')
                            result += 'UruR'
                            break
                                
                        elif(inputCube.get()[center] == currentColor and center == 31):
                            inputCube.rotate('buB')    
                            result += 'buB'
                            break
                else:
                    currentColor = inputCube.get()[0]
                    for center in centers:     
                        if(inputCube.get()[center] == currentColor and center == 4):  
                            inputCube.rotate('luL')                             
                            result += 'luL'
                            break     
                               
                        elif(inputCube.get()[center] == currentColor and center == 13):
                            inputCube.rotate('ufuF')
                            result += 'ufuF'
                            break            
                                        
                        elif(inputCube.get()[center] == currentColor and center == 22):
                            inputCube.rotate('UUruR')
                            result += 'UUruR'
                            break
                                    
                        elif(inputCube.get()[center] == currentColor and center == 31):
                            inputCube.rotate('UbuB')
                            result += 'UbuB'
                            break          
                break
        
       
            
    return result    
        
   
   

