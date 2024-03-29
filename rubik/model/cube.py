from rubik.model.constants import *

class Cube:
    '''
    Rubik's cube
    '''
    def __init__(self, encodedCube):
        self.cube = encodedCube
        
    def rotate(self, directions):
        
        # iterate through each direction and find corresponding rotation
        for i in directions:
            if i == 'F':
                self._rotateF()
            elif i == 'f':
                self._rotatef()
            elif i == 'R':
                self._rotateR()
            elif i == 'r':
                self._rotater()
            elif i == 'B':
                self._rotateB()
            elif i == 'b':
                self._rotateb()
            elif i == 'L':
                self._rotateL()
            elif i == 'l':
                self._rotatel()
            elif i == 'U':
                self._rotateU()
            elif i == 'u':
                self._rotateu()
            elif i == 'D':
                self._rotateD()
            elif i == 'd':
                self._rotated()    
            
        
        return self.cube
        
        
    def get(self):
        return self.cube
    
    def _rotateF(self):
        cubeList = list(self.cube)
        rotatedCubeList = cubeList[:]
        #rotate left face       
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
        return self.cube

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
        return self.cube

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
        return self.cube 
      
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
        rotatedCubeList[DMR] = cubeList[FMR]
        rotatedCubeList[DBR] = cubeList[FBR]
        #rotate right to top
        rotatedCubeList[UTR] = cubeList[BBL]
        rotatedCubeList[UMR] = cubeList[BML]
        rotatedCubeList[UBR] = cubeList[BTL]
        self.cube = "".join(rotatedCubeList)
        return self.cube
    
    def _rotateB(self):
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
    
    def _rotateb(self):
        cubeList = list(self.cube)
        rotatedCubeList = cubeList[:]
        #rotate back face
        rotatedCubeList[BTL] = cubeList[BTR]
        rotatedCubeList[BTM] = cubeList[BMR]
        rotatedCubeList[BTR] = cubeList[BBR]
        rotatedCubeList[BML] = cubeList[BTM]
        rotatedCubeList[BMM] = cubeList[BMM]
        rotatedCubeList[BMR] = cubeList[BBM]
        rotatedCubeList[BBL] = cubeList[BTL]
        rotatedCubeList[BBM] = cubeList[BML]
        rotatedCubeList[BBR] = cubeList[BBL]
        #rotate up to right
        rotatedCubeList[RTR] = cubeList[UTL]
        rotatedCubeList[RMR] = cubeList[UTM]
        rotatedCubeList[RBR] = cubeList[UTR]
        #rotate bottom to left
        rotatedCubeList[DBR] = cubeList[RTR]
        rotatedCubeList[DBM] = cubeList[RMR]
        rotatedCubeList[DBL] = cubeList[RBR]
        #rotate right to bottom
        rotatedCubeList[LTL] = cubeList[DBL]
        rotatedCubeList[LML] = cubeList[DBM]
        rotatedCubeList[LBL] = cubeList[DBR]
        #rotate left to top
        rotatedCubeList[UTL] = cubeList[LBL]
        rotatedCubeList[UTM] = cubeList[LML]
        rotatedCubeList[UTR] = cubeList[LTL]
        self.cube = "".join(rotatedCubeList)
        return self.cube
    
    def _rotateL(self):
        cubeList = list(self.cube)
        rotatedCubeList = cubeList[:]
        #rotate left face
        rotatedCubeList[LTL] = cubeList[LBL]
        rotatedCubeList[LML] = cubeList[LBM]
        rotatedCubeList[LBL] = cubeList[LBR]
        rotatedCubeList[LBM] = cubeList[LMR]
        rotatedCubeList[LMM] = cubeList[LMM]
        rotatedCubeList[LTM] = cubeList[LML]
        rotatedCubeList[LTR] = cubeList[LTL]
        rotatedCubeList[LMR] = cubeList[LTM]
        rotatedCubeList[LBR] = cubeList[LTR]
        #rotate up to right
        rotatedCubeList[FTL] = cubeList[UTL]
        rotatedCubeList[FML] = cubeList[UML]
        rotatedCubeList[FBL] = cubeList[UBL]
        #rotate bottom to left
        rotatedCubeList[DTL] = cubeList[FTL]
        rotatedCubeList[DML] = cubeList[FML]
        rotatedCubeList[DBL] = cubeList[FBL]
        #rotate right to bottom
        rotatedCubeList[BTR] = cubeList[DBL]
        rotatedCubeList[BMR] = cubeList[DML]
        rotatedCubeList[BBR] = cubeList[DTL]
        #rotate left to top
        rotatedCubeList[UTL] = cubeList[BBR]
        rotatedCubeList[UML] = cubeList[BMR]
        rotatedCubeList[UBL] = cubeList[BTR]
        self.cube = "".join(rotatedCubeList)
        return self.cube
    
    def _rotatel(self):
        cubeList = list(self.cube)
        rotatedCubeList = cubeList[:]
        #rotate left face
        rotatedCubeList[LTL] = cubeList[LTR]
        rotatedCubeList[LTM] = cubeList[LMR]
        rotatedCubeList[LTR] = cubeList[LBR]
        rotatedCubeList[LML] = cubeList[LTM]
        rotatedCubeList[LMM] = cubeList[LMM]
        rotatedCubeList[LMR] = cubeList[LBM]
        rotatedCubeList[LBL] = cubeList[LTL]
        rotatedCubeList[LBM] = cubeList[LML]
        rotatedCubeList[LBR] = cubeList[LBL]
        #rotate up to right
        rotatedCubeList[FTL] = cubeList[DTL]
        rotatedCubeList[FML] = cubeList[DML]
        rotatedCubeList[FBL] = cubeList[DBL]
        #rotate bottom to left
        rotatedCubeList[DTL] = cubeList[BBR]
        rotatedCubeList[DML] = cubeList[BMR]
        rotatedCubeList[DBL] = cubeList[BTR]
        #rotate right to bottom
        rotatedCubeList[BTR] = cubeList[UBL]
        rotatedCubeList[BMR] = cubeList[UML]
        rotatedCubeList[BBR] = cubeList[UTL]
        #rotate left to top
        rotatedCubeList[UTL] = cubeList[FTL]
        rotatedCubeList[UML] = cubeList[FML]
        rotatedCubeList[UBL] = cubeList[FBL]
        self.cube = "".join(rotatedCubeList)
        return self.cube
    
    def _rotateU(self):
        cubeList = list(self.cube)
        rotatedCubeList = cubeList[:]
        #rotate u face
        rotatedCubeList[UTL] = cubeList[UBL]
        rotatedCubeList[UTM] = cubeList[UML]
        rotatedCubeList[UTR] = cubeList[UTL]
        rotatedCubeList[UML] = cubeList[UBM]
        rotatedCubeList[UMM] = cubeList[UMM]
        rotatedCubeList[UMR] = cubeList[UTM]
        rotatedCubeList[UBL] = cubeList[UBR]
        rotatedCubeList[UBM] = cubeList[UMR]
        rotatedCubeList[UBR] = cubeList[UTR]
        #rotate up to right
        rotatedCubeList[FTL] = cubeList[RTL]
        rotatedCubeList[FTM] = cubeList[RTM]
        rotatedCubeList[FTR] = cubeList[RTR]
        #rotate bottom to left
        rotatedCubeList[RTL] = cubeList[BTL]
        rotatedCubeList[RTM] = cubeList[BTM]
        rotatedCubeList[RTR] = cubeList[BTR]
        #rotate right to bottom
        rotatedCubeList[BTL] = cubeList[LTL]
        rotatedCubeList[BTM] = cubeList[LTM]
        rotatedCubeList[BTR] = cubeList[LTR]
        #rotate left to top
        rotatedCubeList[LTL] = cubeList[FTL]
        rotatedCubeList[LTM] = cubeList[FTM]
        rotatedCubeList[LTR] = cubeList[FTR]
        self.cube = "".join(rotatedCubeList)
        return self.cube
    
    def _rotateu(self):
        cubeList = list(self.cube)
        rotatedCubeList = cubeList[:]
        #rotate u face
        rotatedCubeList[UTL] = cubeList[UTR]
        rotatedCubeList[UML] = cubeList[UTM]
        rotatedCubeList[UBL] = cubeList[UTL]
        rotatedCubeList[UTM] = cubeList[UMR]
        rotatedCubeList[UMM] = cubeList[UMM]
        rotatedCubeList[UBM] = cubeList[UML]
        rotatedCubeList[UTR] = cubeList[UBR]
        rotatedCubeList[UMR] = cubeList[UBM]
        rotatedCubeList[UBR] = cubeList[UBL]
        #rotate up to right
        rotatedCubeList[FTL] = cubeList[LTL]
        rotatedCubeList[FTM] = cubeList[LTM]
        rotatedCubeList[FTR] = cubeList[LTR]
        #rotate bottom to left
        rotatedCubeList[RTL] = cubeList[FTL]
        rotatedCubeList[RTM] = cubeList[FTM]
        rotatedCubeList[RTR] = cubeList[FTR]
        #rotate right to bottom
        rotatedCubeList[BTL] = cubeList[RTL]
        rotatedCubeList[BTM] = cubeList[RTM]
        rotatedCubeList[BTR] = cubeList[RTR]
        #rotate left to top
        rotatedCubeList[LTL] = cubeList[BTL]
        rotatedCubeList[LTM] = cubeList[BTM]
        rotatedCubeList[LTR] = cubeList[BTR]
        self.cube = "".join(rotatedCubeList)
        return self.cube
    
    def _rotateD(self):
        cubeList = list(self.cube)
        rotatedCubeList = cubeList[:]
        #rotate u face
        rotatedCubeList[DTR] = cubeList[DTL]
        rotatedCubeList[DMR] = cubeList[DTM]
        rotatedCubeList[DBR] = cubeList[DTR]       
        rotatedCubeList[DTM] = cubeList[DML]
        rotatedCubeList[DMM] = cubeList[DMM]
        rotatedCubeList[DBM] = cubeList[DMR]              
        rotatedCubeList[DTL] = cubeList[DBL]
        rotatedCubeList[DML] = cubeList[DBM]
        rotatedCubeList[DBL] = cubeList[DBR]       
        #rotate up to right
        rotatedCubeList[RBL] = cubeList[FBL]
        rotatedCubeList[RBM] = cubeList[FBM]
        rotatedCubeList[RBR] = cubeList[FBR]        
        #rotate bottom to left
        rotatedCubeList[BBL] = cubeList[RBL]
        rotatedCubeList[BBM] = cubeList[RBM]
        rotatedCubeList[BBR] = cubeList[RBR]
        #rotate right to bottom
        rotatedCubeList[LBL] = cubeList[BBL]
        rotatedCubeList[LBM] = cubeList[BBM]
        rotatedCubeList[LBR] = cubeList[BBR]
        #rotate left to top
        rotatedCubeList[FBL] = cubeList[LBL]
        rotatedCubeList[FBM] = cubeList[LBM]
        rotatedCubeList[FBR] = cubeList[LBR]
        self.cube = "".join(rotatedCubeList)
        return self.cube
    
    def _rotated(self):
        cubeList = list(self.cube)
        rotatedCubeList = cubeList[:]
        #rotate u face
        rotatedCubeList[DTL] = cubeList[DTR]
        rotatedCubeList[DML] = cubeList[DTM]
        rotatedCubeList[DBL] = cubeList[DTL]    
        rotatedCubeList[DTM] = cubeList[DMR]
        rotatedCubeList[DMM] = cubeList[DMM]
        rotatedCubeList[DBM] = cubeList[DML]          
        rotatedCubeList[DTR] = cubeList[DBR]
        rotatedCubeList[DMR] = cubeList[DBM]
        rotatedCubeList[DBR] = cubeList[DBL]
        
        #rotate up to right
        rotatedCubeList[RBL] = cubeList[BBL]
        rotatedCubeList[RBM] = cubeList[BBM]
        rotatedCubeList[RBR] = cubeList[BBR]
        
        #rotate bottom to left
        rotatedCubeList[BBL] = cubeList[LBL]
        rotatedCubeList[BBM] = cubeList[LBM]
        rotatedCubeList[BBR] = cubeList[LBR]
        #rotate right to bottom
        rotatedCubeList[LBL] = cubeList[FBL]
        rotatedCubeList[LBM] = cubeList[FBM]
        rotatedCubeList[LBR] = cubeList[FBR]
        
        #rotate left to top
        rotatedCubeList[FBL] = cubeList[RBL]
        rotatedCubeList[FBM] = cubeList[RBM]
        rotatedCubeList[FBR] = cubeList[RBR]
        self.cube = "".join(rotatedCubeList)
        return self.cube









