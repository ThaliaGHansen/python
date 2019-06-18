import csv 
import os 
# go back one level, which is the .., Hit rhe resources, then the filename
file_path = os.path.join("..", "Resources", "netflix_ratings.csv")

# If this is in unsolved
with open(file_path, "r") as f:
    search = input("What movie to search for: ")
    # do something with the search variable
    reader = csv.reader(f)
    next(reader) # skips theheader row
    for row in reader:
        if search in row[0]:
            print(row)

            break #just breaks out the loop

# search = search.lower().strip() #lowercase, remove leading and trailing spaces 

#reader (object - possible rows of your file)
#csv.reader represents the generator in python for element or thing 
#functions and dictionaries and reading and writing through CSVS 





            