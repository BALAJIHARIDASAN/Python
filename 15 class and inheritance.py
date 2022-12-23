# Classes and Methods - Defining our own method in the python - real case object

# Class - Factory
# Instances - Factory producers
# Instance variable -The variable lives inside the instances
# Method - Like function but it belongs to the class


# Python class to represent points in the graph
from symbol import test


class Point:  # Keyword and class name
    def __init__(self):
        self.x = None

    def getX(self):  # Methods of the class/ self - default Argument
        return self.x


point1 = Point()  # Instances
point2 = Point()

point1.x = 5  # Instance Variable - The variable in the inside the instances
point2.x = 10

print(point1.getX())
print(point2.x)

################################################################################################################
print(
    "__________________________________________________________________________________________________________________")


###############################################################################################################3

# Constructor - Is a special Method  that meant to initialize instance Variable
# Dunderscore - __init__


class Point1:  # Name should always starts with capital letter

    def __init__(self, x, y):  # Method
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y


point3 = Point1(10, 100)
point4 = Point1(50, 10)

print(point3.getX())
print(point4.getX())


#######################################################################################################################


# Its is basically like using the Import

class Cars:
    def car(self, x):
        return x, "Diesel"


car1 = Cars()

type1 = car1.car('Engine')

print("Output ", type1)

#####################################################################################################################
print(
    "________________________________________________________________________________________________________________")


#####################################################################################################################

# Adding other method to the class

class Point1:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y


point4 = Point1(10, 25)

print(point4.getX())
print(point4.getY())

######################################################################################################################
print("_______________________________________________________________________________________________________________")


#####################################################################################################################

class Math_square_and_triple:
    def __init__(self, x, y):
        self.x = x * x
        self.y = y * y * y

    def square(self):
        return self.x

    def triple(self):
        return self.y


tri = Math_square_and_triple(5, 5)

print(tri.square())
print(tri.triple())
#######################################################################################################################3
print("_______________________________________________________________________________________________________________")

###########################################################################################################################

city = ['Vellore', 'Bangalore', 'Chennai', 'Mumbai', 'Delhi']
population = ['6599445', '66987222', '4589963', '23467512', '25699545']
states = ['TN', 'KA', 'TN', 'MU', 'ND']

city_tuples = zip(city, population, states)

print("Using zip method :", city_tuples)


class City:
    def __init__(self, n, p, s):
        self.name = n
        self.population = p
        self.state = s

    def __str__(self):  # Print the class
        return '{} , {}, (pop:{}) '.format(self.name, self.population, self.state)


cities = []
for city_tup in city_tuples:
    name, pop, state = city_tup
    city = City(name, pop, state)  # Instance of the City class
    cities.append(city)
    print(name, pop, state)
print("Using the normal method:", cities)

cities1 = [City(n, p, s) for (n, p, s) in city_tuples]
print("Using the list comprehension :", cities)

###################################################################################################################
print("________________________________________________________________________________________")


##################################################################################################

class Point2:
    def __init__(self, initX, initY):  # Constructor
        self.X = initX
        self.Y = initY

    def getX(self):  # Method
        return self.X

    def getY(self):  # Method
        return self.Y

    def distance_from_origin(self):  # Method
        return ((self.X ** 2) + (self.Y ** 2)) ** 0.5

    def __str__(self):  # To represent in string
        return 'Point ( {} , {} )'.format(self.X, self.Y)

    def __add__(self, otherpoint):  # To add the two points in class
        return Point2(self.X + otherpoint.X,
                      self.Y + otherpoint.Y)

    def __sub__(self, otherpoint):  # To sub two points in class
        return Point2(self.X - otherpoint.X,
                      self.Y - otherpoint.Y)

    def halfway(self, target):  # To get the mid point
        mX = (self.X + target.X) / 2
        mY = (self.Y + target.Y) / 2
        return mX, mY


