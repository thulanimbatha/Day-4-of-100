# Rock, Paper, Scissors game
import random

options = ["rock", "paper", "scissors"]

hand = input("Rock(r), Paper(p) or Scissors(s)? ").lower()
comp_choice = random.choice(options)

if comp_choice[0] == hand:
    print("Draw!")
else:
    if comp_choice == "rock" and hand == "s":
        print("Rock beats Scissors! Comp wins")
    elif comp_choice == "paper" and hand == "r":
        print("Paper beats rock. Comp wins")
    elif comp_choice == "scissors" and hand == "p":
        print("Scissors beat paper. Comp wins")
    else:
        print("You win! Nice bro!")
