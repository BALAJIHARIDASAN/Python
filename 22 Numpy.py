import numpy as np

a = np.array([1,2,3,4,5])  # creating the numpy array as integer
print(a)

b = np.array([1.2,3.3,2,6,65,25])  # creating the numpy as float
print(b)

np.zeros(10) # creating the integer filled with zeros
np.ones((3,5),dtype='float')  #  create a 3*5 floating point array with 1's

np.arange(0,20,2)  # create a array starting at 0 and ending at 20 stepping by 2
np.linspace(0,1,5)  # create array of five values evenly spaced between 0 and 1
np.random.random((3,3))  # create a array of uniformly distributed values
np.random.randint(0,10,(3,3))  # create a random integer in the interval of [0,10)
np.eye(3)  # create a identity matrix

###################################################################################
print("______________________________________________________________________________")
################################################################################

c = np.array([1,2,3,4,5],dtype='float')  # explicitly setting the data type
print(c)

###################################################################################
print("______________________________________________________________________________")
################################################################################
d = np.array([range(i,i+3) for i in [2,4,5]])  # create a multidimensional array
print(d)

###################################################################################
print("______________________________________________________________________________")
################################################################################

x1 = np.random.randint(10,size=6)   # one dimensional array
print(x1)
x2 = np.random.randint(10,size = (3,4))  # two dimensional array
print(x2)
x3 = np.random.randint(10,size = (3,4,5))  # three dimensional array
print(x3)

print('dimension',x1.ndim)  # print the number of dimensions
print('shape of the array',x3.shape)  # the size of the each dimensions
print('size of the array',x3.size)  # total size of the array
print('dtype',x3.dtype)  # data type of the array
print(x3.itemsize) # total array size of each array element
print(x3.nbytes,'bytes')  # total size in bytes

###################################################################################
print("______________________________________________________________________________")
################################################################################

# Indexing the array

# one dimensional array

print('first element is :',x1[0])
print('last element is :',x1[-1])

# two dimensional array

print(x2)
print('element in the first row and first column :',x2[0,0])
print('element in the thrid row and first column :',x2[2,0])
print('element in the second row and third column :',x2[1,2])

###################################################################################
print("______________________________________________________________________________")
################################################################################

# slicing the array - x[start : stop : step]

print('first five element :',x1[:5])
print('element after index 5 :',x1[5:])
print('middle subarray',x1[4:7])
print('every other element',x1[::2])
print('every other element starting at index 1 :',x1[1::2])
print( 'all element reversed :',x1[:-1])

# mutidimensional subarray

print(x2[:2,:3])  # two rows and three columns
print(x2[:3,::2])  # all rows and every other columns
print(x2[::-1,::-1])

###################################################################################
print("______________________________________________________________________________")
################################################################################

# reshaping the arrays

grid = np.arange(1,10).reshape((3,3))
print(grid)

x4 = np.array([1,2,3])
x4.reshape((1,3))
print(x4)

###################################################################################
print("______________________________________________________________________________")
################################################################################

# Array concatenation and splitting

x = np.array([1,2,3])
y = np.array([3,2,1])
z = np.concatenate([x,y])  #
print('after contatination :',z)

a1 = np.array([1,2,3])
b1 = np.array([[9,8,7],
               [6,5,4]])
c1 = np.vstack([a1,b1]) # vertically stack the array
print(c1)

a2 = np.array([[99],
               [99]])
c2 = np.hstack([a2,b1])  # horizontally stack the array
print(c2)

###################################################################################
print("______________________________________________________________________________")
################################################################################
# U FUNCTIONS - VECTORIZIED OPERATIONS - UNARY FUNCTIONS

s1 = 5
s2 = 10

# arithmetic operations
s3= np.add(s1,s2)
s4= np.subtract(s1,s2)
s5 = np.multiply(s1,s2)
s6 = np.divide(s1,s2)
s7 = np.floor_divide(s1,s2)
s8 = np.power(s1,s2)
s9 = np.mod(s1,s2)

for i3 in [s3,s4,s5,s6,s7,s8,s9]:
    print(i3)

s10 = [-1,-2,-3,-4,-5,0,1,2,3,4,5]
s11 = np.abs(s10) # it return only the magnitude not the sign
print(s11)

###################################################################################
print("______________________________________________________________________________")
###############################################################################

# trigonometric functions

print(np.sin(10))
print(np.cos(10))
print(np.tan(10))

# inverse theta

print(np.arcsin(12))
print(np.arctan(10))
print(np.cos(120))

# exponents

print(np.exp(2))
print(np.exp2(25))
print(np.power(20))

# logarithmic

print(np.log(20))
print(np.log2(20))
print(np.log10(20))

# special functions

from scipy import special

s13 = [1,2,3,4,5]
print(special.gamma(s13))  # gamma functions and related functions
print(special.gammaln(s13))
print(special.beta(s13,2))

