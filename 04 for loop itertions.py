# For Loop - Multiple Iterations and Repeating the Values - iterate through the sequence


#The difference between for loop and while loop is that in for loop the number of iterations to be done is already known
# and is used to obtain a certain result
# whereas in while loop the command runs until a certain condition is reached and the statement is proved to be false.


for i in ['Balaji', 'Sandeep', 'Santhosh', 'Sundar', 'John']:
    print("hello", i)
    #  i - loop variable
    #  The list values is the sequences

###################################################################
print("____________________________________________________________________")

########################################################################

x = str(input("enter the str :"))
for g in x:  # It will split the entered string and execute line by line
    print(g)

##################################################################################
print("_____________________________________________________________________________")
##############################################################################

# Accumulator pattern

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
count = 0  # Initializing the value
for w in nums:
    count = count + w
print("Sum is :", count)  # This will count the values in List


########################################################
print("____________________________________________________________________________________")
###################################################################################

# Range function - IT TAKES THE INPUT AS THE RANGE SEQUENCE

count1 = 0
for g in range(0, 100, 25):
    count1 = count1 + g
    print("The value using range function is :", count1)

print(list(range(1, 20)))


######################################################################################
print("______________________________________________________________________________________")
#####################################################################################

count = 0
num = 0
print("Before", num)
for thing in [9, 42, 12, 3, 74, 15]:
    num = num + thing
    count += 1
    print(count, num, thing)
avg = num / count
print(count, "After", 'Total is :', num, 'Average  is:', avg)

#######################################################################
print("__________________________________________________________________")
###########################################################################


friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print('Happy New Year:', friend)
print('Done!')

#######################################################################
print("__________________________________________________________________")
###########################################################################

# FOR loop - for strings

txt = 'But soft what light in yonder window breaks'
words = txt.split()   # it split the string into list
t = list()
for word in words:
    t.append((len(word), word))  # It add the values  to the list
    print(word)

t.sort(reverse=True)  # It sort the list in the ascending order

res = list()
for length, word in t:
    res.append(word)

print(res)

#######################################################################
print("__________________________________________________________________")
###########################################################################

for value in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    if value == 3:
        print("Available in the list")
    else:
        print("Not available in the list")

#######################################################################
print("__________________________________________________________________")
###########################################################################
