'''
Created on 2 Mar 2017

@author: vikas

from nose.tools import *
from src.main import *

 Make Test
   
'''
    
import unittest
from src.main import LightsOn


class Test(unittest.TestCase):
    
    def test_count(self):
        self.assertEqual(LightsOn([[True, True, True], [True, True, True], [True, True, True]]), 9)
        
        
   
        
        
 
if __name__ == "__main__":
   
    unittest.main() 
    
    
    
    
    
    
    
    
    
    
'''
RESULTS
uri = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt"
['http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt', 400410]
uri2 = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_a.txt"
['http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_a.txt', 6]
uri3 = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_b.txt"
['http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_b.txt', 29942250]
uri4 = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_c.txt"
['http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_c.txt', 477452]
uri5 = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_d.txt"
['http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_d.txt', 349037]
 
'''