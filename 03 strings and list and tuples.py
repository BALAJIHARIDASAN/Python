# Strings basic - Collection of Characters or Letter

s = "Hello World"  # Sequence of Characters or Letter
print(s)
print(len(s))  # Count the number of character in the variable 's'
m = '5'  # To enter the integers as string
print(m)
print(type(s))
print(type(m))
print("My name is Lenovo, i am a computer, Who helps the world to get better.")


###################################################
print("___________________________________________________________________________")
######################################################

# List - Square Brackets - Collection of ALL DATA TYPES or any type - it is mutable, or changeable, order of sequences
# Element inside the list is called items
# It is Mutable expression - change the values inside after the execution

#Lists are just like dynamic sized arrays, declared in other languages (vector in C++ and ArrayList in Java).
# Lists need not be homogeneous always which makes it a most powerful tool in Python.
# A single list may contain DataTypes like Integers, Strings, as well as Objects.
# Lists are mutable, and hence, they can be altered even after their creation.


mylist = ['Balaji', '25', 'Vellore', 'Tamilnadu', 'India']

print(mylist)
print(type(mylist))  # Type of the variables
print("Indexing in list :", mylist[3])  # To get the index values
print("Length of list :", len(mylist))  # To get the length of the list
print("Reverse the list " ,mylist.reverse())  # To reverse the list
print("sorted list is :",mylist.sort())  # To sort the list in ascending order
print('sorted list ', sorted(mylist)) # using sorted functions


#The sort() will modify an existing list but sorted() will  create a new list

mylist1 = [0] * 5
print(mylist1)

# Concatenate will done only in list
print([1,2,3]+[4,5,6])

#  To delete the elements
mylist.pop(1) # remove the element using index posititon
mylist.remove() # remove whole list  in element by element wise


# Sets - it is the unordered collection of data which is iterable, mutable and no duplicates of values

############################################################
print("__________________________________________________________________________")
###########################################################

# Tuples - Parenthesis - Like List, but its is immutables - It uses Round Brackets -()
# It increases efficiency - we cannot assign any values one we initialized it

mytuples = ('Sam', '25', 'Chennai', 'India')
Mytuples_with_single_value = (100,)
print(type(Mytuples_with_single_value))
print(mytuples)
print(type(mytuples))  # Type of the variable
print("Indexing in tuples :", mytuples[3])  # To get the index values of the tuples - the index value start with 0
print("Length of tuples :", len(mytuples))  # To get the length of the tuples
# Concatenate will done only another Tuples

################################################################
print("________________________________________________________________________________________")
##################################################################

# Indexing parameter - The indexing value always start with 0 - shortcut to find where the value is.

q = 'BALAJI'

print("Index value is : ", q[3])  # To get the index value of the string

print("Length of q :", len(q))  # To find the number of charter in the string

print("negative index is: ", q[-1])  # To get the value from the Reverse order TUPLES


################################################################
print("_____________________________________________________________________________________")
##################################################################

# Slicing operators - Getting the intermediate values in the List or Tuples

mylist1 = ['Balaji', '25', 'Vellore', 'Tamilnadu', 'India']
mylist3 = [['Balaji', ['25']], ['Hari']]
print("Sliced on multiple list", mylist3[0])
print("Sliced value is", mylist1[2:5])  # Slicing the List - myStr[start : stop : step]
print("Sliced value from mid to end :", mylist1[3:])  # Slicing start with 3 val to last val
print('Skipping the one value ',mylist[1::3])
print('Skipping the one value till last ',mylist[::3])
print('Skipping the one value from start ',mylist[1::])
print('Skipping the one value ',mylist[::-1])
print("Appending the list  ",mylist.append("South india")) # appending - add only one element to the list
print('extending the list ',mylist.extend([4, 5])) # extend - add multiple elements to the list


#####################################################################
print("__________________________________________________________________________________________")
#########################################################################

# Count - It counts the number of times the particular value is repeated
# Index - it gives the index position of list or tuples

a = 'I have the Laptop which was brought last week 24 and 46 and 54 and 74 '

print("The char repeated :", a.count("e" and "a"))  # The character that repeated in the given string
print("The int repeated :", a.count("4"))  # The integer repeated in the given character
print("The 'Brought is repeated for :", a.count("brought"))

