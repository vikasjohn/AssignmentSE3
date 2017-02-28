import argparse
import urllib.request
import re 



filename = "input_assign3.txt"
print(filename)
with open(filename) as f:
    line = f.readline()
    value = line.strip().split()
    print(line)
    print(value)
x = int(line)
print(x)
