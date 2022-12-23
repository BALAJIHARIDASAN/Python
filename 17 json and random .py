import json  # java script object notation - like dictonary

person = {"name": 'John',
          "age": 25,
          "city": "new york",
          "has_children": False,
          "titles": ["engineer", "programmer"]
          }

personJSON = json.dumps(person, indent=4, sort_keys=True)  # convert the object into json format  - lower case values
print(personJSON)

##############################################################################################################3
print("_______________________________________________________________________________")
################################################################################################################

with open('person.json', 'w') as file:  # to create a file as json format
    json.dump(person,file,indent=4)

person = json.loads(personJSON)  # json to object - load from the string
print(person)

##############################################################################################################3
print("_______________________________________________________________________________")
################################################################################################################

class User:
    def __init__(self,name,age):
        self.name = name
        self.age = age

def  encode_user(o):
    if isinstance(o,User):
        return {'name':o.name,'age':o.age,o.__class__.__name__:True}
    else:
        raise TypeError

user = User('max',27)
userJSON = json.dumps(user,default=encode_user)
print("As JSON FORMAT :" ,userJSON)

##############################################################################################################3
print("_______________________________________________________________________________")
################################################################################################################

# Random numbers generator

import random

a = random.random()  # it generate the random number
print(a)

b = random.uniform(1, 10)  # it generate the uniform numbers
print(b)

c = random.randint(1, 10)  # it generate the random integer number
print(c)

d = random.randrange(1, 10)  # it generate the number of integer but the upperbound is not included
print(d)

e = random.normalvariate(0, 1)  # it generate the normal distribution values
print(e)

l = list("ABCDEFGH")
f = random.choice(l)  # it will select the random value or char from the list to print
print(f)

g = random.sample(l, 2)  # it will select the sample from the list to print
print(g)

h = random.choices(l, k=3)  # it will select the random values of different choices
print(h)

j = random.shuffle(l)  # it will shuffle the list
print(j)
