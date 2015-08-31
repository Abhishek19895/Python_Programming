__author__ = 'abhisheksingh29895'

#I have used the below url's to help do this
# "http://stackoverflow.com/questions/21407620/numpy-create-fill-with-random-binary-data"
# "http://stackoverflow.com/questions/5622976/how-do-you-calculate-program-run-time-in-python"

#Mathematical operations
import numpy as np
#for permutations
import itertools as iter
#To track speed of function execution
import timeit

#Generating a random matrix through a function
def matrix_generator(n):
    start = timeit.default_timer()
    length = n**2
    combinations = [list(seq) for seq in iter.product("01", repeat = length)]
    Invert = []
    Non_Invert = []
    for j in range(0, len(combinations)):
        a = [int(i) for i in combinations[j]]
        matrix = np.mat(a).reshape((n, n))
        if np.linalg.det(matrix)==0:
            Non_Invert.append(matrix)
        else:
            Invert.append(matrix)
#Printing the total number of binary matrixes possible
    total_matrixes = (len(Invert)+ len(Non_Invert))
    print "The total number of binary matrixes is ",total_matrixes
#Printing the total number of Invertible binary matrixes possible
    total_Invertible = len(Invert)
    print "The total number of Invertible binary matrixes is ",total_Invertible
#Printing the probability of getting an invertible matrix
    probability = float(total_Invertible)/total_matrixes
#Time for function execution
    stop = timeit.default_timer()
    print "The probability of Invertibility at rank ",n,"is ",float(probability)
#Calculating the time taken to perform this operation
    print("--- %s seconds taken---" % (stop - start))


#Enter order of the matrix in function parameter
matrix_generator(5)


