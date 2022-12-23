# Search for lines that contain 'From'
import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From:', line):
        print(line)
##########################################################################
print("______________________________________________________________________________________________")
########################################################################################################

# Search for lines that start with 'From'

import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:', line):
        print(line)

print("______________________________________________________________________________________________")
#########################################################################################
# Search for lines that start with 'F', followed by
# 2 characters, followed by 'm:'
import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^F..m:', line):
        print(line)

# ###############################################################
print("______________________________________________________________________________________________")
#######################################################################################
# Search for lines that start with From and have an at sign
import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:.+@', line):
        print(line)
# #################################################################
print("______________________________________________________________________________________________")
###############################################################################
import re

s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\S+@\S+', s)
print(lst)

# #########################################################################
print("______________________________________________________________________________________________")
###########################################################################

# Search for lines that have an at sign between characters
import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('\S+@\S+', line)
    if len(x) > 0:
        print(x)

# #############################################################################
print("______________________________________________________________________________________________")
##############################################################################

# Search for lines that have an at sign between characters
# The characters must be a letter or number
import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('[a-zA-Z0-9]\S+@\S+[a-zA-Z]', line)
    if len(x) > 0:
        print(x)

# ##########################################################################
print("______________________________________________________________________________________________")
################################################################################
# Search for lines that have an at sign between characters
# The characters must be a letter or number
# The results will be slightly more accurate than re07.py for email addresses
import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('[a-zA-Z0-9\-.]\S+@[a-zA-Z0-9].\S+[a-zA-Z]', line)
    if len(x) > 0:
        print(x)

# ########################################################################
print("______________________________________________________________________________________________")
################################################################################
# Search for lines that start 'X' followed by any non whitespace
# characters and ':' then output the first group of non whitespace
# characters that follows
import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('^X\S*: (\S+)', line)
    if not x: continue
    print(x)
########################################################################
print("______________________________________________________________________________________________")
##############################################################################
# Search for lines that start with 'X' followed by any non
# whitespace characters and ':'
# followed by a space and any number.
# The number can include a decimal.
import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^X\S*: [0-9.]+', line):
        print(line)

########################################################################
print("______________________________________________________________________________________________")
##############################################################################

# Search for lines that start with 'X' followed by any
# non whitespace characters and ':' followed by a space
# and any number. The number can include a decimal.
# Then print the number if it is greater than zero.
import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('^X\S*: ([0-9.]+)', line)
    if len(x) > 0:
        print(x)
########################################################################
print("______________________________________________________________________________________________")
##############################################################################
# Search for lines that start with 'Details: rev='
# followed by numbers and '.'
# Then print the number if it is greater than zero
import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('^Details:.*rev=([0-9.]+)', line)
    if len(x) > 0:
        print(x)

########################################################################
print("______________________________________________________________________________________________")
##############################################################################
