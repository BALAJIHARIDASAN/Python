# Dictionary - Curly brackets - it is the data types which is unordered mutable and indexed contains key value pairs
# It has Keys and Values pairs
        # Key    #Value
car = {'Engine': 'DDIS', 'Model': 'Swift', 'Make': 'Maruthi', 'Year': '2012',
       'Cubic Capacity': '1200'}  # Creating the name for dictionary

print(car)

value = car['Engine']

print("Value for engine is  :", value)

print("Value for model is :", car['Model'])

###################################################################################
print("______________________________________________________________________________")
################################################################################

# Dictionary operators

# Deletion

car1 = {'Engine': 'DDIS', 'Model': 'Swift', 'Make': 'Maruthi', 'Year': '2014', 'Cubic Capacity': '1200'}
        # key     #value

del car1['Year']  # This will delete the whole Key-Value pair
print(car1)

###################################################################################################333
print("________________________________________________________________________________________________")
#########################################################################################33

# Len -TO get the no of key-value pairs in the dictionary

car2 = {'Engine': 'DDIS', 'Model': 'Swift', 'Make': 'Maruthi', 'Year': '2012', 'Cubic Capacity': '1200'}
# key        #value

numitems = len(car2)  # To get the no of key value pair in the dictionary
print("Length is :", numitems)

############################################
print("________________________________________________________________________________________")
#######################################################

# Dictionary methods

car3 = {'Engine': 'DDIS', 'Model': 'Swift', 'Make': 'Maruthi', 'Year': '2012', 'Cubic Capacity': '1200'}
# key        #value

for key in car3.keys():  # To get the key
    print("Keys Is :", key)

keys = list(car3.keys())  # To get the keys in form of list
print("Keys in form of list :", keys)

for value in car3.values():  # To get the values
    print("Values Is :", value)

valuss = list(car3.values())  # To get the values in form of list
print("Values in form of list :", valuss)

for item in car3.items():  # To get the whole item in the dictionary
    print("Key - Value pair is : ", item)

#############################################################################################################
print("___________________________________________________________________________________________")
############################################################################################3

# Get method - It gives the output as 'none' if not available, it useful to avoid the runtime error

car4 = {'Engine': 'DDIS', 'Model': 'Swift', 'Make': 'Maruthi', 'Year': '2012', 'Cubic Capacity': '1200'}
        # key     #value

print("Values using the get method :", car4.get("Engine"))
print("Values using the get method :",
      car4.get("engine"))  # The key is not present in the dictionary, so it print "NONE"

################################################################################################33
print("____________________________________________________________________________________________________")
############################################################################################33333

# Dictionary Accumulation

file = open("dict.txt", 'r')
txt = file.read()
count = 0
for counts in txt:
    if counts == 'a':
        count = count + 1
print("Occurrences of 'A' in the file:", count)

######################################################
print("_______________________________________________________________________")
##################################################################################################

sentence = " The dog chased the rabbit into the forest but the rabbit got escaped"

words = sentence.split()
words_count = {}

for word in words:
    if word not in words_count:
        words_count[word] = 0
    words_count[word] = words_count[word] + 1

print(words_count)


######################################################
print("_______________________________________________________________________")
#######################################################

travel ={"North America": 2, "Europe": 8, "Asia": 16, "Africa": 20}
total = 0
for continent in travel.values():
    total = total + continent
print(total)

######################################################
print("_______________________________________________________________________")
#######################################################
print('END')
