#!/bin/env python3

# Purpose: use nested loops to print square coords and colours

# Loop through x-coords
for x in range(1,9):
    # Loop through y-coords
    for y in range(1,9):
        # Odd x and odd y coords are black
        if x%2 == 1 and y%2 == 1:
            sqVal = "Black"
        # Odd x and even y coords are white
        elif x%2 == 1 and y%2 == 0:
            sqVal = "White"
        # Even x and even y coords are black
        elif x%2 == 0 and y%2 == 0:
            sqVal = "Black"
        # Even x and odd y coords are white
        elif x%2 == 0 and y%2 == 1:
            sqVal = "White"
        print(f'Square ({x},{y}) is {sqVal}')
