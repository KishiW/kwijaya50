## Heading
# start 10:27

from pprint import pprint
import math
import random

def readFile(fileName):
    data = open(fileName).read() # store raw file as text
    array = data.split("\n")[1:-2] # split by line breaks, exclude title and total
    
    for i in range(len(array)):
        temp = array[i].rsplit(",", 1) # temporary list holds job and %
        
        if temp[0][0]== "\"":
            temp[0] = temp[0][1:-1] # remove quotes
            
        temp[1] = float(temp[1]) # make the percentage a number
        array[i] = temp # feed into the array
        
    return array

def makeDict(filename): # makes the dictionary
    data = readFile(filename)
    result = {}
    for i in data:
        result.update({i[0]: i[1]})
    return result

def rand(filename):  # sets up the randomization
    data = makeDict(filename)
    n = 0.0
    temp = {}
    keys = list(data.keys())
    
    values = list(data.values())
    
    for i in range(len(keys)):  # sets up the random dictionary --> list of numbers, we pick a number in between them to simulate the random chance
        y = round(values[i], 1)
        temp.update({keys[i]: round(y+n, 1)})
        n += y
        
    radm = (math.trunc((random.random() * 998)))/10
    
    job = ""
    percentvalues = list(temp.values())

    for i in range(len(keys)): # goes through the dictionary and ends the loop when it is less than or equal to the given percentage
        if radm <= percentvalues[i]:
            job = keys[i]
            break
    
    return job
        


print(rand("occupations.csv"))