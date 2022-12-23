# PYTHON PROGRAMMING -
# CODE - THE LANGUAGE OF THE COMPUTER


# data types - string , float, int, boolean
# collections - list, tuple, dictionary
import sys

print("Welcome to 'PYTHON' Programming")  # Print statement - Printing the expression and value within the parenthesis is called parameter or argument

print("Hello World")  # String - sequence of characters
print('Start Typing')  # Strings
print("She said 'WELCOME HOME'")  # Quotation in-side the strings
print("100")  # Integer
print("3.147")  # Float
print("Ram'S coffee")  # Quotation in-side the Quotation.
print('He said "Hai"')

#############################################
print("____________________________________________________________________")
#############################################

# Expressions - "100" are the building block of programming - It contains values'

# Variables - It is the reserved memory location to store the values.

# Operator and Operands

# Operator Precedence  - Parenthesis, Power, Multiplication, Addition, Left to right  - BOODMAS RULE

# Variable assignment - the values are assigned to the variables

x1,x2,x3 = 10,20,30  # Multiple assignments

print(x1)
print(x2)
print(x3)


x = 10       # Assignment statement
y = 20       # Assignment statement
print(x+y)   # Add
print(x-y)   # Sub
print(x*y)   # Multiply
print(x/y)   # Float div
print(x//y)  # Div
print(x % y)  # Mod
print(4**2)  # Power of the Number

###########################################
print("_____________________________________________________________________")
###########################################

# Functions - Machinery of the programming
# Arguments - Also called as input
# Return value - Also called as output
# Data types - The type of the values type - keyword

print(type(x))  # Integer
print(type('Hello World'))  # String
print(type(3.14))  # Float
print('hello'+'world')  # Concatenation
print('''"OH no",she exclaimed,Ben's bike is broken!"''')

#######################################
print("_____________________________________________________________________________")
##########################################

# Type conversion

print(float(3))  # Int to Float
print(int(3.14))  # Float to Integer

#######################################
print("_____________________________________________________________________________")
##########################################

# Variables - Stores the values of the expressions - 'HAS' a name and value

message = 'Learning the PYTHON PROGRAMMING'  # Set variable
print(message)  # Reference variable
pi = 3.14
print(pi)
greeting = "Hello World"
print("The variable value is:", greeting)

# Where "pi", greeting are called Set variables
# Where "print(greeting, pi)" are the Reference variables

#################################################
print("________________________________________________________________")
###################################################

var1, var2, var3 = 10, 20, 30  # Multiple assignment

print(var1)
print(var2)
print(var3)

print(sys.getsizeof(var1))  # size of the integer object in bytes

#################################################
print("______________________________________________________________")
###################################################
# Updating the Variables

x = 10  # Initialization  of Variables
print("The value of x is :", x)
x = x+15
print("Updated value is :", x)
x += 145   # Incremental Statement
print("Next updated value is :", x)
x -= 15  # Decremental Statement
print("Decremental Value", x)

###################################################
print("______________________________________________________________________")
#####################################################

# Input function - Ask the user to input the values or strings

y = input("Enter the value")
print("Number is", y)

######################################################
print("_______________________________________________________________________")
#######################################################

hours = 45
rate = 30
pay = hours * rate  # Assignment statement with expressions
print("Total pay is :", pay)

######################################################################

usf = input('Enter the US Floor Number: ')
wf = int(usf) - 1
print('Non - US Floor Number is', wf)

######################################################
print("_______________________________________________________________________")
#######################################################

inp = input('Enter Fahrenheit Temperature: ')
fahrenheit = float(inp)
cel = (fahrenheit - 32.0) * 5.0 / 9.0
print(cel)

######################################################
print("_______________________________________________________________________")
#######################################################

big = max("Hello world")  # print the variables that has the max value in the string alphabet
print(big)
small = min("Hello")  # print the variables that has the small value in the sting alphabet
print(small)


######################################################
print("_______________________________________________________________________")
#######################################################

# Syntax Error - Interpreter can't parse the code - Error in the code  - GRAMMAR FOR LANGUAGE

# Runtime Error - The error occurs during the running the program

# Semantic Error - The error occur due improper coding of the data - Run and Decode properly- Programmer Error
