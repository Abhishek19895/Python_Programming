__author__ = 'abhisheksingh29895'

from numpy import *
import numpy

#Using numpy to create a Matrix out of a list from 1:100
A = [[((10*x)+(y+1)) for y in range(10)] for x in range(10)]
A = numpy.array(A)
print "A=",A
print " "

#Declaring the element v -array (1 to 10)
v=numpy.arange(1,11,1)
print "v=",v
print " "


#Declaring the element b -array (1 10 times)
b=[1 for i in range(10)]
b=numpy.array(b)
print "b=",b
print " "

#Now performing matrix operations
'''i have used the following url to take help of linalg syntax for this exersize
http://docs.scipy.org/doc/numpy/reference/routines.linalg.html
'''

print "Computing Av"
Av=numpy.dot(A,v)
print "Av=",Av
print " "


print "Solving using linalg Ax=b"
Ax_b=linalg.solve(A,b)
print "Ax=b",Ax_b
print " "

print "Solving using linalg Ax=v"
Ax_v=linalg.solve(A,v)
print "Ax=v",Ax_v
print " "

