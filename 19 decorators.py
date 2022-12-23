# decorators -Decorators are very powerful and useful tool in Python since it allows programmers to modify the behavior of function or class.
# Decorators allow us to wrap another function in order to extend the behavior of the wrapped function,
# without permanently modifying it.
#  it allows new function to the existing function

def start_end_decorators(func):  # decorator function

    def wrapper():
        print('start')
        func()
        print('end')

    return wrapper


@start_end_decorators  # the behavior of the function is extended, the decorator is injected into the fucntion for more functionality
def print_name():
    print('alex')


print_name()

#####################################################################################################################3
print("_______________________________________________________________________________")
#########################################################################################################################


def start_end_decorators(func):  # decorator function

    def wrapper(*args,**kwargs):
        print('start')
        result=func(*args,**kwargs)
        print('end')
        return result

    return wrapper


@start_end_decorators
def add5(x):
    return x+5

result = add5(10)
print(result)

print(add5.__name__)

#####################################################################################################################3
print("_______________________________________________________________________________")
#########################################################################################################################

def car(func):

    def details():
        print('details are')
        func()

    return details
@car
def model():
    print("swift")


model()

#####################################################################################################################3
print("_______________________________________________________________________________")
#########################################################################################################################

def multiply(func):
    def multi(*args,**kwargs):
        print('start adding')
        result = func(*args,**kwargs)
        print('finish muliplying')
        return result *3
    return multi

@multiply
def add(x,y):
    return x+y

result = add(10,10)
print(result)

#####################################################################################################################3
print("_______________________________________________________________________________")
#########################################################################################################################

import functools

def repeat(num_times):
    def decorator_repeat(func):

        def wrapper(*args,**kwargs):
            global result
            for _ in range(num_times):
                result = func(*args,**kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=4)  # decorator with arguments
def greet(name):
    print("hello",name)
greet('alex')


class Count:  # class decorators
    def __init__(self,func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls +=1
        print(self.num_calls)
        return self.func(*args,**kwargs)

@Count
def say_hello():
    print('hello')

say_hello()
say_hello()
say_hello()


#####################################################################################################################3
print("_______________________________________________________________________________")
#########################################################################################################################
