from unittest import TestCase
from rubik.view.solve import solve
from rubik.view.rotate import rotate
from rubik.model.cube import Cube
 
'''
Created on Apr 8, 2023

@author: jnich
'''
import unittest


class Test(unittest.TestCase):


    #--------------------------------------- def test280_solve_topCorners(self):
            # encodedCube = 'rrbybgwgbyoywrwrbrgggrgybyoryygobwobwrooybgbooowwwwgry'
            #-------------------------------------------------------- parms = {}
            #--------------------------------------- parms['cube'] = encodedCube
            #----------------------------------------------- dirs = solve(parms)
            #----------------------------------- parms['dir'] = dirs['solution']
            #-------------------------------------------- result = rotate(parms)
            
    def test290_solve_FinishedCube(self):
            encodedCube = 'ggbobwrywyowrrwbowbbrggwggygbwboyobyyyooywryobrrrwggro'
            parms = {}
            parms['cube'] = encodedCube
            dirs = solve(parms)
            parms['dir'] = dirs['solution']
            result = rotate(parms)
            self.assertEqual('w', result.get('cube')[45])
            self.assertEqual('w', result.get('cube')[46])
            self.assertEqual('w', result.get('cube')[47])
            self.assertEqual('w', result.get('cube')[48])
            self.assertEqual('w', result.get('cube')[50])
            self.assertEqual('w', result.get('cube')[51])
            self.assertEqual('w', result.get('cube')[52])
            self.assertEqual('w', result.get('cube')[53])
            self.assertEqual(result.get('cube')[4], result.get('cube')[0])
            self.assertEqual(result.get('cube')[4], result.get('cube')[1])
            self.assertEqual(result.get('cube')[4], result.get('cube')[2])
            self.assertEqual(result.get('cube')[4], result.get('cube')[3])
            self.assertEqual(result.get('cube')[4], result.get('cube')[5])
            self.assertEqual(result.get('cube')[4], result.get('cube')[6])
            self.assertEqual(result.get('cube')[4], result.get('cube')[7])
            self.assertEqual(result.get('cube')[4], result.get('cube')[8])
            self.assertEqual(result.get('cube')[13], result.get('cube')[9])
            self.assertEqual(result.get('cube')[13], result.get('cube')[10])
            self.assertEqual(result.get('cube')[13], result.get('cube')[11])
            self.assertEqual(result.get('cube')[13], result.get('cube')[12])
            self.assertEqual(result.get('cube')[13], result.get('cube')[14])
            self.assertEqual(result.get('cube')[13], result.get('cube')[15])
            self.assertEqual(result.get('cube')[13], result.get('cube')[16])
            self.assertEqual(result.get('cube')[13], result.get('cube')[17])
            self.assertEqual(result.get('cube')[22], result.get('cube')[18])
            self.assertEqual(result.get('cube')[22], result.get('cube')[19])
            self.assertEqual(result.get('cube')[22], result.get('cube')[20])
            self.assertEqual(result.get('cube')[22], result.get('cube')[21])
            self.assertEqual(result.get('cube')[22], result.get('cube')[23])
            self.assertEqual(result.get('cube')[22], result.get('cube')[24])
            self.assertEqual(result.get('cube')[22], result.get('cube')[25])
            self.assertEqual(result.get('cube')[22], result.get('cube')[26])
            self.assertEqual(result.get('cube')[31], result.get('cube')[27])
            self.assertEqual(result.get('cube')[31], result.get('cube')[28])
            self.assertEqual(result.get('cube')[31], result.get('cube')[29])
            self.assertEqual(result.get('cube')[31], result.get('cube')[30])
            self.assertEqual(result.get('cube')[31], result.get('cube')[32])
            self.assertEqual(result.get('cube')[31], result.get('cube')[33])
            self.assertEqual(result.get('cube')[31], result.get('cube')[34])
            self.assertEqual(result.get('cube')[31], result.get('cube')[35])
            self.assertEqual(result.get('cube')[40], result.get('cube')[36])
            self.assertEqual(result.get('cube')[40], result.get('cube')[37])
            self.assertEqual(result.get('cube')[40], result.get('cube')[38])
            self.assertEqual(result.get('cube')[40], result.get('cube')[39])
            self.assertEqual(result.get('cube')[40], result.get('cube')[41])
            self.assertEqual(result.get('cube')[40], result.get('cube')[42])
            self.assertEqual(result.get('cube')[40], result.get('cube')[43])
            self.assertEqual(result.get('cube')[40], result.get('cube')[44])  
