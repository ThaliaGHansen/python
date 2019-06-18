
#this will print out what?
#1
#x = 5 
#y = 10
#if 2 * x >10:
    #print ("we got it right")
#else:
    #print ("practice ya tables")    

#data = [50,100,90,55,1001,42,35]
    #multiply each element by 10
    #[500,1000,900,...]
#times_ten= []

#for d in data:
       # times_ten.append (d*10)
#only append if the d* 10 is < 600
        #print (lens(times_ten) #growing each time


#List comprehension 

# The list of candies to print to the screen
#candyList = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit", "Swedish Fish",
             #"Skittles", "Hershey Bar", "Starbursts", "M&MS"]

# The amount of candy the user will be allowed to choose
#allowance = 5

# The list used to store all of the candies selected inside of
#candyCart = []

# Print out options
#for i in range(len(candyList)):
    #print("[" + str(i) + "] " + candyList[i])

    #5x, ask them what they want, keep track of that choice somehow
#for x in range (allowance):
    #selection = input ("What candy would you like add?")

    
#candyList.append(5)
#print (selection,candyList)


    #do something with the selection , hint append to the candyCart!


#for element in candyCart:
        #print (element,candyList[element])


#import os
#os is part of the python standard lib 

#print(os.getcwd())

#print(os.path.join(".", "Resources","input.txt"))
#print(os.path.abspath(os.path.join(".", "Resources","input.text")))
#for _file in os.listdir("."):
#print(_file)

#context manager 'r' read, 'a' is append 'w' write
#with open()


# import csv

# with open ("../Resources/accouting.csv", "r") as f:
#         reader = csv.reader (f)
#         reader = csv.DictReader (f)
# #skip the first row by using next 
# next (reader)
# #skip another just enter another next 

#         for row in reader:
#             print (row)
# #to print the first name 
#     print (dict(row)['First Name'])

# #to print out a line item instead of a row
#     print (row,2)


import csv 
imp

with open("../Resources/accounting.csv", "r") as f:
    reader = csv.reader(f)
    #reader = csv.DictReader(f)
    # Prefer the dictionary reader
    next(reader) # skips theheader row
    for row in reader:
        print(row[-1])