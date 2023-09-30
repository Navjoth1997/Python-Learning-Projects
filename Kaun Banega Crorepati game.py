#Kaun Banega Crorepati game

Amount = ["10000","100000","200000"]
Questions = ["Q1. The language of Lakshadweep(Union Territory of India), is","Q2. Bahubali festival is related to","Q3. Who is the author of the epic 'Meghdoot"]
Options = ["A. Tamil B. Hindi C. Malayala D. Telugu","A. Islam B. Hinduism C. Buddhism D. Jainism","A. Vishakadatta B. Valmiki C. Banabhatta D. Kalidas"]
Correct_answer = ["C","D","D"]
Comments = ["-> Here comes your First Question","-> Good, keep going","-> Wow,you answered 2 Question right, Now answer this one"]
Total_Amount = 0

print("This game is designed by Navjoth Singh")
Name = input("Please, Enter your name: ")
print("hello",Name,"Welcome to this game")
input("Are you ready(Yes/No): ")

for i in range(len(Questions)):
    print(Comments[i])
    print(Questions[i])
    print(Options[i])
    Answer = input("Type your answer: ")
    if Answer.upper() == Correct_answer[i]:
        print("Correct Answer,",Name)
        Total_Amount = Amount[i]
        if i == len(Questions)-1:
            print("Thank you for playing this game", Name)
            print("Your total winning amount is:", Total_Amount)
            break
        else:
            print(Name,",Your winning amount is:", Amount[i])
    else:
        print("Sorry, Wrong answer", Name)
        print(Name,",Your winning amount is:", Total_Amount)
        break

 