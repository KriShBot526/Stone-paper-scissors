import random

user_score = 0
comp_score = 0

while True:
    rand = random.choice(["rock", "paper", "scissor"])

    user_input = input("Enter Rock/Paper/Scissor or press q to Quit: ").lower()
    if user_input == "q":
        print(f"Your score is {user_score} and computer score is {comp_score}")
        quit()

    if user_input in ["rock", "paper", "scissor"]:
        if rand == user_input:
            print("Ended in a draw")

        elif rand == "rock" and user_input == "paper":
            print("You win!!!")
            user_score += 1
        elif rand == "paper" and user_input == "scissor":
            print("You win!!!")
            user_score += 1
        elif rand == "scissor" and user_input == "rock":
            print("You win!!!")
            user_score += 1
        
        else:
            print("Computer wins!!!")
            comp_score += 1
    else:
        print("Wrong input!!!")