# Nested data  module 3 first file

nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [2, 4, 5]]  # List within the list
print("After append : ", nested)
print("Index value is :", nested[0])
print("Length of the list is :", len(nested))

for i in nested:
    print(i)
nested.append([9, 9, 9])  # Append to the list
print("After using the for loop to append the list :", nested)

print(" By Multiple Indexing : ", nested[0][1])  # To get the value inside the list of the list

########################################################################################
print("____________________________________________________________________________________________")
###########################################################################################

# Nested dictionaries - Bracket count is important and the key and value pair is must

car = {'Specification':
           {"Engine": 'DDIS',
            "Model": 'Swift',
            "Make": 'Maruthi',
            'Physical features':
                {'Colour': {'Body': 'Red'},
                 'Bumper': 'black'
                 },
            'Year': '2014',
            'Cubic Capacity': '1200'
            }
       }

color = car['Specification']['Physical features']['Colour']['Body']
bumper_color = car['Specification']['Physical features']['Bumper']
print("Nested Data in Dictionary :", color)
print("Nested Data in Dictionary :", bumper_color)
year_manufacure1 = car['Specification']["Year"]
print("Manufactured year is :", year_manufacure1)

######################################################################################################################
print("______________________________________________________________________________________________________")
######################################################################################################################

# JSON - JAVA SCRIPT OBJECT NOTATION - TO READ AND WRITE THE JAVASCRIPT DATA - IT IS BASICALLY IN DICTIONARY

import json

a_string = '\n\n\n{\n"resultcount":25,\n"result":[\n{"wrappertype":"track","kind":"podcast","collectionid":10854}]}'
d = json.loads(a_string)  # Take string as input and return as dictionary
print(type(d))
print(d.keys())
print(d["resultcount"])

######################################################################################################################
print("______________________________________________________________________________________________________")


#####################################################################################################################
def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2)


d1 = {'Key1': {'c': 5, 'a': 90, '5': 50}, 'key2': {'b': 3, 'c': "yes"}}
print(d)
print(pretty(d1))

######################################################################################################################
print("______________________________________________________________________________________________________")
######################################################################################################################

# Nested Iteration - Using loop for multiple times  and continuous iteration - parse the list within the list

nested1 = [['a', 'b', 'c'], ['d', 'e', 'f']]
for i in nested1:
    print("level1 :", i)
    for u in i:
        print("level 2 :", u)

#########################################################################################################
print("____________________________________________________________________________________________________")
########################################################################################################

list = ['Balaji', 'Hari', '25', 'Vellore', 'Tamilnadu', 'India'], ['Sam', 'Kiran', '35', 'Chennai', 'Tamilnadu',
                                                                   'India'], ['Susan', 'Tam', '25', 'Salem',
                                                                              'Tamilnadu', 'India']

lastname = []  # To extract the inner list and extract the particular values from the list
for s in list:
    lastname.append(s[1])  # To parse the last-name from the list
print(lastname)

print("Indexing in the list :", list[1][0])

b_string = []  # Looking for particular value in the list
for t in list:
    for word in t:  # IN - operator used for comparison
        if 'a' in word:
            b_string.append(word)
print("using the in operator :", b_string)

###########################################################################################################
print("______________________________________________________________________________________________________")
############################################################################################################3

nested3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("level: {}".format(nested3))

#########################################################################################################
print("____________________________________________________________________________________________________")
##########################################################################################################

# Deep and Shallow copy- to copy the list values


org = [['Balaji', 'Raj', 'Tam'], ['Kiran', 'Santosh', 'Jamal']]
print("Original list is :", org)
copy = org[:]  # To extract all element from the org
print("Copied list is :", copy)
print("Checking the object :", org == copy)
org[0].append('Tina')
print("After Append Original list is :", org)
print("After Append copy list is :", copy)

copy_out_list = []
for e in org:
    copy_inn_list = []
    for item in e:
        copy_inn_list.append(item)
    copy_out_list.append(copy_inn_list)
print("__________")
print("Using the FOR loop copying as Deep copy :", copy_out_list)

##############################################################################################################

print("END")

