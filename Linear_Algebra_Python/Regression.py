__author__ = 'abhisheksingh29895'

import numpy
import csv

def least_squares(X,Y):
# defining a vector of 1's of length(number of points)
    b = [1 for i in range(0,len(X))]
    b = numpy.array(b)
    A = numpy.column_stack((list(X),list(b)))
#Taking the transpose
    A_transpose = A.T
#Accepting the Y_values and multiplying them by A.transpose
    N = numpy.dot(A_transpose,Y)
    M = numpy.dot(A_transpose,A)
#Solving for the value of slope & Intercept in the matrix Z
    Z = numpy.linalg.solve(M,N)
#The value of slope is
    m = Z[0]
    print "The slope is ",m
    print ""
#The value of Intercept is
    b = Z[1]
    print "The intercept is ",b
    print ""
#Generating a vector of values for fitted Y
    Y_new = []
    Error =[]
    for i in range(0, len(X)):
        k = (X[i] * m) + b
        Y_new.append(k)
        E = (Y[i]- Y_new[i])**2
        Error.append(E)
#Sum of the squares of the observed Y values
    sum = 0
    for i in range(0, len(X)):
        sum = sum + Error[i]
    print sum
    print ""


#least_squares((1,2,3,4),(1.1,2.1,3.3,4.5)) dummy values
f = open('olympics.csv')
csv_f =csv.reader(f)

jump = csv_f[0]
for row in csv_f:

    print row

f.close()