# Methods on List and String

mylist = [5, 27, 3, 12]  # Creating the empty list
print("Initial List is :", mylist)


####################################################################################################################
print("__________________________________________________________________")
########################################################################################


# Methods on string

my_string = ' Hello World '

print(my_string.strip())  # Strip the string with whitespaces to the list

print(my_string.upper())  # UPPERCASE - convert to uppercase

print(my_string.lower())  # LOWERCASE  - convert to lowercase

print(my_string.startswith('Hello'))  # print 'true' if the line start with the specified character

print(my_string.endswith('World')) # print 'true' if the line end with the specified character

print(my_string.find('o'))  # find the particular character in the string

print(my_string.count('o'))  # count number of times the particular character is repeatex

print(my_string.replace('World','Universe'))  # replace new value with old value

####################################################################################################################
print("__________________________________________________________________")
########################################################################################

greet = "  Hello World  "

print(greet.lstrip())  # Remove the whitespace in left

print(greet.rstrip())  # Remove the whitespace in right

print(greet.strip())  # Remove the both beginning and ending whitespaces

####################################################################################################################
print("__________________________________________________________________")
########################################################################################


str2 = " WELCOME EVERYONE "
str2 = str2.rjust(50) # Right align the string using a specific character as the
print(str2)


str2 = " WELCOME EVERYONE "
str2 = str2.center(100) # center align the string using a specific character as t
print(str2)

####################################################################################################################
print("__________________________________________________________________")
########################################################################################

mystr6 = '123456789'
print(mystr6.isalpha()) # returns True if all the characters in the text are lett
print(mystr6.isalnum()) # returns True if a string contains only letters or numb
print(mystr6.isdecimal()) # returns True if all the characters are decimals (0-9)
print(mystr6.isnumeric()) # returns True if all the characters are numeric (0-9)

####################################################################################################################
print("__________________________________________________________________")
########################################################################################

mystr6 = 'abcde'
print(mystr6.isalpha()) # returns True if all the characters in the text are lett
print(mystr6.isalnum()) # returns True if a string contains only letters or numb
print(mystr6.isdecimal()) # returns True if all the characters are decimals (0-9)
print(mystr6.isnumeric()) # returns True if all the characters are numeric (0-9)

####################################################################################################################
print("__________________________________________________________________")
########################################################################################

mystr7 = 'ABCDEF'
print(mystr7.isupper()) # Returns True if all the characters are in upper case
print(mystr7.islower()) # Returns True if all the characters are in lower case

####################################################################################################################
print("__________________________________________________________________")
########################################################################################

# Non-Mutating methods on Strings

ss = 'HELLO WORLD'
print(ss.lower())  # Print the LOWER case of the String

tt = ss.upper()
print(tt)  # Print the UPPER case of the String

print("Strip the String", tt.strip())  # Strip the white-space in the List

uu = ss.replace("ORL", "***")  # Replace the string

print("Using REPLACE method", uu)
###########################################################################
print("__________________________________________________________________")
###########################################################################

# Adding values using - FOR loop

mylist1 = []  # Empty list
for i in range(0, 25, 5):  # Using RANGE function
    mylist1.append(i)   # Using the append method
print("Using FOR loop :", mylist1)

##########################################################################
print("__________________________________________________________________")
##########################################################################

# methods on list

mylist.insert(1, 12)  # Inserting the value with position
print('After Insert :', mylist)

print("Count is :", mylist.count(12))  # Count the list

print("Index value is:", mylist.index(3))  # Get the Index values

print("Count is :", mylist.count(5))

mylist.reverse()  # Making the Reverse order of the list
print("After reverse is :", mylist)

mylist.sort()  # Sorting the list on Ascending order
print("After Sort is :", mylist)

lastitem = mylist.pop()  # PRINT THE LAST ITEM IN THE LIST

print("After POP is :", lastitem)  # PRINT THE LAST ITEM IN THE LIST
print("Final List is :", mylist)

mylist.clear() # Empty List / Delete all items in the list
mylist
######################################################################
print("__________________________________________________________________")
###########################################################################


scores = [('Balaji', 20), ('Susan', 30)]
for person in scores:
    name = person[0]
    scores = person[1]
    print("Hello {}. Your Score Is {}".format(name, scores))

# "{}" - Substitution for the Values using ".format method"

###########################################################################
print("__________________________________________________________________")
###########################################################################
item1 = 45
item2 = 75
item3 = 85
profit = 350

revenue = "cost of item1,item2,item3 are {2},{0}and{1} with profit of {3}"  # using the index values in different places
print(revenue.format(item1,item2,item3,profit))

###########################################################################
print("__________________________________________________________________")
###########################################################################

price = float(100)
discount = float(25)
new_price = (1 - discount / 100) * price

result = '${:.2f} Discounted By {}% Is ${:.2f}.'.format(price, discount, new_price)
print(result)

# "${:.2f}" Print the no of value after two Decimal points

###########################################################################
print("__________________________________________________________________")
###########################################################################

# Append Method for List - ADDING THE VALUES TO THE LIST

orglist = [14, 25, 35, 26, 25]

print("After Append is :", orglist)

##########################################################################
print("__________________________________________________________________")
############################################################################

# Accumulator pattern in List - For loop

num = [3, 5, 6, 8]
count = []
count1 = 0
for w in num:
    x = w ** 2
    count.append(x)
    print("Count :", x)
for w1 in count:
    count1 = count1 + w1
print("Acc Value are :{} AND Total is {}".format(count, count1))


#######################################################################
print("__________________________________________________________________")
##########################################################################

# Accumulator in string -

s = input("Enter the Text : ")

acc = " "
for c in s:
    acc = acc + c + "" + c + ""
    print(acc)

print("Acc in string :", acc)

#######################################################################
print("__________________________________________________________________")
##########################################################################

# Parsing and Extracting

data = "From Balaji.hsrm@uct.ac.za Sat Jan 5 09:14:16 2020"

atop = data.find("@")   # Search the sign in the data

print(atop)   # Print the index position of the sign

ssop = data.find(' ', atop)
print(ssop)

host = data[atop + 1: ssop]  # Slicing the data
print(host)

#######################################################################
print("__________________________________________________________________")
##########################################################################


print("""
    
        END""")
