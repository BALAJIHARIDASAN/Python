# Global and Local variables -   way of defining the attributes

def square(n):
    y1 = n * n  # Y - Is the local variable used within the function
    return y1


result = square(10)
print("Square of Number using Local Variable  :", result)

print("___________")

y = 5  # Global variable - Use Value outside Functions
print("global Variable :", y)

#######################################################################################################
print("___________________________________________________________________")
#############################################################################

# Composition of functions - using two function to get the result  - the function within the function

def sum_of_square(x1, y1, z):
    a = square(x1)
    b = square(y1)
    c = square(z)
    return a + b + c


result1 = sum_of_square(5, 6, 7)
print("Sum of numbers using functions", result1)

##################################################################################################
print("______________________________________________________________________________________")
###################################################################################################

# Tuple Packing

cars = ('Swift', '2014', 'Maruthi', 'India', 'Japan', 'Diesel', 'Turbo')

print("Index value is :", cars[4])


def year():
    return cars[1]


def model():
    return cars[0]


x = year()
print("Got the Year of Manufacture", x)
y = model()
print("Model is :", y)

##################################################################################
print("__________________________________________________________________________________________")
#####################################################################################################

print("END")
