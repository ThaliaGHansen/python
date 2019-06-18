import random

choices =['Rock','Paper','Scissors']
user_choice = random.choice(choices)
computer_choice = random.choice(choices)


if user_choice=="Rock" and computer_choice =="Paper":
    print(f"The computer wins and they chose {computer_choice}")

elif user_choice=="Rock" and computer_choice == "Scissors":
        print(f" Thalia wins regarless with {user_choice}")

elif user_choice== "Scissors" and computer_choice =="Rock":
         print(f"Thalia wins regarless with {computer_choice}")


#paper covers rocks
#scirrors cut paper
#Rock smashes scissors 
#dont forget if they are the same 


