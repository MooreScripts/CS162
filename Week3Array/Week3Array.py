import numpy as np
import random

#1 Generate a random 2-dimensional numpy integer array with dimensions 5x5
matrix = np.random.randint(0, 100, size=(5,5))

#2 Print the array
print("\033[31mprinting randomized 5x5 array\033[0m", "\n", matrix)

#3 Print the number from the 2nd row, 3rd column, index starts at 0 in numpy

print("\033[31mPrinting the value from 2nd row, 3rd column:\033[0m", matrix[1, 2])

#Print the sum of all the elements in the array
print("\033[31mPrint the sum of all elements\033[0m", matrix.sum())

#print the average of each row. axis=0 performs operation on rows, while an axis=1 would operate on columns
print("\033[31mprint the average of each row\033[0m", matrix.mean(axis=0))

#Print the max value of each column. Axis=1 puts operation on columns

print("\033[31mprinting the max value of each column: \033[0m",matrix.max(axis=1))




