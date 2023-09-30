# Coding:
# if (the word contains atleast 3 characters):
#   Remove the first letter and append it at the end also append three random characters at the starting and the end
# else:
#   Simply reverse the string

# Decoding:
# if (the word contains less than 3 characters):
#   Reverse it
# else:
#   Remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Coding-Decoding-of-Message

print("This is designed by Navjoth Singh")
name = input("Please, Enter your name: ")
print(f"hello, {name} ")

import random

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def encode(message):
  en_code = ""
  words = message.split()
  for word in words:  
     if len(word)<3:
         en_code += word[::-1] + ""
     else:
         word2 = ''.join(random.choices(alphabet,k=3))+word[1:]+word[0]+''.join(random.choices(alphabet,k=3))
         en_code += word2 + " "
  return en_code

def decode(message):
  en_code = ""
  words = message.split()
  for word in words:  
     if len(word)<3:
         en_code += word[::-1] + " "
     else:
         word2 = word[-4]+word[3:-4]
         en_code += word2 + " "
  return en_code


Code = input("\nPlease select you want to encode(C) or decode(D) your message:").lower()

# Code= Code.lower()

if Code == "c":
 message = input("please enter for encryption:")
 print(encode(message))
elif Code == "d":
 message = input("please enter for encryption:")
 print(decode(message))
else:
 print("\nInvalid choice. Please enter 'C' for coding or 'D' for decoding.")


