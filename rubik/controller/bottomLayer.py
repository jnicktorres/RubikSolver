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
    count = 0
    ##########################################################
    while count < 20:
        temp = None
        for i in rightcorn:
            print('checking')
            if fakeCube.get()[i] == matchcol:
                print('found')
                #finding opposite corner of white corner
                if i == 2:
                    temp = fakeCube.get()[9]
                    for c in centers:
                        if(fakeCube.get()[c] == temp and c == 4):                    
                            fakeCube._rotateU()
                            fakeCube._rotatel()
                            fakeCube._rotateu()
                            fakeCube._rotateL()               
                            result += 'UluL'
                        
                        elif(fakeCube.get()[c] == temp and c == 13):
                            fakeCube._rotatef()
                            fakeCube._rotateu()
                            fakeCube._rotateF()
                            result += 'fuF'
                            
                            
                        elif(fakeCube.get()[c] == temp and c == 22):
                            fakeCube._rotateu()
                            fakeCube._rotater()
                            fakeCube._rotateu()
                            fakeCube._rotateR()
                            result += 'uruR'
                            
                        elif(fakeCube.get()[c] == temp and c == 31):
                            fakeCube._rotateU()
                            fakeCube._rotateU()
                            fakeCube._rotateb()
                            fakeCube._rotateu()
                            fakeCube._rotateB()
                            result += 'UUbuB'
               
                    
                elif i == 11:
                    
                    temp = fakeCube.get()[18]
                    for c in centers:
                        if(fakeCube.get()[c] == temp and c == 4):
                            fakeCube._rotateU()
                            fakeCube._rotateU()                    
                            fakeCube._rotatel()
                            fakeCube._rotateu()
                            fakeCube._rotateL()               
                            result += 'UUluL'
                        
                        elif(fakeCube.get()[c] == temp and c == 13):
                            fakeCube._rotateU()
                            fakeCube._rotatef()
                            fakeCube._rotateu()
                            fakeCube._rotateF()
                            result += 'UfuF'
                            
                            
                        elif(fakeCube.get()[c] == temp and c == 22):
                            fakeCube._rotater()
                            fakeCube._rotateu()
                            fakeCube._rotateR()
                            result += 'ruR'
                            
                        elif(fakeCube.get()[c] == temp and c == 31):
                            fakeCube._rotateu()
                            fakeCube._rotateb()
                            fakeCube._rotateu()
                            fakeCube._rotateB()
                            result += 'ubuB'
                    
                     
                    
                elif i == 20:
                    
                    temp = fakeCube.get()[27]
                    
                    for c in centers:
                        if(fakeCube.get()[c] == temp and c == 4):
                            fakeCube._rotateu()                   
                            fakeCube._rotatel()
                            fakeCube._rotateu()
                            fakeCube._rotateL()               
                            result += 'uluL'
                        
                        elif(fakeCube.get()[c] == temp and c == 13):
                            fakeCube._rotateU()
                            fakeCube._rotateU()
                            fakeCube._rotatef()
                            fakeCube._rotateu()
                            fakeCube._rotateF()
                            result += 'UUfuF'
                            
                            
                        elif(fakeCube.get()[c] == temp and c == 22):
                            fakeCube._rotateU()
                            fakeCube._rotater()
                            fakeCube._rotateu()
                            fakeCube._rotateR()
                            result += 'UruR'
                            
                        elif(fakeCube.get()[c] == temp and c == 31):
                            fakeCube._rotateb()
                            fakeCube._rotateu()
                            fakeCube._rotateB()
                            result += 'buB'
                    
                else:
                    temp = fakeCube.get()[0]
                    for c in centers:     
                        if(fakeCube.get()[c] == temp and c == 4):                 
                                fakeCube._rotatel()
                                fakeCube._rotateu()
                                fakeCube._rotateL()               
                                result += 'luL'
                            
                        elif(fakeCube.get()[c] == temp and c == 13):
                                fakeCube._rotateu()
                                fakeCube._rotatef()
                                fakeCube._rotateu()
                                fakeCube._rotateF()
                                result += 'ufuF'
                                
                                
                        elif(fakeCube.get()[c] == temp and c == 22):
                                fakeCube._rotateU()
                                fakeCube._rotateU()
                                fakeCube._rotater()
                                fakeCube._rotateu()
                                fakeCube._rotateR()
                                result += 'UUruR'
                                
                        elif(fakeCube.get()[c] == temp and c == 31):
                                fakeCube._rotateU()
                                fakeCube._rotateb()
                                fakeCube._rotateu()
                                fakeCube._rotateB()
                                result += 'UbuB'
        
    
