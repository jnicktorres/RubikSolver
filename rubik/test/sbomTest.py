'''
Created on Jan 19, 2023

@author: jnich
'''
import unittest
import app

class SbomTest(unittest.TestCase):


    def test_sbom_100_ShouldReturnAuthorName(self):
        author = 'jnt0024'
        result = app._getAuthor('../../')
        resultingAuthorName = result['author']
        self.assertEqual(resultingAuthorName,author)
