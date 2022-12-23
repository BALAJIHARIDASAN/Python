# API - APPLICATION PROGRAMMING INTERFACE  - ONE COMPUTER INTERFACE WITH ANOTHER COMPUTER
# REST - REPRESENTATIONAL STATE TRANSFER

# HTTP://                UMICH.EDU    /           ABOUT
# protocol            #server or domain       # path or argument

# IP ADDRESS - INTERNET PROTOCOL - UNIQUE NAME -192.168.1.1.247(0-255) for a computers

###########################################################################################################

# ROUTER -  BROWSER TO SERVER
# PACKET - DATA TRANSFER FORMAT (DATA SENT THROUGHT ONLINE)
# HTML - HYPER TEXT MARKUP LANGUAGE


# Fetching the page data -
# Translate domain name to ip address
# Open the connection
# Start sending message using the http protocol
# GET METHOD
# Receive as HTML
# Browser renders the HTML

import requests
import json

page = requests.get("https://api.datamuse.com/words?rel_rhy=funny")  # To open the page-data from web
print("Type of the file :", type(page))  # it print the type of the request object
print("Printing the first 150 text :", page.text[:150])   # it print the first 150 characters
print("Entering the page url :", page.url)  # print the url that was fetched
print("______________")
x = json.loads(page.text) # Turning the page.txt into a python list
print("Json file :", x)
print("Printing the index values :", x[0])  # Printing the index value
print(json.dumps(x, indent=2))  # print the result in the json format

####################################################################################################################
print("____________________________________________________________________________________________________")
####################################################################################################################3

def rythms(word):
    baseurl = requests.get("https://api.datamuse.com/words")
    dic = {}
    dic["rel_rhy"] = word
    dic["max"] = "4"
    words = baseurl.json()
    return [d['word'] for d in words]


print(rythms("funny"))

#############################################################################################################3333

r = requests.get("https://api.datamuse.com/words?rel_rhy=funny")
print(r.text)
print(r.url)

####################################################################################################################3
print("___________________________________________________________________________________________________________")
########################################################################################################################