p1 = Point2(7, 8)  # Invoking the class
p2 = Point2(9, 2)
print(p1)
print(p2)
print("Add", p1 + p2)
print("Sub", p1 - p2)

mid = p1.halfway(p2)  # return a new point that is halfway between p and q
print("MID POINT ", mid)

#######################################################################################
print("_________________________________________________________________________________________")


########################################################################################


class cars:
    def __init__(self, name1, variant):
        self.name = name1
        self.variant = variant

    def sort_priority(self):
        return self.variant


L = [
    cars('Swift', 'VDI'),
    cars('Ertiga', 'ZDI'),  # List
    cars('Ciaz', 'LDI')
]

for f in sorted(L, key=cars.sort_priority):  # Sorted based on the alphabet order of the values
    print(f.name)

for h in sorted(L, key=lambda x: x.sort_priority()):  # using lambda functions
    print("Using the lambda", h.name)

################################################################################################################3333
print("__________________________________________________________________________________------")


####################################################################################################################

# Class variable and Instance variable

class Point3:
    printed_rep = "*"  # to print the point style

    def __init__(self, initX, initY):  # Constructor
        self.x = initX
        self.y = initY

    def graph(self):  # To draw the graph
        row = []
        size = max(int(self.x), int(self.y)) + 2
        for j in range(size - 1):
            if (j + 1) == int(self.y):
                special_row = str((j + 1) % 10) + (" " * (int(self.x) - 1)) + self.printed_rep
                row.append(special_row)
            else:
                row.append(str((j + 1) % 10))
        row.reverse()
        x_axis = " "
        for k in range(size):
            x_axis += str(k % 10)
        row.append(x_axis)

        return "\n".join(row)


p3 = Point3(2, 3)

p4 = Point3(3, 12)

print(p3.graph())
print()
print(p4.graph())
print(p3.printed_rep)

#########################################################################################################
print("__________________________________________________________________________________________")
##########################################################################################################
# Inheriting variables and Methods

current_year = 2020


class Person:
    def __init__(self, name1, year):
        self.name = name1
        self.year = year

    def get_age(self):
        return current_year - self.year

    def __str__(self):
        return '{} is {}'.format(self.name, self.get_age())


balaji = Person("Balaji hari", 1994)

print("Age of :", balaji)

print("_______________________________________________________________________________")


class Student:
    def __init__(self, name1, year):
        self.name = name1
        self.year = year
        self.knowledge = 0

    def study(self):
        self.knowledge += 1

    def __str__(self):
        return ' {} : {} '.format(self.name, self.study())


varun = Student("Varun", 1994)
varun.study()
print(varun.knowledge)
########################################################################################################
print("_______________________________________________________________________________")
############################################################################################################

# Inheritance -  Easy way for class - inherite from another class

current_year = 2020


class Person:
    def __init__(self, name, year):
        self.name = name
        self.year = year

    def get_age(self):
        return current_year - self.year

    def __str__(self):
        return '{}:{}'.format(self.name, self.get_age())


balaji = Person("Balaji Hari", 1994)

print("Age of :", balaji)

print("_______________________________________________________________________________")


class Student(Person):
    def __init__(self, name, year):
        Person.__init__(self, name, year)
        super().__init__(name, year)
        self.knowledge = 0

    def study(self):
        self.knowledge += 1


varun = Student("Varun", 1994)
varun.study()
print("Using inheritance ", varun.knowledge)

######################################################################################################3
print("_______________________________________________________________________________")


########################################################################################################

# Override method -

class Book:  # Super class
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return '{} by {}'.format(self.title, self.author)


class Paperbook(Book):  # Sub class
    def __init__(self, title, author, num_pages):
        Book.__init__(self, title, author)
        self.num_pages = num_pages


class Ebook(Book):  # Sub class
    def __init__(self, title, author, size):
        Book.__init__(self, title, author)
        self.size = size


# composition

class Library():
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def get_num_books(self):
        return len(self.books)


