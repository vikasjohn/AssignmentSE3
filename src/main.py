import argparse
import urllib.request
import re 
import numpy as np
from textwrap import fill

''' reading the file  form the src file'''
filename = "input_assign3.txt"
print(filename)
with open(filename) as f:
    line = f.readline(25)
    value = line.strip().split()
#    print(line)
#   print(value)
#x = int(line)
#print(x)
a2d = [ list(range(i*10, i*10 + 10)) for i in range(10) ]
# print(a2d)

L = int(line)
print(L)
#grid = [[False] * 10 for i in range(10)]
#ledGrid = np.array(grid)
#print(grid)
#print(ledGrid)

#grid = 0
#fill = False
#for i in range(L):
 #   for j in range(L):
#        grid [i][j] = fill
        
#print(grid)
    
Grid_Array=[[0]*L for _ in range(L)]
#print(Grid_Array)