mylist2 = ['Balaji', 25, 'Vellore', 'Tamilnadu', 'India']
print("List repeated is :", mylist2.count('India'))  # To count the values repeated in the list
print("Index value is:", a.index("have"))  # To get index value of the character in the list

################################################################################
print("_______________________________________________________________________________________________-")
################################################################################

import sys

print(sys.getsizeof(mytuples),'bytes')  # It gives the size of the object
print(sys.getsizeof(mylist),'bytes')

################################################################################
print("_______________________________________________________________________________________________-")
################################################################################

import timeit

print(timeit.timeit(stmt = '[0,1,2,3,4,5]',number = 1000000))  # It will gives the time to print the particular object
print(timeit.timeit(stmt = '(0,1,2,3,4,5)',number = 1000000))


################################################################################
print("_______________________________________________________________________________________________-")
################################################################################

# Split - It split the words into list along the white spaces

song = "The rain in Spain"

ind = song.split()  # Split the string into List 

print("Split value is :", ind)

# Join  - It joins the string into the List with whitespaces

h = ['Balaji', '25', 'Vellore', 'Tamilnadu', 'India']
glue = ' : '
print("Join list is:", glue.join(h))  # Joining the list to characters
print(" & ".join(h))  # Joining the list to characters


###########################################################################
print("______________________________________________________________________________________________")
##############################################################################


friends = ['Balaji', 'Susan', 'Raman', 'Kiran']

# FOR loop in the list - the iteration process

for i in friends:  # "i" is called loop variables/ "friends" iterative variables
    print("Welcome to party:", i)

friends[2] = 'Sundar'  # Replacing the string character in the list using the index method

print("After Replace :", friends)


###########################################################################
print("______________________________________________________________________________________________")
##############################################################################

# ACCUMULATOR PATTERN - it accumulate the value every time it process

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
accum = 0   # Accumulator variables
for w in nums:  # Iterative variables
    accum = accum + w  # Update accumulator
print("Accumulator value in the List", accum)
###########################################################################
print("______________________________________________________________________________________________")
##############################################################################

total1 = 0  # Initializing the value  for total
count1 = 0  # Initializing the value  for count
while True:
    inp = input('Enter a number: ')
    if inp == 'done': break
    value = float(inp)
    total1 = total1 + value
    count1 = count1 + 1

average1 = total1 / count1
print('Average:', average1)

##########################################################################
print("______________________________________________________________________________________________")
##############################################################################
# Refer TRY and EXPECT in the file 17

total2 = 0
count2 = 0
while True:
    inp = input('Enter a number: ')
    if inp == 'done' or inp == 'DONE':  # Loop will execute until we type done
        break
    try:
        value = float(inp)
    except:
        print('Invalid input')
        continue
    total2 = total2 + value
    count2 = count2 + 1

average2 = total2 / count2
print('Average using try/except :', average2)

##########################################################################
print("______________________________________________________________________________________________")
##############################################################################

inp = input('Enter Celsius Temperature: ')
cel = float(inp)
fahr = (cel * 9.0) / 5.0 + 32.0
print(fahr)

##########################################################################
print("______________________________________________________________________________________________")
##############################################################################
# LOOPING AND COUNTING

word = 'Banana'
count3 = 0
for letter in word:
    if letter == "a":
        count3 = count3 + 1
print("NO of 'a' in the letter :", count3)

######################################################
print("_______________________________________________________________________")
#######################################################

greet = "hello bob"
greet.upper()
print(greet)

greet1 = "HELLO WORLD"
greet1.lower()
print(greet1)

######################################################
print("_______________________________________________________________________")
#######################################################

line = 'balaji.hsrm@gmail.com sat 5:09:14 16 2002'
word1 = line.split()
print(word1)
print(word1[2])
Email_id = word1[0]
print(Email_id.split('@')[1])

######################################################
print("_______________________________________________________________________")
#######################################################

# set -Do not allow duplicates
#   Unordered collections of homogeneous elements
#  Sets are generally used to remove duplicate elements from a list

# union
# intersection
# difference
# symmetric difference