mybook = Ebook('the Oddesay', 'Homer', 25)
print(mybook)
print(mybook.size)
mybook1 = Paperbook('Oddesay', 'Homer', 565)
print(mybook1.num_pages)

guindy = Library()
guindy.add_book(mybook)
guindy.add_book(mybook1)
print("No of Book in Library", guindy.get_num_books())

##############################################################################################################3
print("_______________________________________________________________________________")
################################################################################################################
from random import randrange


class Pet:
    boredom_decrement = 4
    hunger_decrement = 6
    boredom_threshold = 5
    hunger_threshold = 10
    sounds = ['Mrrp']

    def __init__(self, name="Kitty"):
        self.name = name
        self.hunger = randrange(self.hunger_threshold)
        self.boredom = randrange(self.boredom_threshold)
        self.sounds = self.sounds[:]

    def clock_tick(self):
        self.boredom += 1
        self.hunger += 1

    def mood(self):
        if self.hunger <= self.hunger_threshold and self.boredom_threshold:
            return 'happy'
        else:
            return "bored"

        def __str__(self):
            state = " I'am " + self.name + ". "
            state += " I'feel " + self.mood() + "."
            return state

        def hi(self):
            print(self.sounds[randrange(len(self.sounds))])
            self.reduce_boredom()

        def teach(self, word):
            self.sounds.append(word)
            self.reduce_boredom()

        def feed(self):
            self.reduce_hunger()

        def reduce_hunger(self):
            self.hunger = max(0, self.hunger - self.hunger_decrement)

        def reduce_boredom(self):
            self.boredom = max(0, self.boredom - self.boredom_decrement)


class PartyAnimal:
    x = 0

    def party(self):
        self.x = self.x + 1
        print("So far", self.x)


an = PartyAnimal()
print("Type", type(an))
print("Dir ", dir(an))
print("Type", type(an.x))
print("Type", type(an.party))

##############################################################################################################3
print("_______________________________________________________________________________")


################################################################################################################

class PartyAnimal:
    x = 0

    def __init__(self):
        print('I am constructed')

    def party(self):
        self.x = self.x + 1
        print('So far', self.x)

    def __del__(self):
        print('I am destructed', self.x)


an = PartyAnimal()
an.party()
an.party()
an = 42
print('An contains', an)

##############################################################################################################3
print("_______________________________________________________________________________")
################################################################################################################

#class  - python engineer

class SoftwareEngineer:
    alias = 'keyboard magician'   # class attributes - it belongs to the whole class

    def __init__(self,name,age, level,salary): # parameters
        # init - constructor -  is used to initialize the number of properties inside the class
        # instance attributes  - it only belongs to the particular instances
        # self parameter - it takes the reference of the particular object
        self.name = name  # attributes
        self.age = age
        self.level = level
        self.salary = salary


se1 = SoftwareEngineer('balaji',27,'junior',7000) # instance of the class

print(se1.name)  # calling the instances
print(se1.salary)
print(se1.age)
print(SoftwareEngineer.alias)


se2 = SoftwareEngineer('hari',35,'senior',12000)
print(se2.salary)
print(se2.name)
print(se2.age)

##############################################################################################################3
print("_______________________________________________________________________________")
################################################################################################################

#function in classes -

class SoftwareEngineer:
    alias = 'keyboard magician'   # class attributes

    def __init__(self,name,age, level,salary):
        #instance attributes
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary

    def code(self):  # instance method
        print("writing the code")

    def code_in_language(self,language):
        print("writing code in {}".format(language))

    def information(self):
        information = f"name = {self.name},age ={self.age},level = {self.level}"
        return information

    # dander methods - in-built
    def __str__(self):  # string representation of the class
        print('software engineer details')

    def __eq__(self, other):  # compare two objects
        return self.age == other and self.level == other

    @staticmethod  # decorator - avoid the self
    def entry_salary(age):
        if age > 25:
            return 5000
        else:
            return 9000


