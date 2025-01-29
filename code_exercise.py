

print("\nQ2a\n")
# Q2a: write a function which takes a letter (as a string) as an input and outputs it's position in the alphabet
# alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
#             "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

# A2a:



print("\nQ2b\n")
# Q2b: create a function which takes a persons name as an input string and returns an
# ID number consisting of the positions of each letter in the name
# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14

# A2b:

def code(name):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                 "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

    positions = []
    for letter in name.lower():
        if letter in alphabet:
            positions.append(str(alphabet.index(letter)))

    result = "".join(positions)
    return result

print(code("bob"))



def generate_password(name):

    id = code(name)

    sum_of_id = 0
    for i in id:
        sum_of_id += int(i)

    password = int(id) - sum_of_id
    return password

print(generate_password("bob"))