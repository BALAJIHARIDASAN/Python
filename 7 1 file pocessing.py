#chuck file processing

handle = open('mbox.txt','r') #To open the file in the python
int=handle.read() # TO read the lines in the file
print(len(int)) # To get the length of the file

######################################################################33
print("______________________________________________________________________________________")
###########################################################################


handle = open('mbox.txt','r')
count = 0
for line in handle:
    count=count+1
print("lines in file :",count)


######################################################################33
print("______________________________________________________________________________________")
###########################################################################

handle2 = open('mbox.txt','r')
for line1 in handle2:
    line1=line1.strip()  #To remove the white space in the file
    if line1.startswith('From'): # Execute the line start with the entered character
        print(line1)

######################################################################33
print("______________________________________________________________________________________")
###########################################################################



