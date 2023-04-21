from rubik.model.constants import *
from rubik.model.cube import Cube

def solveUpperLayer(theCube: Cube) -> str:
    '''
        This is the top-level function  for rotating
        a cube so that the entire upper layer is solved.
        
        input:  an instance of the cube class with up-face surface solved
        output: the rotations required to solve the upper layer  
    '''  
    #### Variables  
    inputCube = theCube
    result = ''
    frontFace = inputCube.get()[FMM]
    rightFace = inputCube.get()[RMM]
    backFace = inputCube.get()[BMM]
    leftFace = inputCube.get()[LMM]
    currentColor = FMM
    ######
    
    
    # Does the Top Corners Method *******************************

    while checkTopCorners(inputCube) == False:
        if inputCube.get()[FTL] == inputCube.get()[FTR]:   
            if inputCube.get()[FTL] == frontFace:
                result += "fUBuFUbBUbUBUUb"
                inputCube.rotate("fUBuFUbBUbUBUUb") 
                 
            elif inputCube.get()[FTL] == rightFace:
                result += "urULuRUlLUlULUUl"
                inputCube._rotateu()
                inputCube.rotate("rULuRUlLUlULUUl")  
                     
            elif inputCube.get()[FTL] == backFace:
                result += 'uubUFuBUfFUfUFUUf'
                inputCube._rotateu() 
                inputCube._rotateu() 
                inputCube.rotate('bUFuBUfFUfUFUUf')
                
            elif inputCube.get()[FTL] == leftFace:
                result += 'UlURuLUrRUrURUUr'
                inputCube._rotateU() 
                inputCube.rotate("lURuLUrRUrURUUr")
                
        #Solving for Right Face                          
        elif inputCube.get()[RTL] == inputCube.get()[RTR]:
            if inputCube.get()[RTL] == frontFace:
                result += "UfUBuFUbBUbUBUUb"
                inputCube._rotateU() 
                inputCube.rotate("fUBuFUbBUbUBUUb")  
                
            elif inputCube.get()[RTL] == rightFace:
                result += "rULuRUlLUlULUUl"
                inputCube.rotate("rULuRUlLUlULUUl")  
                
            elif inputCube.get()[RTL] == backFace:
                result += 'ubUFuBUfFUfUFUUf'
                inputCube._rotateu() 
                inputCube.rotate('bUFuBUfFUfUFUUf')
                
            elif inputCube.get()[RTL] == leftFace:
                result += 'uulURuLUrRUrURUUr'
                inputCube._rotateu()
                inputCube._rotateu()
                inputCube.rotate("lURuLUrRUrURUUr")
                
        #Solving for Back Face            
        elif inputCube.get()[BTL] == inputCube.get()[BTR]:
            if inputCube.get()[BTL] == frontFace:
                result += "uufUBuFUbBUbUBUUb"
                inputCube._rotateu() 
                inputCube._rotateu() 
                inputCube.rotate("fUBuFUbBUbUBUUb") 
                    
            elif inputCube.get()[BTL] == rightFace:
                result += 'UrULuRUlLUlULUUl'
                inputCube._rotateU() 
                inputCube.rotate("rULuRUlLUlULUUl")
                    
            elif inputCube.get()[BTL] == backFace:
                result += 'bUFuBUfFUfUFUUf'
                inputCube.rotate('bUFuBUfFUfUFUUf')
                 
            elif inputCube.get()[BTL] == leftFace:
                result += 'ulURuLUrRUrURUUr'
                inputCube._rotateu()
                inputCube.rotate("lURuLUrRUrURUUr")
        
        #Solving for left Face    
        elif inputCube.get()[LTL] == inputCube.get()[LTR]:
            if inputCube.get()[LTL] == frontFace:
                result += "ufUBuFUbBUbUBUUb"
                inputCube._rotateu() 
                inputCube.rotate("fUBuFUbBUbUBUUb")       
            elif inputCube.get()[LTL] == rightFace:
                result += "uurULuRUlLUlULUUl"
                inputCube._rotateu()   
                inputCube._rotateu()
                inputCube.rotate("rULuRUlLUlULUUl")      
            elif inputCube.get()[LTL] == backFace:
                result += 'bUFuBUfFUfUFUUf'
                inputCube._rotateU() 
                inputCube.rotate('bUFuBUfFUfUFUUf')
            elif inputCube.get()[LTL] == leftFace:
                result += 'lURuLUrRUrURUUr'
                inputCube.rotate("lURuLUrRUrURUUr")
        
        else:
            #if we have no matching pairs of corners, we line up a single corner and rotate
            while(inputCube.get()[FTR] != inputCube.get()[currentColor]):
                #Add RTL tiles to get next center
                currentColor += RTL
                 
            if currentColor == FMM:
                result += "fUBuFUbBUbUBUUb"
                inputCube.rotate("fUBuFUbBUbUBUUb") 
                
            elif currentColor == RMM:
                result += "rULuRUlLUlULUUl"
                inputCube.rotate("rULuRUlLUlULUUl") 
            
            elif currentColor == BMM:
                result += 'bUFuBUfFUfUFUUf'
                inputCube.rotate('bUFuBUfFUfUFUUf')
            else:
                result += 'lURuLUrRUrURUUr'
                inputCube.rotate("lURuLUrRUrURUUr")
    # **********************************        

    # Solve for the Top Layer

    while isFinishedCube(inputCube) == False:
        if checkFullFace(inputCube) == "front":
            result += "BBulRBBrLuBB"
            inputCube.rotate("BBulRBBrLuBB")

        elif checkFullFace(inputCube) == "right":

            result += "LLufBLLbFuLL"
            inputCube.rotate("LLufBLLbFuLL")

        elif checkFullFace(inputCube) == "back":
            result += "FFurLFFlRuFF"
            inputCube.rotate("FFurLFFlRuFF")

        elif checkFullFace(inputCube) == "left":
            result += "RRubFRRfBuRR"
            inputCube.rotate("RRubFRRfBuRR")

        elif checkFullFace(inputCube) == "no face":
            result += "FFurLFFlRuFF"
            inputCube.rotate("FFurLFFlRuFF")

    return result
     
