# iterators - Iterator in Python is any Python type that can be used with a ‘for in loop’
#iterables - the value will stored in memory location for iteration

# generators - it used to create the iterators using yield keyword - it used to create local variable values


from itertools import product

a = [2, 1, 3]
b = [4, 5, 6]

prod = product(a, b, )  # Cartersian product
prod1 = product(a, b, repeat=2)
print(list(prod))
print(list(prod1))

##############################################################
print("_______________________________________________________________________________")
#############################################################


from itertools import permutations

a = [1, 2, 3, 4, 5]
perm = permutations(a)   # order is important
print(list(perm))


#################################################################
print("_______________________________________________________________________________")
###############################################################


from itertools import combinations

b = [1, 2, 3, 4, 5]
comb = combinations(b, 2)  # order doesn't matter
print(list(comb))

###############################################################
print("_______________________________________________________________________________")
###############################################################
from itertools import combinations_with_replacement

comb1 = combinations_with_replacement(b, 2)
print(list(comb1))

#############################################################
print("_______________________________________________________________________________")
##############################################################
from itertools import accumulate


c = [1, 2, 3, 4, 5]
acc = accumulate(c, func=max)
print(list(acc))

##############################################################
print("_______________________________________________________________________________")
##############################################################
from  itertools import groupby

a = [1,2,3,45,5,6,7]

group = groupby(a,key=lambda x : x > 3)
for key  ,value in group:
    print(key,list(value))

from functools import reduce

a = [1,2,3,4]
prod = reduce(lambda x,y:x*y,a)
print(prod)
###############################################################
print("_______________________________________________________________________________")
###############################################################
# generators - It is the functions that return the object that can iterate over and generate items inside the object only one at a time and only ask for it , it is much more memory efficient deals with large data set

def my_generators():
    yield 1
    yield 2
    yield 3


def countdown(num):
    print('starting')
    while num > 0:
        yield num
        num -=1  # update the yield

cd = countdown(4)

value = next(cd)
print(value)

print(next(cd))
print(value)

##############################################################
print("_______________________________________________________________________________")
###############################################################

def first_n(n):
    nums= []
    num = 0
    while num <n:
        nums.append(num)
        num +=1
    return nums

def first_n_generator(n):
    num = 0
    while num <n:
        yield num
        num +=1


print(sum(first_n(10)))
print(sum(first_n_generator(10)))
################################################################
print("_______________________________________________________________________________")
#########################################################

import sys

print(sys.getsizeof(first_n(1000000)),'bytes')
print(sys.getsizeof(first_n_generator(1000000)),'bytes')

###################################################################
print("_______________________________________________________________________________")
###################################################################
