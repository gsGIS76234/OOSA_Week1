#!/bin/env python3

# Purpose: implement sorting algorithm for array of random numbers

# Import packages
import numpy as np
import time

# Create random number array generator
def randArray(arrLen):
    """Creates array of random lengths, with length specified by user"""
    data = np.random.random((arrLen))
    return data

# Create example array of random numbers
exArray = randArray(5)

print(exArray)

# Develop function to find minimum number in array
def sortFunc(inpArr):
    """Sort numpy array into numerical order"""
    # Determine the length of the input array
    sizeArr = len(inpArr)
    # Loop through each entry in the array
    for i in range(0,sizeArr):
        # Initially, assume first element is the lowest value
        lowValIdx = i
        # For each element, compare value to subsequent elements
        for j in range(i+1, sizeArr):
            # If one of the subsequent elements is lower, change low index value
            if inpArr[j] < inpArr[lowValIdx]:
                lowValIdx = j
        # Once lowest value found, reorder array
        inpArr[i], inpArr[lowValIdx] = inpArr[lowValIdx], inpArr[i]
    return inpArr

# Initial time
t = time.clock()
# Create example sorted array
srtdArr = sortFunc(exArray)
t = time.clock() - t
print(f'Calculation took {t} seconds')
print(srtdArr)
