# game of rock, paper, scissors 
# keeps track of user_wins and computer_wins 
import random

user_wins = 0
comp_wins = 0
draws = 0

options = ["rock", "paper", "scissor"]

while True:
    user_pick = input("Pick Rock/Paper/Scissors to play or q to quit: ").lower()

    if user_pick == "q":
        break
    elif user_pick not in options:
        print("Invalid option choose once again****")
        continue
    
    random_number = random.randint(0,2)
    # 0-rock, 1-paper, 2-scissor
    comp_pick = options[random_number]

    if (user_pick == "rock" and comp_pick == "scissor") or (user_pick == "paper" and comp_pick == "rock") or (user_pick == "scissor" and comp_pick == "paper"):
        print("Computer choose " +comp_pick)
        print("You won!")
        user_wins += 1

    elif user_pick == comp_pick:
        print("Both of you choose same")
        print("Draw!!")
        draws += 1

    else:
        print("Computer choose " +comp_pick)
        print("You Loose!")
        comp_wins += 1

print("You won",user_wins,"times and computer won",comp_wins,"and draws are",draws,"times out of",user_wins+comp_wins+draws,"total games")

print("Goodbye !!")