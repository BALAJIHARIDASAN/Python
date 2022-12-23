# While loop - Combination of IF and FOR statement - To print same statement multiple times

x = 1  # Initial statement
while x <= 5:  # Giving the conditions - only execute if the statement is true
    print("WELCOME To 'WHILE' LOOP")  # Block of the statement
    x = x + 1  # Incrementing the value - It is must to run the loop

##################################################################################
print("___________________________________________________________________________________")
######################################################################################

# Using WHILE loop in functions

def repeating():
    x1 = 1  # local variable
    while x1 <= 10:
        print("Congrats Welcome to Party")
        x1 = x1 + 2


repeating()

######################################################################################################
print("__________________________________________________________________________________")
############################################################################################

# BREAK and CONTINUE statement -

# BREAK - EXECUTABLE STATEMENT -The ‘break’ statement ends the current loop and resumes
# execution at the next statement.


n = 5
while n > 0:
    n -=1
    if n ==2:
        break
    print(n)
print('loop ended')

l =[1,2,3,4,5,6]

for i in l:
    if i == 3:
        break
    print(i)


# CONTINUE - The ‘continue’ statement in Python ignores all the
# remaining statements in the iteration of the current
# loop and moves the control back to the beginning of
# the loop.

n = 5

while n > 0:
    n -=1
    if n ==3:
        continue
    print(n)


#######################################################################
print("__________________________________________________________________")
###########################################################################

# Definite and indefinite loop

a = 6  # Initial statement

while a < 10:
    print("We are Calculating")
    if a % 2 == 0:
        a += 3
        continue
    if a % 3 == 0:
        a += 5
    a += 1
print("Done with Loop", str(a))

#########################################################################################################3
print("________________________________________________________________________________")
############################################################################################################
# keyword Parameter

initial = 7


def f(x1, y1, z=initial):
    print("x,y,z  are :", x1, y1, z)


f(3, 2)  # Only to invoke the function

######################################################################################################
print("________________________________________________________________________________")
####################################################################################################

numlist = list()
while True:
    inp = input('Enter a number: ')
    if inp == 'done':
        break
    value = float(inp)
    numlist.append(value)

average = sum(numlist) / len(numlist)
print('Average:', average)

########################################################################################
print("________________________________________________________________________________")


###############################################################################################


# Lambda Expressions - Simplest way of defining the function

def cal(k, b, c, d):  # Traditional way of defining the function without lambda
    return k * b / c + d


print(cal(1, 2, 3, 4))

calc = lambda c, d: c + d   # Easiest way of defining the function with lambda

print("Value using the Lambda :", calc(10, 11))

multi = lambda e, f1, g: e * f1 * g
print("Own function using Lambda :", multi(5, 6, 7))

########################################################################################
print("________________________________________________________________________________")
###############################################################################################

# Sort function

company = ["Maruthi", "Nissan", "Ford", "Renault", "Audi", "Porsche", "Hyundai"]
sales = ['23', '45', '85', '78', '54', '35', '26']

company.sort()  # Sorted by alphabetical order
print("Sorted company list :", company)

sales.sort()  # Sorted by ascending order of numbers
print("Sorted sales list :", sales)

#####################################################################################################3
print("________________________________________________________________________________________")
###################################################################################################3

# Reversed sort

company = ["Maruthi", "Nissan", "Ford", "Renault", "Audi", "Porsche", "Hyundai"]

print("reversed sort", sorted(company, reverse=True))  # Reversing the sort of the list

#################################################################################################3
print("________________________________________________________________________________________")
#################################################################################################

# Optional key parameter

sales = [23, 45, -85, 78, -54, 35, 26]


def absolute(j):
    if j >= 0:
        return j
    else:
        return -j


print(absolute(3))
print(absolute(-15))

for y in sales:
    print(absolute(y))

###########################################################################
print("______________________________________________________________________________________________")
##############################################################################
# While statement with accumulator pattern
total = 0
count = 0
while True:
    inp = input('Enter a number: ')
    if inp == 'done': break
    value = float(inp)
    total = total + value
    count = count + 1

average = total / count
print('Average:', average)

##########################################################################
print("______________________________________________________________________________________________")
##############################################################################
# while statement for accumulator pattern with conditional execution

total = 0
count = 0
while True:
    inp = input('Enter a number: ')
    if inp == 'done':
        break
    try:
        value = float(inp)
    except:
        print('Invalid input')
        continue
    total = total + value
    count = count + 1

average = total / count
print('Average:', average)

##########################################################################
print("______________________________________________________________________________________________")
##############################################################################

while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')

##########################################################################
print("______________________________________________________________________________________________")
##############################################################################
inp = input('Enter Hours: ')
hours = float(inp)
inp = input('Enter Rate: ')
rate = float(inp)
if hours > 40:
    pay = hours * rate + (hours - 40) * rate * 0.5
else:
    pay = hours * rate
print('Pay:', pay)

##########################################################################
print("______________________________________________________________________________________________")
##############################################################################

try:
    inp = input('Enter Hours: ')
    hours = float(inp)
    inp = input('Enter Rate: ')
    rate = float(inp)
    if hours > 40:
        pay = hours * rate + (hours - 40) * rate * 1.5
    else:
        pay = hours * rate
    print('Pay:', pay)
except:
    print('Error, please enter numeric input')

##########################################################################
print("______________________________________________________________________________________________")
##############################################################################

inp = input('Enter a Number:')
n = int(inp)
while n != 1:
    print(n, end=' ')  # Use comma to suppress newline  - it stops print the values in the next line
    if n % 2 == 0:  # n is even
        n = n / 2
    else:  # n is odd
        n = n * 3 + 1

##########################################################################
print("______________________________________________________________________________________________")
##############################################################################

print("END")
