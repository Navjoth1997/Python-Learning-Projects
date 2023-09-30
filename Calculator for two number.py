#Calculator for two number

print("This game is designed by Navjoth Singh")
Name = input("Please, Enter your name: ")
print("hello",Name,"Welcome to this game")

print('choose operation you wants to perform')
print('1. addition')
print('2. Subtraction')
print('3. division')
print('4. multiplication')
print('5. modulus')
print('6. Exponential')
print('7. Floor division')

operation= input('Enter No:')
a=input('a=') 
b=input('b=')

if(operation=='1'):
    print('the addition of number is',int(a)+int(b))
elif(operation=='2'):
    print('the subtraction of number is',int(a)-int(b))
elif(operation=='3'):
    print('the division of number is',int(a)/int(b))
elif(operation=='4'):
    print('the multiplication of number is',int(a)*int(b))
elif(operation=='5'):
    print('the modulus of number is',int(a)%int(b))
elif(operation=='6'):
    print('the exponential of number is',int(a)**int(b))
elif(operation=='7'):
    print('the floor division of number is',int(a)//int(b))
else:
    print('Incorrect number selected')


    