# Guess the correct number

import random

print("This game is designed by Navjoth Singh")
Name = input("Please, Enter your name: ")
print("hello",Name,"Welcome to this game")
input("Are you ready(Yes/No): ")

target_numbers = ["39", "40", "38"]  
target_number = random.choice(target_numbers)
num = input("Guess the number :")

for char in target_number:
    if(num == target_number):
        print("You guess the correct number i.e. :", target_number)
        break
    print('You entered wrong number, please try again')
    break

while( num != target_number ):
    num = input("Guess the number :")
    if(num == target_number):
        print("You guess the correct number i.e. :", num)
        break
    print(num,'is incorrect number, Please try again')
