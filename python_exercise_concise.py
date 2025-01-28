

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