###################### Solve Left Corners #####################################################################    

        for i in leftcorn:     
           
            if fakeCube.get()[i] == matchcol:
                #finding opposite corner of white corner
                if i == 0:
                    temp = fakeCube.get()[29]
                    for c in centers:
                        if(fakeCube.get()[c] == temp and c == 4):                    
                                fakeCube._rotateu()
                                fakeCube._rotateR()
                                fakeCube._rotateU()
                                fakeCube._rotater()               
                                result += 'uRUr'
                            
                        elif(fakeCube.get()[c] == temp and c == 31):
                                fakeCube._rotateF()
                                fakeCube._rotateU()
                                fakeCube._rotatef()
                                result += 'FUf'
                                
                                
                        elif(fakeCube.get()[c] == temp and c == 13):
                                fakeCube._rotateu()
                                fakeCube._rotateu()
                                fakeCube._rotateB()
                                fakeCube._rotateU()
                                fakeCube._rotateb()
                                result += 'uuBUb'
                                
                        elif(fakeCube.get()[c] == temp and c == 22):
                                fakeCube._rotateU()
                                fakeCube._rotateL()
                                fakeCube._rotateU()
                                fakeCube._rotatel()
                                result += 'ULUl'
                   
                        
                elif i == 27:
                
                    temp = fakeCube.get()[20]
                    for c in centers:
                        if(fakeCube.get()[c] == temp and c == 4):                    
                                fakeCube._rotateu()
                                fakeCube._rotateu()
                                fakeCube._rotateR()
                                fakeCube._rotateU()
                                fakeCube._rotater()               
                                result += 'uuRUr'
                            
                        elif(fakeCube.get()[c] == temp and c == 31):
                                fakeCube._rotateu()
                                fakeCube._rotateF()
                                fakeCube._rotateU()
                                fakeCube._rotatef()
                                result += 'uFUf'
                                
                                
                        elif(fakeCube.get()[c] == temp and c == 13):
                                fakeCube._rotateU()
                                fakeCube._rotateB()
                                fakeCube._rotateU()
                                fakeCube._rotateb()
                                result += 'UBUb'
                                
                        elif(fakeCube.get()[c] == temp and c == 22):
                                fakeCube._rotateL()
                                fakeCube._rotateU()
                                fakeCube._rotatel()
                                result += 'LUl'
                         
                        
                elif i == 18:
                        
                    temp = fakeCube.get()[11]
                        
                    for c in centers:
                        if(fakeCube.get()[c] == temp and c == 4):                    
                                fakeCube._rotateU()
                                fakeCube._rotateR()
                                fakeCube._rotateU()
                                fakeCube._rotater()               
                                result += 'URUr'
                            
                        elif(fakeCube.get()[c] == temp and c == 31):
                                fakeCube._rotateu()
                                fakeCube._rotateu()
                                fakeCube._rotateF()
                                fakeCube._rotateU()
                                fakeCube._rotatef()
                                result += 'uuFUf'
                                
                                
                        elif(fakeCube.get()[c] == temp and c == 13):
                                fakeCube._rotateB()
                                fakeCube._rotateU()
                                fakeCube._rotateb()
                                result += 'BUb'
                                
                        elif(fakeCube.get()[c] == temp and c == 22):
                                fakeCube._rotateu()                            
                                fakeCube._rotateL()
                                fakeCube._rotateU()
                                fakeCube._rotatel()
                                result += 'uLUl'
                        
                else:
                        
                    temp = fakeCube.get()[2]
                         
                    for c in centers:
                        if(fakeCube.get()[c] == temp and c == 4):                    
                                fakeCube._rotateR()
                                fakeCube._rotateU()
                                fakeCube._rotater()               
                                result += 'RUr'
                            
                        elif(fakeCube.get()[c] == temp and c == 31):
                                fakeCube._rotateU()
                                fakeCube._rotateF()
                                fakeCube._rotateU()
                                fakeCube._rotatef()
                                result += 'UFUf'
                                
                                
                        elif(fakeCube.get()[c] == temp and c == 13):
                                fakeCube._rotateu()   
                                fakeCube._rotateB()
                                fakeCube._rotateU()
                                fakeCube._rotateb()
                                result += 'uBUb'
                                
                        elif(fakeCube.get()[c] == temp and c == 22):
                                fakeCube._rotateu()
                                fakeCube._rotateu()                              
                                fakeCube._rotateL()
                                fakeCube._rotateU()
                                fakeCube._rotatel()
                                result += 'uuLUl'
                
        
        count += 1
    
                              
    
    return result;      #TODO:  remove this stubbed value
