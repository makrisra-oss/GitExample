

# Q2b: create a function which takes a persons name as an input string and returns an
# ID number consisting of the positions of each letter in the name
# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14

# A2b:

# def function(user_input):
#     alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
#                 "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
#     for letter in user_input:
#         if letter in alphabet:
#             position = alphabet.index(letter + 1)
#
# function('bob')

def function2(user_input):
    dict = {
        "a": "0",
        "b": "1",
        "c": "2",
        "d": "3",
        "e": "4",
        "f": "5",
        "g": "6",
        "h": "7",
        "i": "8",
        "j": "9",
        "k": "10",
        "l": "11",
        "m": "12",
        "n": "13",
        "o": "14",
        "p": "15",
        "q": "16",
        "r": "17",
        "s": "18",
        "t": "19",
        "u": "20",
        "v": "21",
        "w": "22",
        "x": "23",
        "y": "24",
        "z": "25",
        " ": "26"
    }

    positions = []
    for letter in user_input:
        if letter in dict:
            position = dict[letter]
            positions.append(position)
    result = int(''.join(positions))
    return result

print(function2("bob"))


print("\nQ2c\n")
# Q2c: Create a function which turns this ID into a password. The function should subtract
# the sum of the numbers in the id that was generated from the whole number of the id.
# e.g. f("bob") -> 1134 (because bob's id was 1141 and 1+1+4+1 = 7 so 1141 - 7 = 1134)

# A2c:

def generate_password(input):
    dict = {
        "a": "0",
        "b": "1",
        "c": "2",
        "d": "3",
        "e": "4",
        "f": "5",
        "g": "6",
        "h": "7",
        "i": "8",
        "j": "9",
        "k": "10",
        "l": "11",
        "m": "12",
        "n": "13",
        "o": "14",
        "p": "15",
        "q": "16",
        "r": "17",
        "s": "18",
        "t": "19",
        "u": "20",
        "v": "21",
        "w": "22",
        "x": "23",
        "y": "24",
        "z": "25",
        " ": "26"
    }

    code = []
    for char in input:
        code.append(dict[char])

    total = 0
    for num in code:
        for char in num:
            total += int(char)

    return int(''.join(code)) - total

print(generate_password("bob"))

print("\nQ1a\n")
# Q1a: Write a function which takes in an integer as an argument and returns the divisors of that number as a list
# e.g. f(12) = [1, 2, 3, 4, 6, 12]
# hint: range(1, n) returns a collection of the numbers from 1 to n-1

# A1a:

def function(integer):
    list = []
    for i in range(1, integer + 1):
        if integer % i == 0:
            list.append(i)
    return list

print(function(12))

print("\nQ1b\n")
# Q1b: Write a function which takes in two integers as arguments and returns true if one of the numbers
# is a factor of the other, false otherwise
# (bonus points if you call your previous function within this function

# A1b:

def function(integer1, integer2):
    if integer1 % integer2 == 0 or integer2 % integer1 == 0:
        return True
    else:
        return False

print(function(12, 24))
print(function(35, 31))


print("\nQ2a\n")
# Q2a: write a function which takes a letter (as a string) as an input and outputs it's position in the alphabet
# alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
#             "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

# A2a:

def position(letter):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
    return alphabet.index(letter)

print(position("g"))

print("\nQ2b\n")
# Q2b: create a function which takes a persons name as an input string and returns an
# ID number consisting of the positions of each letter in the name
# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14

# A2b:

def password(name):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

    positions = []
    for letter in name:
        positions.append(letter)
        result = ''.join(map(str, positions))


    return result

print(password("bob"))

def password(name):

    positions = []
    for letter in name:
        positions.append(letter)
        result = ''.join(map(str, positions))

    return result

print(password("bob"))

def password(name):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    positions = []
    for letter in name.lower():
        if letter in alphabet:
            positions.append(alphabet.index(letter))

    result = ''.join(map(str, positions))

    return result

print(password("bob"))



def generate_password(name):

    id = code(name)

    sum_of_id = 0
    for i in id:
        sum_of_id += int(i)

    password = int(id) - sum_of_id
    return password

print(generate_password("bob"))

# def password(name):
#     alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
#                 "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
#


# def password(name):
#     # Define the alphabet
#     alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
#                 "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
#
#     # Function to find the position of a letter in the alphabet
#     def position(letter):
#         return alphabet.index(letter.lower()) + 1  # Get position (1-based)
#
#     # Step 1: Create a list of positions for each letter in the name
#     positions = []
#     for letter in name:
#         if letter.lower() in alphabet:  # Ensure valid letter
#             positions.append(position(letter))
#
#     # Step 2: Join the positions into a single number
#     result = int(''.join(map(str, positions)))
#
#     # Step 3: Calculate the sum of digits of the result
#     subtract = sum(int(digit) for digit in str(result))
#
#     # Step 4: Return the result after subtraction
#     return result - subtract
#
# # Test the function
# print(password("bob"))  # Output: 215152 - (2 + 1 + 5 + 1 + 5 + 2) = 215136
# print(password("alice"))  # Test with another name
# print(password("zoo"))  # Test with a short name