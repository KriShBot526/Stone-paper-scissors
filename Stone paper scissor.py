import random
import regex as re

user_score = 0
comp_score = 0

while True:
    print("\n")
    print("Rock, Paper, Scissor... Shoot!")

    user_input = input("Enter [R]ock/[P]aper/[S]cissor or press to [Q]uit: ")
    
    if(not re.match("[RrPpSsQq]", user_input)) or (len(user_input) != 1):
        print("Please Choose a letter")
        print("[R]ock/[P]aper/[S]cissor or [Q]uit")
        continue

    print(f"You chose {user_input}")

    if user_input.upper() == "Q":
        print("Exiting Game...")
        print(f"Your score is {user_score} and computer score is {comp_score}")
        quit()

    choices = ["R", "P", "S"]

    comp_choice = random.choice(choices)
    print(f"I chose {comp_choice}")


    if comp_choice == user_input.upper():
        print("Ended in a draw")

    elif comp_choice == "R" and user_input.upper() == "S":
        print("Rock beats scissors! I win!")
        comp_score += 1

    elif comp_choice == "S" and user_input.upper() == "P":
        print("Scissors beats paper! I win!")
        comp_score += 1

    elif comp_choice == "R" and user_input.upper() == "S":
        print("Paper beat rock, I win!")
        comp_score += 1
        
    else:
        print("You win!")
        user_score += 1
