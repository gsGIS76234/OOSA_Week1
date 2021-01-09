#!/bin/env python3

# Purpose: use nested loops to print out chess board coords

# For loop for x-axis
for x in range(1,9):
    # For loop for y-axis
    for y in range(1,9):
        print(f'({x},{y})')
