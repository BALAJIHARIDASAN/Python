# Reading  whole file

file = open('mbox.txt', 'r')  # Enter the file name - To open the file
content = file.read()  # To read the file - Read the whole file
print(content[:150])  # To read the first 100 contents
file.close()

#######################################################################
print("__________________________________________________________________")
##########################################################################

# New line character - Print the character in the new line -"\n"

stuff = ' Hello\n World '

print(stuff)
print(len(stuff))

######################################################################
print("______________________________________________________________________________________")
###########################################################################

# Reading the file

file = open('mbox.txt', 'r')  # Enter the file name
contents = file.readlines()  # To read the whole file, line-by-line

print("Count of file Characters :", len(contents))  # Counting the character in the file

for lin in contents[:4]:  # Printing the first four line of the file
    print(lin.strip())  # Strip removes the whitespace in the file

file.close()
#####################################################################################################
print("__________________________________________________________________")
######################################################################################################

# Writing to the file

files = open("square.txt", "w")

for number in range(10):
    square = number * number
    files.write(str(square))  # Writing into file
    files.write("\n")  # New line character

newfile = open("square.txt", "r")
content1 = newfile.read()  # Reading the file
print(content1)  # Printing the content

newfile.close()
###########################################################################################################3
print("___________________________________________________________________________________________________")
##################################################################################################################

# Using "WITH" to open the files

with open("square.txt", "r")as md:  # Equivalent to above method like "open" method
    for line in md:
        print(line)
md.close()

##########################################################################################################
print("_______________________________________________________________________________________________________")
########################################################################################

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.find('@uct.ac.za') == -1:
        continue
    print(line)

##########################################################################################################
print("_______________________________________________________________________________________________________")
########################################################################################

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()  # To remove the White-Space in the file
    if not line.startswith('From '):  # Print the line start with the given condition
        continue
    words = line.split()  # Split the lines in the file
    print(words[2])  # Print the file based on the index value
##########################################################################################################
print("_______________________________________________________________________________________________________")
########################################################################################
fname = input('Enter the file name: ')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)
##########################################################################################################
print("_______________________________________________________________________________________________________")

########################################################################################

fhand = open('mbox-short.txt')
for line in fhand:
    words = line.split()
    # print 'Debug:', words
    if len(words) == 0: continue
    if words[0] != 'From': continue
    print(words[2])

##########################################################################################################
print("_______________________________________________________________________________________________________")
########################################################################################
fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    if len(words) > 0:
        if words[0] != 'From':
            continue
        print(words[2])

#####################################################################
print("____________________________________________________________")
####################################################################


# CSV format - comma separated values

file1 = open("hotel.csv", "r")
lin1 = file1.readlines()  # To read the file by line-by-line
for lin2 in lin1:
    print(lin2.strip())  # To remove the whitespace
print("________________")

header = lin1[0]
field = header.strip().split(',')  # To remove white space and split into list
print(field)

for row in lin1:
    vals = row.strip().split(',')  # To remove white space and split into list
    print(vals)
    print("count of line :", len(vals))

#########################################################################################
print("___________________________________________________________________________________________")
###################################################################

fname3 = input('Enter the file name: ')
try:
    fhand3 = open(fname3)
except:
    print('File cannot be opened:', fname3)
    exit()

counts = dict()
for line in fhand3:
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

print(counts)

#########################################################################################
print("___________________________________________________________________________________________")
###################################################################


import string

fname4 = input('Enter the file name: ')
try:
    fhand4 = open(fname4)
except:
    print('File cannot be opened:', fname4)
    exit()

counts = dict()
for line in fhand4:
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

print(counts)

#########################################################################################
print("___________________________________________________________________________________________")
###################################################################


# Search for lines that start with "From" and have an at sign
import re

hand = open('mbox.txt')
search = input('Enter a regular expression: ')
count = 0
for line in hand:
    line = line.rstrip()
    if re.search(search, line): count = count + 1

print('mbox.txt had', count, 'lines that matched', search)

#########################################################################################
print("___________________________________________________________________________________________")
###################################################################


fname = input('Enter file name: ')
fhand = open(fname)
c = dict()
for line in fhand:
    if not line.startswith('From '):
        continue
    pieces = line.split()
    email = pieces[1]
    c[email] = c.get(email, 0) + 1

print(c)

#########################################################################################
print("___________________________________________________________________________________________")
###################################################################

fname = input('Enter file name: ')
fhand = open(fname)
c = dict()
for line in fhand:
    if not line.startswith('From '): continue
    pieces = line.split()
    email = pieces[1]
    c[email] = c.get(email, 0) + 1

bigc = None
bige = None
for word in c:
    value = c[word]
    if bigc is None or value > bigc:
        bigw = word
        bigc = value

print(bigw, bigc)

#########################################################################################
print("___________________________________________________________________________________________")
###################################################################

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)

#########################################################################################
print("___________________________________________________________________________________________")
###################################################################

name = input('Enter file: ')
handle = open(name, 'r')
wordlist = list()
for line in handle:
    words = line.split()
    for word in words:
        if word in wordlist:
            continue
        wordlist.append(word)

wordlist.sort()
print(wordlist)

#########################################################################################
print("___________________________________________________________________________________________")
###################################################################

name = input('Enter file:')
handle = open(name, 'r')
counts = dict()

for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

bigcount = None
bigword = None
for word, count in list(counts.items()):
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)

#########################################################################################
print("___________________________________________________________________________________________")
###################################################################
