# Try and Except

items = ['a', 'b', 'c']

try:  # program try to run the program first if error happens it runs except
    print('a')
    third = items[2]
    print('b')
except:  # otherwise
    print("something went wrong")
    third = False
print("i want to run")

#####################################################################################################################3
print("_______________________________________________________________________________")
#########################################################################################################################


fname = input('Enter the file name: ')
if fname == 'na na boo boo':
    print('NA NA BOO BOO TO YOU - You have been punkd!')
    exit()

try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)

#####################################################################################################################3
print("_______________________________________________________________________________")
#########################################################################################################################


inp = input('Enter Fahrenheit Temperature:')
try:
    fahr = float(inp)
    cel = (fahr - 32.0) * 5.0 / 9.0
    print(cel)
except:
    print('Please enter a number')

#####################################################################################################################3
print("_______________________________________________________________________________")
#########################################################################################################################
total = 0
count = 0
while (True):
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

#####################################################################################################################3
print("_______________________________________________________________________________")
#########################################################################################################################


inp = input('Enter score: ')
try:
    score = float(inp)
except:
    score = -1

if score > 1.0 or score < 0.0:
    print('Bad score')
elif score > 0.9:
    print('A')
elif score > 0.8:
    print('B')
elif score > 0.7:
    print('C')
elif score > 0.6:
    print('D')
else:
    print('F')

#####################################################################################################################3
print("_______________________________________________________________________________")
#########################################################################################################################


fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)

#####################################################################################################################3
print("_______________________________________________________________________________")
#########################################################################################################################

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
count = 0
total = 0
for line in fhand:
    words = line.split()
    if len(words) != 2: continue
    if words[0] != 'X-DSPAM-Confidence:': continue
    try:
        conf = float(words[1])
    except:
        continue
    count = count + 1
    total = total + conf
average = total / count
print('Average spam confidence:', average)

#####################################################################################################################3
print("_______________________________________________________________________________")
#########################################################################################################################

fname = input('Enter file name: ')
fhand = open(fname)
c = dict()
for line in fhand:
    if not line.startswith('From '): continue
    pieces = line.split()
    time = pieces[5]
    parts = time.split(':')
    hour = parts[0]
    c[hour] = c.get(hour, 0) + 1

lst = list()
for key in c:
    value = c[key]
    lst.append((value, key))

lst.sort()

for value, key in lst:
    print(key, value)
