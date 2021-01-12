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
exArray = randArray(50)

print(exArray)

# Develop function to find minimum number in array
def sortFunc(inpArr):
    """Sort numpy array into order"""
    # Create empty array to append results to
    outList = []
    # Determine length of input array
    arrLen = len(inpArr)
    # Loop through the input array
    for i in range(arrLen):
        # Find the min number in input array
        minNo = np.amin(inpArr)
        # Append lowest number to output list
        outList.append(minNo)
        # Remove number from input array
        inpArr = inpArr[inpArr != minNo]
    # Convert output list to array
    outArr = np.array(outList)
    # Return the output array
    return outArr

print(sortFunc(exArray))
