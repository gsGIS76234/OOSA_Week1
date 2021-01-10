#!/bin/env python3

# Purpose: read in data from data.txt and make scatterplot

# Import necessary packages
import numpy as np
from matplotlib import pyplot as plt

# Use load text to read data into two np arrays, x and y
filename = "/home/s0838123/src/OOSA/OOSA-code-public/data/data.txt"
x, y = np.loadtxt(filename, unpack=True, dtype=int, usecols=(0,1))

# Use pyplot to develop a basic scatterplot
plt.scatter(x,y)
plt.title("Plot of 'data.txt'", fontweight = "bold")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()
