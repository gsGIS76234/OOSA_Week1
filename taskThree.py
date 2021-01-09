#!/bin/env python3

# Purpose: use nested loops to determine distances between squares

# Import the sqrt function
from math import sqrt

# Loop through x0
for x0 in range(1,9):
    # Loop through y0
    for y0 in range(1,9):
        #Loop through x1
        for x1 in range(1,9):
            # Loop through y1
            for y1 in range(1,9):
                if x0 == x1 and y0 == y1:
                    continue
                sqrDist = sqrt((x1-x0)**2+(y1-y0)**2)
                print(f'{x0},{y0} to {x1},{y1} distance {sqrDist}')