# check to see if top corners step is complete        
def checkTopCorners(inputCube):  
    if(inputCube.get()[FTL] == inputCube.get()[FMM] and inputCube.get()[FTR] == inputCube.get()[FMM]):
        if(inputCube.get()[RTL] == inputCube.get()[RMM] and inputCube.get()[RTR] == inputCube.get()[RMM]):
            if(inputCube.get()[BTL] == inputCube.get()[BMM] and inputCube.get()[BTR] == inputCube.get()[BMM]):
                if(inputCube.get()[LTL] == inputCube.get()[LMM] and inputCube.get()[LTR] == inputCube.get()[LMM]):
                    return True
    return False

# If we find full face, tell which direction it is
def checkFullFace(inputCube):
    #Get colors of each face
    frontFace = inputCube.get()[FMM]
    rightFace = inputCube.get()[RMM]
    backFace = inputCube.get()[BMM]
    leftFace = inputCube.get()[LMM]
    
    if (inputCube.get()[FTL] == frontFace and inputCube.get()[FTM] == frontFace and inputCube.get()[FTR] == frontFace):
        return "front"
    elif (inputCube.get()[RTL] == rightFace and inputCube.get()[RTM] == rightFace and inputCube.get()[RTR] == rightFace):
        return "right"
    elif (inputCube.get()[BTL] == backFace and inputCube.get()[BTM] == backFace and inputCube.get()[BTR] == backFace):
        return "back"
    elif (inputCube.get()[LTL] == leftFace and inputCube.get()[LTM] == leftFace and inputCube.get()[LTR] == leftFace):
        return "left"

    return "no face"


#this method just checks every tile to see if we have a solved cube
def isFinishedCube(inputCube):
    if(inputCube.get()[DTL] == inputCube.get()[DMM] and inputCube.get()[DTM] == inputCube.get()[DMM] and inputCube.get()[DTR] == inputCube.get()[DMM] and inputCube.get()[DML] == inputCube.get()[DMM] and inputCube.get()[DMR] == inputCube.get()[DMM] and inputCube.get()[DBL] == inputCube.get()[DMM] and inputCube.get()[DBM] == inputCube.get()[DMM] and inputCube.get()[DBR] == inputCube.get()[DMM]):
        if(inputCube.get()[FTL] == inputCube.get()[FMM] and inputCube.get()[FTM] == inputCube.get()[FMM] and inputCube.get()[FTR] == inputCube.get()[FMM]and inputCube.get()[FML] == inputCube.get()[FMM] and inputCube.get()[FMR] == inputCube.get()[FMM] and inputCube.get()[FBL] == inputCube.get()[FMM] and inputCube.get()[FBM] == inputCube.get()[FMM] and inputCube.get()[FBR] == inputCube.get()[FMM]):
            if(inputCube.get()[RTL] == inputCube.get()[RMM] and inputCube.get()[RTM] == inputCube.get()[RMM] and inputCube.get()[RTR] == inputCube.get()[RMM] and inputCube.get()[RML] == inputCube.get()[RMM] and inputCube.get()[RMR] == inputCube.get()[RMM] and inputCube.get()[RBL] == inputCube.get()[RMM] and inputCube.get()[RBM] == inputCube.get()[RMM] and inputCube.get()[RBR] == inputCube.get()[RMM]):
                if(inputCube.get()[BTL] == inputCube.get()[BMM] and inputCube.get()[BTM] == inputCube.get()[BMM] and inputCube.get()[BTR] == inputCube.get()[BMM] and inputCube.get()[BML] == inputCube.get()[BMM] and inputCube.get()[BMR] == inputCube.get()[BMM] and inputCube.get()[BBL] == inputCube.get()[BMM] and inputCube.get()[BBM] == inputCube.get()[BMM] and inputCube.get()[BBR] == inputCube.get()[BMM]):
                    if(inputCube.get()[LTL] == inputCube.get()[LMM] and inputCube.get()[LTM] == inputCube.get()[LMM] and inputCube.get()[LTR] == inputCube.get()[LMM] and inputCube.get()[LML] == inputCube.get()[LMM] and inputCube.get()[LMR] == inputCube.get()[LMM] and inputCube.get()[LBL] == inputCube.get()[LMM] and inputCube.get()[LBM] == inputCube.get()[LMM] and inputCube.get()[LBR] == inputCube.get()[LMM]):
                        if(inputCube.get()[UTL] == inputCube.get()[UMM] and inputCube.get()[UTM] == inputCube.get()[UMM] and inputCube.get()[UTR] == inputCube.get()[UMM] and inputCube.get()[UML] == inputCube.get()[UMM] and inputCube.get()[UMR] == inputCube.get()[UMM] and inputCube.get()[UBL] == inputCube.get()[UMM] and inputCube.get()[UBM] == inputCube.get()[UMM] and inputCube.get()[UBR] == inputCube.get()[UMM]):
                            return True
                    
                        

    return False

