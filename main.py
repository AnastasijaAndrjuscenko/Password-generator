import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
# Creating empty list to make it easier to shuffle it in the end of the code.
password_not_random = []
# Taking random characters from lists and adding to empty list to create one password with letters/symbols/numbers.
# Result depends on the request
for letter in range(1, nr_letters + 1):
    password_not_random.append(random.choice(letters))

for sym in range(1, nr_symbols + 1):
    password_not_random.append(random.choice(symbols))

for numi in range(1, nr_numbers + 1):
    password_not_random.append(random.choice(numbers))

# After creating a list with password
# we shuffle it to make it harder to hack.
random.shuffle(password_not_random)
password_shuffled = ""
# Same procedure, but changing list to string to make it easier for input(easier for people who will need it)
for changing_to_string in range(0, len(password_not_random)):
    password_shuffled += password_not_random[changing_to_string]
print(f"Your password is: {password_shuffled}")
