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
        
        self._rotateR()
        
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



