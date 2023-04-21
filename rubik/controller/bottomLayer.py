from rubik.model.constants import *
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
    matchcol = inputCube.get()[DMM] # color to be matched
    centers = [FMM,RMM,BMM,LMM]
    rightcorn = [FTR,RTR, BTR,LTR]
    leftcorn = [FTL,RTL, BTL,LTL]
    topcorn = [UTL,UTR,UBL,UBR]
    result = ''
    
    
    
    ## start by iterating 4 times since thats how many it takes to circle completetly
    
    for _ in range(0,4):
        
    ################## if white tiles are on bottom layer or white tile on bottom is wrong then move ########################################
        if (matchcol in inputCube.get()[FBL] or matchcol in inputCube.get()[LBR]) or (matchcol == inputCube.get()[DTL] and inputCube.get()[FBL] != inputCube.get()[FMM]):
            inputCube.rotate('luL') 
            result += 'luL'
            
               
        elif (matchcol in inputCube.get()[LBL] or matchcol in inputCube.get()[BBR]) or (matchcol == inputCube.get()[DBL] and inputCube.get()[LBL] != inputCube.get()[LMM]):
            inputCube.rotate('buB') 
            result += 'buB'
        elif  (matchcol in inputCube.get()[FBR] or matchcol in inputCube.get()[RBL]) or (matchcol == inputCube.get()[DTR] and inputCube.get()[RBL] != inputCube.get()[RMM]):
            inputCube.rotate('fuF') 
            result += 'fuF'
               
        elif  (matchcol in inputCube.get()[RBR] or matchcol in inputCube.get()[BBL]) or (matchcol == inputCube.get()[DBR] and inputCube.get()[BBL] != inputCube.get()[BMM]):
            inputCube.rotate('ruR') 
            result += 'ruR'
        
             
        ################## if white tiles are on top then move to middle of cube ########################################    
        for tile in topcorn:
            if inputCube.get()[tile] == matchcol:
                for _ in range(0,4):     
                    if inputCube.get()[UTL] == matchcol and inputCube.get()[DBL] != matchcol:
                        result += 'Lul'
                        inputCube.rotate('Lul') 
                    elif inputCube.get()[UTR] == matchcol and inputCube.get()[DBR] != matchcol:
                        result += 'Bub'
                        inputCube.rotate('Bub')   
                    elif inputCube.get()[UBL] == matchcol and inputCube.get()[DTL] != matchcol:
                        result += 'Fuf'
                        inputCube.rotate('Fuf')   
                    elif inputCube.get()[UBR] == matchcol and inputCube.get()[DTR] != matchcol:
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
                if tile == FTL:
                    currentColor = inputCube.get()[LTR]
                    for center in centers:
                        if(inputCube.get()[center] == currentColor and center == FMM):                    
                            inputCube.rotate('uRUr')             
                            result += 'uRUr'
                            break    
                        elif(inputCube.get()[center] == currentColor and center == LMM):
                            inputCube.rotate('FUf') 
                            result += 'FUf'
                            break                      
                        elif(inputCube.get()[center] == currentColor and center == RMM):
                            inputCube.rotate('uuBUb') 
                            result += 'uuBUb'
                            break        
                        elif(inputCube.get()[center] == currentColor and center == BMM):
                            inputCube.rotate('ULUl') 
                            result += 'ULUl'
                            break
                            
                elif tile == LTL:
                    
                    currentColor = inputCube.get()[BTR]
                    for center in centers:
                        if(inputCube.get()[center] == currentColor and center == FMM):                    
                            inputCube.rotate('uuRUr')             
                            result += 'uuRUr'
                            break    
                        elif(inputCube.get()[center] == currentColor and center == LMM):
                            inputCube.rotate('uFUf')
                            result += 'uFUf'
                            break        
                                    
                        elif(inputCube.get()[center] == currentColor and center == RMM):
                            inputCube.rotate('UBUb')  
                            result += 'UBUb'
                            break
                                
                        elif(inputCube.get()[center] == currentColor and center == BMM):
                            inputCube.rotate('LUl')  
                            result += 'LUl'
                            break 
                            
                elif tile == BTL:
                            
                    currentColor = inputCube.get()[RTR]
                            
                    for center in centers:
                        if(inputCube.get()[center] == currentColor and center == FMM):                    
                            inputCube.rotate('URUr')            
                            result += 'URUr'
                            break    
                        elif(inputCube.get()[center] == currentColor and center == LMM):
                            inputCube.rotate('uuFUf')   
                            result += 'uuFUf'
                            break        
                                    
                        elif(inputCube.get()[center] == currentColor and center == RMM):
                            inputCube.rotate('BUb')   
                            result += 'BUb'
                            break        
                        elif(inputCube.get()[center] == currentColor and center == BMM):
                                
                            inputCube.rotate('uLUl')    
                            result += 'uLUl'
            
                            break
                else:
                            
                    currentColor = inputCube.get()[FTR]
                             
                    for center in centers:
                        if(inputCube.get()[center] == currentColor and center == FMM):                    
                            inputCube.rotate('RUr')              
                            result += 'RUr'
                            break
                                
                        elif(inputCube.get()[center] == currentColor and center == LMM):
                            inputCube.rotate('UFUf')  
                            result += 'UFUf'
                            break        
                                    
                        elif(inputCube.get()[center] == currentColor and center == RMM):
                            inputCube.rotate('uBUb')  
                            result += 'uBUb'
                            break        
                        elif(inputCube.get()[center] == currentColor and center == BMM):
                            inputCube.rotate('uuLUl')  
                            result += 'uuLUl'
                            break            
                break
        
        ################## Move Right Corner Tiles######################################## 
            
        for tile in rightcorn:            #finding opposite corner of white corner
            if inputCube.get()[tile] == matchcol:
                if tile == FTR:
                    currentColor = inputCube.get()[RTL]
                    for center in centers:
                        if(inputCube.get()[center] == currentColor and center == FMM):                    
                            inputCube.rotate('UluL')               
                            result += 'UluL'
                            break
                                
                        elif(inputCube.get()[center] == currentColor and center == RMM):
                            inputCube.rotate('fuF') 
                            result += 'fuF'
                            break        
                                    
                        elif(inputCube.get()[center] == currentColor and center == BMM):
                            inputCube.rotate('uruR') 
                            result += 'uruR'
                            break        
                        elif(inputCube.get()[center] == currentColor and center == LMM):
                            inputCube.rotate('UUbuB') 
                            result += 'UUbuB'
                            break
                            
                elif tile == RTR:                   
                    currentColor = inputCube.get()[BTL]
                    for center in centers:
                        if(inputCube.get()[center] == currentColor and center == FMM):
                            inputCube.rotate('UUluL')             
                            result += 'UUluL'
                            break    
                        elif(inputCube.get()[center] == currentColor and center == RMM):
                            inputCube.rotate('UfuF')
                            result += 'UfuF'
                            break        
                                    
                        elif(inputCube.get()[center] == currentColor and center == BMM):
                            inputCube.rotate('ruR')
                            result += 'ruR'
                            break
                                    
                        elif(inputCube.get()[center] == currentColor and center == LMM):
                            inputCube.rotate('ubuB')
                            result += 'ubuB'
                            break
                             
                            
                elif tile == BTR:
                            
                    currentColor = inputCube.get()[LTL]
                            
                    for center in centers:
                        if(inputCube.get()[center] == currentColor and center == FMM):
                            inputCube.rotate('uluL')            
                            result += 'uluL'
                            break
                            
                        elif(inputCube.get()[center] == currentColor and center == RMM):
                            inputCube.rotate('UUfuF')
                            result += 'UUfuF'
                            break        
                                    
                        elif(inputCube.get()[center] == currentColor and center == BMM):
                            inputCube.rotate('UruR')
                            result += 'UruR'
                            break
                                
                        elif(inputCube.get()[center] == currentColor and center == LMM):
                            inputCube.rotate('buB')    
                            result += 'buB'
                            break
                else:
                    currentColor = inputCube.get()[FTL]
                    for center in centers:     
                        if(inputCube.get()[center] == currentColor and center == FMM):  
                            inputCube.rotate('luL')                             
                            result += 'luL'
                            break     
                               
                        elif(inputCube.get()[center] == currentColor and center == RMM):
                            inputCube.rotate('ufuF')
                            result += 'ufuF'
                            break            
                                        
                        elif(inputCube.get()[center] == currentColor and center == BMM):
                            inputCube.rotate('UUruR')
                            result += 'UUruR'
                            break
                                    
                        elif(inputCube.get()[center] == currentColor and center == LMM):
                            inputCube.rotate('UbuB')
                            result += 'UbuB'
                            break          
                break
        
       
            
    return result    
        
   
   

