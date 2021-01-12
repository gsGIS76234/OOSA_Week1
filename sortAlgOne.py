#!/bin/env python3

# Purpose: implement sorting algorithm for array of random numbers

# Import packages
import numpy as np

# Create random number array generator
def randArray(arrLen):
    """Creates array of random lengths, with length specified by user"""
    data = np.random.random((arrLen))
    return data
