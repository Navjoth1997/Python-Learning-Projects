# the sum of total numeric value of characters in a name

print("This is designed by Navjoth Singh")
name = input("Please, Enter your name: ")

def calculate_name_position(name):
    name = name.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    total_position = 0
    for char in name:
        if char in alphabet:
            position = alphabet.index(char) + 1
            total_position += position
    return total_position

result = calculate_name_position(name)
print("Sum of character:", result)

