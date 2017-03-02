'''
Created on 28 Feb 2017

@author: vikas
'''


import numpy as np
import argparse
import urllib.request
import time
import os

print(os.path.exists('input_assign3.txt'))

'''
def read_uri(fname):
    #Read in a website
    if fname.startswith('http'):
        return buffer(fname)
    else:
        #Read in a file on the instance
        return open(fname).read()
    
def buffer(filename):
    #Buffer the website for reading
    uri = filename
    req = urllib.request.urlopen(uri)
    buffer = req.read().decode('utf-8')
    return buffer

def parse():
    #Parse in an input command for the CLI
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', help='input help')
    args = parser.parse_args()
    
    filename = args.input
    return filename

'''
#to turn the light on
def turn_on(x1,y1,x2,y2,ledGrid):
    """ This function checks the given block of light are turned on (true) """
    for row in range(y1,y2+1):
        for col in range(x1,x2+1):
            if ledGrid[row][col] == False:
                ledGrid[row][col] = True
    return ledGrid
    



#To turns the lights off
def turn_off(x1,y1,x2,y2,ledGrid):
    """ This function checks the block and turned the light off (False) """
    for row in range(y1,y2+1):
        for col in range(x1,x2+1):
            if ledGrid[row][col] == True:
                ledGrid[row][col] = False
    return ledGrid

#To turn the status of lights to opposite.
def switch(x1,y1,x2,y2,ledGrid):
    """ This function changes the status to opposite, from off to on or from on to off."""
    for row in range(y1,y2+1):
        for col in range(x1,x2+1):
            if ledGrid[row][col] == True:
                ledGrid[row][col] = False
            elif ledGrid[row][col] == False:
                ledGrid[row][col] = True
                
    return ledGrid


def main():
   
    start_time = time.time()
    print("The Project is now running: ") 
       
    filename = "input_assign3.txt"
    with open(filename) as f:
        first_line = f.readline()  
        L = int(first_line) # to get the value of L as integers
        grid = [[False] * L for i in range(L)]
        ledGrid = np.array(grid) # to create the grid as in matrix form.
        #for i, line in enumerate(f), run the loop to read the lines
        for line in f.readlines():
            line = line.replace(',', ' ') 
            values = line.strip().split()
            
           
            if (line.startswith("turn on")):
                x1 = int(values[2])
                y1 = int(values[3])
                x2 = int(values[5])
                y2 = int(values[6])
                    # to check the limits of values
                if x1 < 0:
                    x1 = 0
                if x2 >= L:
                    x2 = L-1
                if y1 < 0:
                    y1 = 0
                if y2 >= L:
                    y2 = L-1
    

                ledGridOutput = turn_on(x1, y1, x2, y2, ledGrid)
         
            elif line.startswith("turn off"):
                x1 = int(values[2])
                y1 = int(values[3])
                x2 = int(values[5])
                y2 = int(values[6])
                if x1 < 0:
                    x1 = 0
                if x2 >= L:
                    x2 = L-1
                if y1 < 0:
                    y1 = 0
                if y2 >= L:
                    y2 = L-1
    
                ledGridOutput = turn_off(x1, y1, x2, y2, ledGrid)
                 
                #Values[0] will be the first item in the line, if it is switch assign values
            elif line.startswith("switch"):
                x1 = int(values[1])
                y1 = int(values[2])
                x2 = int(values[4])
                y2 = int(values[5])
                if x1 < 0:
                    x1 = 0
                if x2 >= L:
                    x2 = L-1
                if y1 < 0:
                    y1 = 0
                if y2 >= L:
                    y2 = L-1
    
                ledGridOutput = switch(x1, y1, x2, y2, ledGrid)
            
            #else:
            #continue


    
       
    print("The number of lights on are: ", LightsOn(ledGridOutput))
    print("Finished program")
    end_time = time.time()
    print(end_time - start_time)  
    
def LightsOn(ledGridOutput):
    count = 0
    for row in ledGridOutput:
        for col in row:
            if col == True:
                count += 1
    return count     
    
if __name__ == "__main__":
    main()