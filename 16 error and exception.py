# Error and exception - syntax error,
# typeerror,
# module error,
# name error,
# file error,
# key error
# value error,
# index error,
# dictionary error,
# division by zero error


a = -5
if a < 0:
    raise Exception('number must be positive')  # it will raise the error the user defined

##############################################################################################################3
print("_______________________________________________________________________________")
################################################################################################################

b = -5
assert (b >= 0), 'b is positive'  # it will give the assertion error

##############################################################################################################3
print("_______________________________________________________________________________")
################################################################################################################

# try and except error
try:
    c = 5/0
except:
    print('error happened')

a = 5
b = 10
try:
    c = a/b
except Exception as e:  # it generate the inbuilt error
    print(e)



##############################################################################################################3
print("_______________________________________________________________________________")
################################################################################################################

try:
   a = 5/1
   b = a+ '10'
except ZeroDivisionError as e:  # for 'a'
  print(e)
except TypeError as e: # for 'b'
  print(e)

##############################################################################################################3
print("_______________________________________________________________________________")
################################################################################################################

try:
    c = 5/0
except Exception as e:  # It will print the error in the data in built
    print(e)
else:
    print('everything is fine')  # Appears only there is no error in the data
finally:
    print('cleaning up')  # It will print everytime even there is the error

##############################################################################################################3
print("_______________________________________________________________________________")
################################################################################################################

# Error class - user defined errors

class ValueTooHighError(Exception): # class for user defined error
    pass

class ValueTooLowError(Exception):
    def __init__(self,message,value):
        self.message = message
        self.value = value

def test_value(x):
    if x >100:
        raise ValueTooHighError('value too high')
    if x<50:
        raise ValueTooLowError('value is too low ', x)

test_value(200)
# or
try:
    test_value(25)

except ValueTooLowError as e:
    print(e.value,e.message)

except ValueTooHighError as e:
    print(e)

else:
    print("every thing is fine")

finally:
    print('always calculating')