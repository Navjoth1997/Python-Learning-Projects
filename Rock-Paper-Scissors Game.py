# Game "rock-paper-scissors" where players use hand gestures to represent a rock, paper, or a scissors.
# The rock beats the scissors, the paper beats the rock, and the scissors beats the paper.
# Write a python program to create a Game "rock-paper-scissors" in Python.
# Whoever score 3 points first will win this game

import random

print("This game is designed by Navjoth Singh\n")

Name = input("Enter Your Name: ")
print(f"\nWelcome to this game {Name}")

Attribute = ("Rock","Paper","Scissors")

Computer_Score = 0
Score = 0
while True:
        if Score == 3 or Computer_Score == 3:
            break
        Action = input(f"\nPlease selct your attribute {Name} from Rock,Paper,Scissors : ").lower()
        if Action == "rock":
            Import = random.choice(Attribute).lower()
            print(f"\nYou chose {Action}.\nComputer chose {Import}.")
            if Import == "rock":
                print(f"\nDraw, No score awarded")
                print(f"\nComuter Current Score = {Computer_Score}")
                print(f"{Name}, Your Current Score = {Score}")
            elif Import == "paper":
                Score += 0
                Computer_Score += 1
                print(f"\nSorry, You loose this Round, Computer score is increased by 1")
                print(f"\nComuter Score = {Computer_Score}")
                print(f"{Name}, Your score = {Score}")
            else:
                Score += 1
                Computer_Score += 0
                print(f"\nHurray!, You win this Round and your score is increased by 1")
                print(f"\nComuter Current Score = {Computer_Score}")
                print(f"{Name}, Your Current Score = {Score}")
        elif Action == "paper":
            Import = random.choice(Attribute).lower()
            print(f"\nYou chose {Action}.\nComputer chose {Import}.")
            if Import == "rock":
                Score += 1
                Computer_Score += 0
                print(f"\nHurray!, You win this Round and your score is increased by 1")
                print(f"\nComuter Current Score = {Computer_Score}")
                print(f"{Name}, Your Current Score = {Score}")
            elif Import == "paper":
                print("\nDraw, No score awarded")
                print(f"\nComuter Current Score = {Computer_Score}")
                print(f"{Name}, Your Current Score = {Score}")
            else:
                Score += 0
                Computer_Score += 1
                print(f"\nSorry, You loose this Round, Computer score is increased by 1")
                print(f"\nComuter Score = {Computer_Score}")
                print(f"Your score = {Score}")
        elif Action == "scissors":
            Import = random.choice(Attribute).lower()
            print(f"\nYou chose {Action}.\nComputer chose {Import}.")
            if Import == "rock":
                Score += 0
                Computer_Score += 1
                print(f"\nSorry, You loose this Round, Computer score is increased by 1")
                print(f"\nComuter Score = {Computer_Score}")
                print(f"{Name}, Your score = {Score}")
            elif Import == "paper":
                Score += 1
                Computer_Score += 0
                print(f"\nHurray!, You win this Round and your score is increased by 1")
                print(f"\nComuter Current Score = {Computer_Score}")
                print(f"{Name}, Your Current Score = {Score}")
            else:
                print(f"\nDraw, No score awarded")
                print(f"\nComuter Current Score = {Computer_Score}")
                print(f"{Name}, Your Current Score = {Score}")
        else:
            print(f"\nSpeeling mistake, Please type correct word of selective attribute {Name}")


# print(f"\n{Name}, Your Final Score = {Score}")
# print(f"\nComputer, Final Score = {Computer_Score}\n")

if Score > Computer_Score:
    print(f"\n{Name} Wins")
elif Score == Computer_Score:
    print(f"\nGame Draw")
else:
    print(f"\nComputer Wins")

print("\nGame Over")
