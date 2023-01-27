from rubik.model.constants import *

class Cube:
    '''
    Rubik's cube
    '''
    def __init__(self, encodedCube):
        self.cube = encodedCube
        
    def rotate(self, directions):
        
        #self._rotateF()  
        #self._rotatef()
        #self._rotateR()
        #self._rotater()
        
        
        cubeList = list(self.cube)
        rotatedCubeList = cubeList[:]
        #rotate back face       
        
        rotatedCubeList[BTL] = cubeList[BBL]
        rotatedCubeList[BTM] = cubeList[BML]
        rotatedCubeList[BTR] = cubeList[BTL]      
        rotatedCubeList[BML] = cubeList[BBM]
        rotatedCubeList[BMM] = cubeList[BMM]
        rotatedCubeList[BMR] = cubeList[BTM]      
        rotatedCubeList[BBL] = cubeList[BBR]
        rotatedCubeList[BBM] = cubeList[BMR]
        rotatedCubeList[BBR] = cubeList[BTR]   
           
        #rotate up to right
        rotatedCubeList[UTL] = cubeList[RTR]
        rotatedCubeList[UTM] = cubeList[RMR]
        rotatedCubeList[UTR] = cubeList[RBR]
                
        #rotate bottom to left        
        rotatedCubeList[LTL] = cubeList[UTR]
        rotatedCubeList[LML] = cubeList[UTM]
        rotatedCubeList[LBL] = cubeList[UTL]
        
        #rotate right to bottom       
        rotatedCubeList[DBL] = cubeList[LTL]
        rotatedCubeList[DBM] = cubeList[LML]
        rotatedCubeList[DBR] = cubeList[LBL]        
        #rotate left to top
        rotatedCubeList[RTR] = cubeList[DBR]
        rotatedCubeList[RMR] = cubeList[DBM]
        rotatedCubeList[RBR] = cubeList[DBL]
        self.cube = "".join(rotatedCubeList)
        
        return self.cube
        
        
    def get(self):
        return self.cube
    
    def _rotateF(self):
        cubeList = list(self.cube)
        rotatedCubeList = cubeList[:]
        #rotate front face       
        rotatedCubeList[FTR] = cubeList[FTL]
        rotatedCubeList[FMR] = cubeList[FTM]
        rotatedCubeList[FBR] = cubeList[FTR]
        rotatedCubeList[FTM] = cubeList[FML]
        rotatedCubeList[FMM] = cubeList[FMM]
        rotatedCubeList[FBM] = cubeList[FMR]
        rotatedCubeList[FTL] = cubeList[FBL]
        rotatedCubeList[FML] = cubeList[FBM]
        rotatedCubeList[FBL] = cubeList[FBR]      
        #rotate up to right
        rotatedCubeList[RTL] = cubeList[UBL]
        rotatedCubeList[RML] = cubeList[UBM]
        rotatedCubeList[RBL] = cubeList[UBR]        
        #rotate bottom to left        
        rotatedCubeList[DTR] = cubeList[RTL]
        rotatedCubeList[DTM] = cubeList[RML]
        rotatedCubeList[DTL] = cubeList[RBL]
        #rotate right to bottom       
        rotatedCubeList[LTR] = cubeList[DTL]
        rotatedCubeList[LMR] = cubeList[DTM]
        rotatedCubeList[LBR] = cubeList[DTR]        
        #rotate left to top
        rotatedCubeList[UBR] = cubeList[LTR]
        rotatedCubeList[UBM] = cubeList[LMR]
        rotatedCubeList[UBL] = cubeList[LBR]
        self.cube = "".join(rotatedCubeList)

    def _rotatef(self):
        cubeList = list(self.cube)
        rotatedCubeList = cubeList[:]
        #rotate front face
        rotatedCubeList[FTL] = cubeList[FTR]
        rotatedCubeList[FML] = cubeList[FTM]
        rotatedCubeList[FBL] = cubeList[FTL]
        rotatedCubeList[FTM] = cubeList[FMR]
        rotatedCubeList[FMM] = cubeList[FMM]
        rotatedCubeList[FBM] = cubeList[FML]
        rotatedCubeList[FTR] = cubeList[FBR]
        rotatedCubeList[FMR] = cubeList[FBM]
        rotatedCubeList[FBR] = cubeList[FBL]
        #rotate up to left
        rotatedCubeList[LTR] = cubeList[UBR]
        rotatedCubeList[LMR] = cubeList[UBM]
        rotatedCubeList[LBR] = cubeList[UBL]
        #rotate bottom to right
        rotatedCubeList[DTL] = cubeList[LTR]
        rotatedCubeList[DTM] = cubeList[LMR]
        rotatedCubeList[DTR] = cubeList[LBR]
        #rotate left to bottom
        rotatedCubeList[RTL] = cubeList[DTR]
        rotatedCubeList[RML] = cubeList[DTM]
        rotatedCubeList[RBL] = cubeList[DTL]
        #rotate right to top
        rotatedCubeList[UBL] = cubeList[RTL]
        rotatedCubeList[UBM] = cubeList[RML]
        rotatedCubeList[UBR] = cubeList[RBL]
        self.cube = "".join(rotatedCubeList)

    def _rotateR(self):
        cubeList = list(self.cube)
        rotatedCubeList = cubeList[:]
        #rotate right face
        rotatedCubeList[RTL] = cubeList[RBL]
        rotatedCubeList[RTM] = cubeList[RML]
        rotatedCubeList[RTR] = cubeList[RTL]
        rotatedCubeList[RML] = cubeList[RBM]
        rotatedCubeList[RMM] = cubeList[RMM]
        rotatedCubeList[RMR] = cubeList[RTM]
        rotatedCubeList[RBL] = cubeList[RBR]
        rotatedCubeList[RBM] = cubeList[RMR]
        rotatedCubeList[RBR] = cubeList[RTR]
        #rotate up to right
        rotatedCubeList[BTL] = cubeList[UBR]
        rotatedCubeList[BML] = cubeList[UMR]
        rotatedCubeList[BBL] = cubeList[UTR]
        #rotate right to bottom
        rotatedCubeList[DTR] = cubeList[BBL]
        rotatedCubeList[DMR] = cubeList[BML]
        rotatedCubeList[DBR] = cubeList[BTL]
        #rotate bottom to left  
        rotatedCubeList[FTR] = cubeList[DTR]
        rotatedCubeList[FMR] = cubeList[DMR]
        rotatedCubeList[FBR] = cubeList[DBR]
        #rotate left to top
        rotatedCubeList[UTR] = cubeList[FTR]
        rotatedCubeList[UMR] = cubeList[FMR]
        rotatedCubeList[UBR] = cubeList[FBR]
        self.cube = "".join(rotatedCubeList)

    def _rotater(self):
        cubeList = list(self.cube)
        rotatedCubeList = cubeList[:]
        #rotate right face
        rotatedCubeList[RTL] = cubeList[RTR]
        rotatedCubeList[RML] = cubeList[RTM]
        rotatedCubeList[RBL] = cubeList[RTL]
        rotatedCubeList[RTM] = cubeList[RMR]
        rotatedCubeList[RMM] = cubeList[RMM]
        rotatedCubeList[RBM] = cubeList[RML]
        rotatedCubeList[RTR] = cubeList[RBR]
        rotatedCubeList[RMR] = cubeList[RBM]
        rotatedCubeList[RBR] = cubeList[RBL]
        #rotate up to left
        rotatedCubeList[FTR] = cubeList[UTR]
        rotatedCubeList[FMR] = cubeList[UMR]
        rotatedCubeList[FBR] = cubeList[UBR]
        #rotate bottom to right
        rotatedCubeList[BTL] = cubeList[DBR]
        rotatedCubeList[BML] = cubeList[DMR]
        rotatedCubeList[BBL] = cubeList[DTR]
        #rotate left to bottom
        rotatedCubeList[DTR] = cubeList[FTR]
        rotatedCubeList[DMR] = cubeList[FTM]
        rotatedCubeList[DBR] = cubeList[FBR]
        #rotate right to top
        rotatedCubeList[UTR] = cubeList[BBL]
        rotatedCubeList[UMR] = cubeList[BML]
        rotatedCubeList[UBR] = cubeList[BTL]
        self.cube = "".join(rotatedCubeList)




