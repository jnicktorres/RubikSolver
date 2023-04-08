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


    def test160_solve_bottomlayer(self):
        encodedCube = 'ooowbrrgywobwrggygwgbwgryywrwybobgywyrroybbybgorbwgoro'
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
        self.assertEqual(result.get('cube')[4], result.get('cube')[6])
        self.assertEqual(result.get('cube')[4], result.get('cube')[7])
        self.assertEqual(result.get('cube')[4], result.get('cube')[8])
        self.assertEqual(result.get('cube')[13], result.get('cube')[15])
        self.assertEqual(result.get('cube')[13], result.get('cube')[16])
        self.assertEqual(result.get('cube')[13], result.get('cube')[17])
        self.assertEqual(result.get('cube')[22], result.get('cube')[24])
        self.assertEqual(result.get('cube')[22], result.get('cube')[25])
        self.assertEqual(result.get('cube')[22], result.get('cube')[26])
        self.assertEqual(result.get('cube')[31], result.get('cube')[33])
        self.assertEqual(result.get('cube')[31], result.get('cube')[34])
        self.assertEqual(result.get('cube')[31], result.get('cube')[35])        

