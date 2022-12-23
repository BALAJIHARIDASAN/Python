# Boolean expressions -  logical operators  - it is used to represent the truth value

# Comparison operator -  compare the values

print("Checking for Equal :", 5 == 5)  # Checking the condition/ comparison operators
print("Checking for NOT Equal :", 5 != 6)  # Not equal
print("Checking for Greater than :", 5 >= 80)  # Greater than or equal to
print("Checking for Lesser than :", 10 <= 5)  # Less than or equal to

#################################################################
print("__________________________________________________________________")
#################################################################

# Logical operators - AND / OR / NOT  - Tree Table

x = 45
if x >= 5 and x >= 10:  # Two conditions must satisfy
    print("Good ")
else:
    print("Sorry")
#################################################################
print("__________________________________________________________________")
#################################################################

y = 75
if y >= 50 or y <= 100:  # Any-one condition must satisfy
    print("The value is correct")

###########################################################################
print("__________________________________________________________________")
#######################################################################

# IN AND NOT IN operators -

print('p' in 'Apple')
print('o' not in 'Apple')
print("s" in 'Swift')
print("Balaji" in ['Balaji', 'Sandeep', 'Santhosh', 'Sundar', 'John'])
print("Bala" not in ['Balaji', 'Sandeep', 'Santhosh', 'Sundar', 'John'])

###########################################################################
print("__________________________________________________________________")
#######################################################################

# Conditional Execution - if-else statement

d = 15
if d % 5 == 0:  # If with  boolean expression
    print("Divisible")  # It will execute only if above statement is True
else:  # Otherwise
    print("Not divisible")

##################################################################
print("__________________________________________________________________")
####################################################################

# Comparison Execution  -  It compares the values for the execution
x = 12

if x < 10:
    print("Smaller")
    print("First step")
if x > 10:
    print("Greater")

print("Finish")  # This will execute even if not met the conditions

##################################################################
print("__________________________________________________________________")
####################################################################
y = 10

if y > 2:
    print("Bigger")
else:
    print("Smaller")

##################################################################
print("__________________________________________________________________")
####################################################################

s = 86  # Nested Conditions - ELIF Statement
if s >= 85:
    print("Distinction")
elif s >= 60:  # ELIF condition - Check the condition line-by-line
    print('First Class')
elif s >= 50:  # This loop will not execute if the above statement is - True
    print("Second Class")
elif s >= 35:
    print("Third Class")
else:
    print("Arrears")

###################################################################
print("__________________________________________________________________")
####################################################################

# Accumulator pattern with conditions - For Loop

pharse = " What a wonderful day"

total = 0
for char in pharse:
    if char == "a":
        total = total + 1
print("Total NO of 'a' in the pharse:", total)

#############################################################################
print("__________________________________________________________________")
##############################################################################
# Largest number in the list

nums = [15, 45, 68, 28, 986, 584, 587, 326, 958, 124, 658, 254, 215, 521, 556, 662, 3214, 3662, 5214, 23321, 2254,
        5684]

largest_number = nums[0]
for n in nums:
    if n > largest_number:
        largest_number = n
print("Largest number is :", largest_number)

#############################################################################
print("__________________________________________________________________")
##############################################################################
# Mutability   - In the List


mylist = ['Balaji', '25', 'Vellore', 'Tamilnadu', 'India']

print("Before Replacing:", mylist)

mylist[0] = "Sam"  # Giving the indexing values

print("After Replacing :", mylist)

del mylist[3]  # Deleting the list value with index values
print("After Deleting Tamilnadu :", mylist)

#####################################################################################


# bitwise operator - Python Bitwise Operators take one to two operands, and operates on it/them bit by  bit, instead of whole

number = 9

print((number % 3 == 0 ) & (number % 5 == 0)) # bitwise and operator

print((number % 3 == 0 ) | (number % 5 == 0)) # bitwise or opeator

