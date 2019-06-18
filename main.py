 import os
import csv
# HW INSTRUCTIONS
# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The average of the changes in "Profit/Losses" over the entire period
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period
monthcount = 0
totalrev = []
currentrevenue = []
prevrevenue = 0
revenue_change = []
revenue_changes = []
months = []
max_month_index =0
min_month_index= 0
#file_path= os.path.join("PyBank","Resources","budget_data.csv")
#print (os.getcwd()
#/Users/admin/Desktop/DENVDEN201905DATA4-homework/Homework/3 Python  6-18/PyBank/Resources/budget_data.csv
 
with open('./budget_data.csv','r') as csvfile:
    csvfilereader =csv.reader (csvfile)
    READ = csv.reader(csvfile, delimiter=',')
    header=next(READ) #after the header
    
    for row in READ:
        monthcount = monthcount + 1
        months.append(row[0])  
        totalrev.append(int(row[1]))
        if monthcount > 1:
          currentrevenue = (float(row[1]))

         
          
          revenue_change= currentrevenue - prevrevenue
          revenue_changes.append(revenue_change)
          prevrevenue = currentrevenue
          #totalrev = totalrev + currentrevenue 

sum_rev_changes = sum(revenue_changes)
AverageChange = sum_rev_changes /(monthcount -2)
max_change = max(revenue_changes)
min_change = min(revenue_changes)
max_month_index = revenue_changes.index(max_change)
min_month_index = revenue_changes.index(min_change)
max_month = months[max_month_index]
min_month = months[min_month_index]
#print(sum(profit_losses))
    #print (len(months))
Greatest_Increase_in_Profits = 0 
Greatest_Decrease_in_Profits = 0 
#where my data is in my desktop 
#/Users/admin/Desktop/DENVDEN201905DATA4-homework/Homework/3\ Python\ \ 6-18/main.py

print("Financial Analysis") #Header
print("------------------------")  #Border
print("Total Months:", len(months))
print("Total: $", sum(totalrev))
print("Average Change:$",(AverageChange/-2))
print("Greatest Increase in Profits:{max_month}(${max_change})")
print("Greatest Decrease in Profits: {min_month}(${min_change})")


for _ in range(5):
    name = input("Please enter the name of someone you know. ")
    names.append(name)
# @TODO: Use a list comprehension to create a list of lowercased names
lowercased = [x.lower() for x in names]
# @TODO: Use a list comprehension to create a list of titlecased names
# https://www.tutorialspoint.com/python/string_title.htm
titlecased = [x.title() for x in names]
invitations = [
    f"Dear {name}, please come to the wedding this Saturday!" for name in titlecased]
for invitation in invitations:
    print(invitation)