se1 = SoftwareEngineer('balaji',27,'junior',7000)

print(se1.salary)
print(se1.age)
print(SoftwareEngineer.alias)


se2 = SoftwareEngineer('hari',35,'senior',12000)

print(se2.salary)
print(se1.code())  # calling the values from the code methods
print(se2.code())
print(se1.code_in_language('Python'))  # calling the values from the language methods
print(se1 == se2)
print(se1.information())
print(se2.information)  # getting the value using the information methods
print(se1.entry_salary(23))
print(SoftwareEngineer.entry_salary(30))
##############################################################################################################3
print("_______________________________________________________________________________")
################################################################################################################

# Inheritance - The process which one class takes the values from the  another class
# parent class and the child class

class Employee:  # parent class
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary

    def work_center(self,center):  # Instances for the parent class or base class
        print('employee center',center)

    def work(self):
        print(f"{self.name} is working")

    def __str__(self):
        print('employee details')


class SoftwareEngineer(Employee):  # Child class
    def __init__(self, name, age, salary, level):
        super().__init__(name, age, salary)  # Overriding the class
        self.level = level

    def tool(self,tool):  # Instance for the child class
        print('tool used ',tool)

    def debug(self):
        print(f"{self.name} is debugging")

    def work(self):  # overiding the parent class instance methods
        print(f"{self.name} is coding")


class Designer(Employee):  # Child class
    def __init__(self, name, age, salary, project):
        super().__init__(name, age, salary)  # Overriding the parent class
        self.project = project

    def tool(self,tool): # Instance for the child class
        print("tool used ",tool)

    def draw(self):
        print(f"{self.name} is working")

    def work(self):
        print(f"{self.name} is designing")  # overriding the parent class instance methods

se1 = SoftwareEngineer('balaji',27,5000,'junior')
de1 = Designer('hari',25,3000,'python')

se1.debug()
se1.work()  # calling the overridden methods

de1.draw()
se1.work() # calling the overridden methods


# Polymorphism -  code works on the superclass and subclass

employees = [SoftwareEngineer('balaji',27,5000,'junior'),
                    SoftwareEngineer('balaji',27,5000,'junior'),
                    Designer('hari',25,3000,'python')]

def motivate_employees(employees):
    for employee in employees:
        employee.work()

motivate_employees(employees)

##############################################################################################################3
print("_______________________________________________________________________________")
################################################################################################################

# Encapsulation - hiding the data - instance variables are kept private - it restricts the access

# Private - the variable is partially hidden  - over-riding is possible

# protected - the variable is only accessed by the subclass and cannot able to access outside the particular class

class SoftwareEngineer:
    def __init__(self, name, age):
        self.name = name # public
        self.age  = age # public
        self.__salary = None  # private - double underscore
        self.__bugs = 0  # private -  double underscore

    def code(self):
        self.__bugs +=1

    #getter - only way to access the private variables
    def get_salary(self): # public function
        return self.__salary

    # setters  - only way to access the private variables
    def set_salary(self,value):  # public function
        if value < 1000:
            self.__salary = 1000
        if value >20000:
            self.__salary = 20000
        else:
            self.__salary = value

    def _calculate_Salary(self,base_value):
        if self.__bugs < 10:
            return base_value
        elif self.__bugs < 100:
            return base_value*2
        else:
            return base_value *3

se = SoftwareEngineer('max' , 25)

print(se.age)
print(se.name)

for i in range(70):
    se.code()

se.set_salary(6000)
print(se.get_salary())

##############################################################################################################3
print("_______________________________________________________________________________")
################################################################################################################

# Properties - use this instead of setter and getters

class SoftwareEngineer:

    def  __init__(self):
        self.__salary = None

    @property # decorators  - getter
    def salary(self):
        return self.__salary

    @salary.setter # decorators - setter
    def salary(self,value):
        self.__salary = value

se = SoftwareEngineer()

se.salary = 7000
print(se.salary)