__author__ = 'abhisheksingh29895'
#I have used Prof. Jan Reiman's code for solving this problem
# "http://stackoverflow.com/questions/5889142/python-numpy-scipy-finding-the-null-space-of-a-matrix"

import numpy as np

def BasisCompute(A,b):

#Performing operations for matrix elements, Computing rank through the linalg matrix rank function
    rank = np.linalg.matrix_rank(A)
    print "Rank of the matrix is ",rank
    print ""

#estimating the dimension of the matrix
    matrix_shape = np.shape(A)
    rows = matrix_shape[0]
    cols = matrix_shape[1]
    print "Rows of a matrix are ",rows,"and cols are ",cols
    print ""

#Checking the solution type
    if cols != len(b):
        print "LinAlgErr"
        print " "
        print "Quitting the program"
        raise SystemExit

    else:
#Checking for if the matrix is solvable by first testing if it has a non-zero determinant
        if np.linalg.det(A)==0:
            print "Determinant is 0, hence not solvable"
            print " "
            print "Quitting the program"
            raise SystemExit
        else:
#Printing the solutions for such a matrix, which is solvable
            Ax_b = np.linalg.solve(A,b)
            print " Solutions for Ax_b is ",Ax_b
            print " "
            u, s, vh = np.linalg.svd(A)
            null_mask = (s <= 1e-15)
            null_space = np.compress(null_mask, vh, axis=0)
            print "The null space is:",null_space
            print " "

BasisCompute(A=[[-2, -2, 1],[1, 0, 2], [1, 1, 4]], b=[3,3,3])
#BasisCompute(A=[[1,1,1,1,1],[1, 2, 5,1,6], [2, 1, 2,1,1],[3, 1, 7,1,5],[4, 3, 6,8,9]], b=[3,2,3,4,5])

