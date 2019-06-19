import csv

with open('./election_data.csv','r') as csvfile:
    csvfilereader =csv.reader (csvfile)
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    counttotalvotes = 0
    votes=[]
    candidates= {}
    collections = []
    elections = {}
    # {candidates,votes}
    nominees = {}
    winnernominees = 0
    winner = ""

    for row in csvreader:
            counttotalvotes += 1
            candidates = row[2]
            if candidates in elections:
                elections[candidates] += 1 
            else:
                elections[candidates] = 1

    for person, vote_count in elections.items():
        nominees[person] ="'{0:.0%}.format{vote_count / counttotalvotes}'"
        if vote_count > winnernominees:
         winnernominees = vote_count
         winner = "person"

# for row in reader 
# count =+1 
# candidate = row[2]
 
#  if candidate in elections 
#   elections [candidate]
#sum(list)

print ("Election Results")
print ("----------------")
print ("Total Votes:{counttotalvotes}")
print ("----------------")
# print ("Khan:")
# print ("Correy:")
# print ("Li:")
# print ("O'Tooley:")
for person, vote_count in elections.items():
   print(f"{person}:{nominees[person]}{vote_count}")


print ("---------------")
print ("Winner:{winner}")
print ("---------------")


# filepath = os.path.join(".", save_file)
with open("./electionresults.txt",'w') as text:
  text.write("Election Results" + "\n")
  text.write("----------------" + "\n")
  text.write(f"Total Votes:{counttotalvotes}" + "\n")
  text.write("----------------" + "\n")
  for person, vote_count in elections.items():
      text.write(f"{person}:{nominees[person]}{vote_count}" + "\n")
      text.write("---------------" + "\n")
      text.write(f"Winner: {winner}" + "\n")
      text.write("---------------" + "\n")