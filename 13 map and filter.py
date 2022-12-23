#  Map and Filter functions
# basic difference - map gives the boolean values but filter gives the output as filtered list


def double(a_list):
    list = []
    for i in a_list:
        element = 2 * i
        list.append(element)
    return list


things = [2, 9, 6]
print(things)
new = double(things)
print("Using Normal Function Method :", new)

#################################################################################################################
print("____________________________________________________________________________________________________")
#####################################################################################################################

# Map - The Map function is for accumulation - parse the function within the function
# it maps the given function to items in iterable and return the list of result

# map(lambda_expression, sequence)

sample = [1,2,3,4]

seq = list(map(lambda x : x*2, sample))


def triple(value):
    return 3 * value  # Main calculation is done here


def triplestuff(a_list):
    new_list = map(triple, a_list)  # Accumulation done here
    # Func   # SEQUENCE
    return new_list


def quadruplestuff(a_list):
    new_list = map(lambda value: 4 * value,
                   a_list)  # Lambda is used to code in single line without defining the transformer function
    # Transformer   #Sequences
    return str(new_list)


things = ([1, 2, 3])

things3 = triplestuff(things)
print("Using MAP :", triplestuff(things))

things4 = quadruplestuff(things)
print("Using MAP :", things4)
################################################################################################
print("__________________________________________________________________________________________________")
#######################################################################################################

def square(n):
    return n * n


my_list = [2, 3, 4, 5, 6, 7, 8, 9]
updated_list = map(square, my_list)
print(updated_list)
print(list(updated_list))

################################################################################################
print("__________________________________________________________________________________________________")
#######################################################################################################


abb = ["Usa", "China", "India", "Canada", "Russia"]


def trans(st):
    return st.upper()


upp = map(trans, abb)
upp1 = map(lambda st: st.upper(), abb)
print("Using lambda method :", upp1)
print(str(upp))

#############################################################################################################
print("__________________________________________________________________________________________________")


##########################################################################################################

# Filter - To Filter the particular data from the list -  it passes the given iterable to the function and return the items which has true value
# filter(lambda expression ,sequence)

num = list(range(10))

seq = list(filter(lambda x : x%3 == 0, num))
print(seq)


def keep_evens(nums):   # the code without the filter option
    new_list = []
    for num in nums:
        if num%2==0:
            new_list.append(num)
    return new_list

print(keep_evens([1,2,3,4,5,6,7,8,9]))


def evens(nums):  # code with the filter option  - do same thing as above but with less code

    new1 = filter(lambda num: num % 2 == 0, nums)  # To filter the list
    return list(new1)


print(evens([1, 2, 3, 4, 6, 8, 9]))

###########################################################################################################
print("__________________________________________________________________________________________________")
################################################################################################

lst = ["Balaji", "Saman", "Kiran", "Santha", "Suan"]
lst2 = filter(lambda word: "i" in word, lst)

print(lst2)

#######################################################################################################
print("__________________________________________________________________________________________________")
#########################################################################################################
# List comprehension -  simpler syntax for Map and Filter - it provides the concise way to create the list
# it consist of brackets contain expression followed by for loop then zero or one or more if clause

# [output for i in list if condition ]

l = [j**3 for j in range(10) if j % 3 ==0]

#  [ output if condition else for i in list]

l = [ p if p % 2 == 0 else 0 for  p in range(10)]

# without list  comprehension

lst1 = []
def lst_square(lst):
    for i in lst:
        lst1.append(i*i)
    return lst1

print('without list comprehension',lst_square([1,2,3,4,5,6,7])


th = [2, 5, 9]

youlist = [value * 2 for value in th]
        # Transformer
        # Expression

print("using the List comprehension :", youlist)

#List all numbers divisible by 3 , 9 & 12 using nested "if" with List Comprehension
mylist4 = [i for i in range(200) if i % 3 == 0 if i % 9 == 0 if i % 12 == 0]
print(mylist4)

# Odd even test
l1 = [print("{} is Even Number".format(i)) if i%2==0 else print("{} is odd number".format(i))]
print(l1)



#################################################3##################################################
print("__________________________________________________________________________________________________")
####################################################33#############################################

# List Comprehension for list -

def even(nums):
    list = [num for num in nums if num % 2 == 0]
    return list


print("Using Comprehension :", even([1, 2, 65, 78, 45, 78, 52, 49, 62]))

#########################################################################################################
print("__________________________________________________________________________________________________")
###########################################################################################################

# Zip function - it is used for the addition of vectors as x and y values - x1,y1 and x2,y2 for two values

l1 = [3, 4, 5]
l2 = [4, 5, 6]
l3 = []
l4 = list(zip(l1, l2))

print("List function", l4)

for (x1, x2) in l4:
    l3.append(x1 + x2)

print("Using zip ", l3)

###############################################################################################################
print("__________________________________________________________________________________________________")
##############################################################################################################

from functools import reduce

# reduce -  as like map but
# it gives the output as single value

k = [1,2,3,4,5]

print(reduce(lambda x,y: x+y,k))
