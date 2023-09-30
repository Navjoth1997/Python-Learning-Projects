#Good Morning message

import time
print("This game is designed by Navjoth Singh")
Name = input("Please, Enter your name: ")

# timestamp = int(input("Please enter the time: "))    #if you wish you can do it manually
Realtime = time.strftime('%H:%M:%S')
timestamp = int(time.strftime('%H'))
print("the time at this moment is :" , Realtime)

if (0 <= timestamp < 3):
    print("Good Night",Name,",Sir/Mam")
elif (6 <= timestamp < 12):
    print("Good Morning",Name,",Sir/Mam")
elif (timestamp < 16):
    print("Good Afternoon",Name,",Sir/Mam")
elif( timestamp < 20):
    print("Good Evening",Name,",Sir/Mam")
elif( 20 <= timestamp < 24):
    print("Please have your dinner",Name,",Sir/Mam")
else:
    print("Go to sleep it's already too late",Name,",Sir/Mam")
