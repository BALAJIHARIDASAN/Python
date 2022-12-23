# Functions - a function is a piece of code written to carry out a specified task
# Arguments - value we pass into the functions as its input when we call the functions

# types - built-in, user defined, anonymous


# Required Arguments - if the function does not requires the argument and is passed it will throw an error

#Keyword Arguments- The arguments have names assigned to them

def employee(name, destination):
    print(name, destination)

employee(name = 'balaji',destination= 'officer')

# default arguments

def employee(destination,name = 'balaji'):  # default arguments should follow the non defaulted argument
    print(name, destination)

employee('officers')



def hello():  # Giving the name for function
    # Parameter space
    print("Welcome to 'FUNCTIONS' in Python ")  # Blocks for functions
    # it only print the statement it will not able to assign to the variables

hello()  # Invoking the functions

var = hello()  # it will give the value  output 'NONE' because we are not returning any value in the variable

def hello_1():
    return 'hello world'

var1 = hello_1() # the fucntion is assinged to the variable only when u use the return statement

print(var1)

# positional and keyword argument

def info(name,age = 25):

#  'name'  is the positional argument where we dont assign any value
#   age - is the keyword argument where we assigned the values

    print('my name is {} and my age is {}'.format(name,age) )

print(info('balaji'))



def info_1(*args,**kwargs):
    print(args)
    print(kwargs)

print(info_1('balaji','hari',age = 29,dob = 1994))

# *args - positional argument - use any number of values without the error
# ** kwargs - keyword arguments - use any number key value pairs without error

l = ['balaji','hari','vellore']
d = {'age':29,'year':35}

def info_2(*args,**kwargs):  #  it help to add the list and dict in the functions

    print(args)
    print(kwargs)

print(info_2(*l,**d))



####################################################################################
print("_____________________________________________________________________________________")
####################################################################################

def car(c, s):  # Defining the functions
    print("Congrats for Buying" + " " + c + " " + s)  # Function blocks
    print("Safe Driving" + " " + c)


car('Swift', 'Hatchback')  # Invoking the functions
print("_____")
car('I10', 'Salon')

###########################################################################################
print("____________________________________________________________________________________________")
###########################################################################################
# Default argument - giving the default values while assigning the attributes

def students(name ='balaji',age =45):
    print(name)
    print(age)

students()

def student1(name,age,*mark):   # *args - means the values are in tuples
    print(name)
    print(age)
    print(mark)
    for i in mark:
        print((i))

student1('balaji', 22,95,84,85,75)

def student(name,age,**mark):   # **kwargs- means the values in dictionary
    print(name)
    print(age)
    print(mark)
    for key,value in mark.items():
        print(key)
        print(value)
student('balaji', 22, english=95, math=84)

###########################################################################################
print("____________________________________________________________________________________________")
############################################################################################

# Return value in the Function

def square(n, w):
    square1 = n * n, w * w
    return square1  # It only return the value it won't "print" unless WE call it


result = square(10, 5)  # Invoking the function
print("Square of Number is :", result)  # Getting the result from invoking the Function


# Adding Two Values

def addition(x, y1):
    return x + y1


Number = 4, 2
add = addition(4, 2)
print("Using function to add Two Number {} is {} ".format(Number, add))

#############################################################################################3333333
print("_______________________________________________________________________________________________")
#########################################################################################################33

# A Function with accumulation

def total(lst):
    tot = 0
    for num in lst:
        tot = tot + num
    return tot


y = total([1, 2, 3, 4, 5])

print("Total using Accumulation :", y)

################################################################################################################
print("__________________________________________________________________________________________________")
################################################################################################################

# Inbuilt functions
word = 'hello'
big = max(word)  # Getting the max of the alphabet in order
print(big)
print(min(word))  # Getting the min of the alphabet in order
print(type(word))  # Getting the type of the variable
##################################################################
print("__________________________________________________________________")
####################################################################

def greet(lang):  # function with conditional statements
    if lang == 'Es':
        return 'Hola'  # Return value
    elif lang == 'Eng':
        return 'Hello'    # Return value
    elif lang == 'Fr':
        return 'Bonjour'  # Return value
    else:
        return 'Vanakam'  # otherwise


print(greet('Fr'), 'Micheal')
print(greet('Er'), 'Susan')
print(greet("kr"), 'Balaji')

##################################################################
print("__________________________________________________________________")
####################################################################

# lambda function - it is anonymous function - function with no name - it is assigned to the variable

# lambda arguments : expression

subtraction = lambda  x,y : x-y
print(subtraction(100,20))

##################################################################
print("__________________________________________________________________")
####################################################################

