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


    def test280_solve_topCorners(self):
            encodedCube = 'rrbybgwgbyoywrwrbrgggrgybyoryygobwobwrooybgbooowwwwgry'
            parms = {}
            parms['cube'] = encodedCube
            dirs = solve(parms)
            parms['dir'] = dirs['solution']
            result = rotate(parms)
            
    def test290_solve_topCorners(self):
            encodedCube = 'ggbobwrywyowrrwbowbbrggwggygbwboyobyyyooywryobrrrwggro'
            parms = {}
            parms['cube'] = encodedCube
            dirs = solve(parms)
            parms['dir'] = dirs['solution']
            result = rotate(parms)
            
    def test300_solve_topCorners(self):
            encodedCube = 'rrbybywwyoryoroowgbrbbgowbryoygogwboowrwyyggwgggrwbbyr'
            parms = {}
            parms['cube'] = encodedCube
            dirs = solve(parms)
            parms['dir'] = dirs['solution']
            result = rotate(parms)
