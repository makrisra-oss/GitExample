from sympy import isprime

print("\nQ1a\n")
# Q1a: Print only the first 5 numbers in this list
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1a:

print(x[0:5])

print("\nQ1b\n")
# Q1b: Now print only the even numbers in this list (the elements that are themselves even)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1b:

for num in x:
    if num % 2 == 0:
        print(num)

print("\nQ1c\n")
# Q1c: Now only print the even numbers up to the fifth element in the list (e.g. 2, 4, 34)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1c:

for num in x[0:5]:
    if num % 2 == 0:
        print(num)

print("\nQ2a\n")
# Q2a: from the list of names, create another list that consists of only the first letters of each first name
# e.g. ["Alan Turing", "Leonardo Fibonacci"] -> ["A", "L"]
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2a:

new_list = []

for i in names:
    if i[0].isupper():
        new_list.append(i[0])

print(new_list)

print("\nQ2b\n")
# Q2b: from the list of names, create another list that consists of only the index of the space in the string
# HINT: use your_string.index("substring")
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2b:

new_list = []

for name in names:
    space_index = name.index(' ')
    new_list.append(space_index)

print(new_list)

# names = "Alan Turing"
#
# new_list = []
# for i in names:
#     if i == ' ':
#         new_list.append(names.index(i))
#
# print(new_list)

print("\nQ2c\n")
# Q2c: from the list of names, create another list that consists of the first and last initial of each individual
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2c:

new_list = []

for name in names:
    parts = name.split()

    initial = parts[0][0] + parts[1][0]
    new_list.append(initial)

print(new_list)

print("\nQ3a\n")
# Q3a: Here is a list of lists, print only the lists which have no duplicates
# Hint: This can be easily done by using sets as a set does not contain duplicates
list_of_lists = [[1,5,7,3,44,4,1],
                 ["A", "B", "C"],
                 ["Hi", "Hello", "Ciao", "By", "Goodbye", "Ciao"],
                 ["one", "Two", "Three", "Four"]]


# A3a:

# set_list_1 = set(list_of_lists[0])
# set_list_2 = set(list_of_lists[1])
# set_list_3 = set(list_of_lists[2])
# set_list_4 = set(list_of_lists[3])
#
# print(set_list_1)
# print(set_list_2)
# print(set_list_3)
# print(set_list_4)
#
# combined_set = set_list_1.union(set_list_2, set_list_4)
# print(combined_set)

for list in list_of_lists:
    if len(list) == len(set(list)):
        print(list)

print("\nQ4a\n")
# Q4a: Using a while loop, ask the user to input a number greater than 100, if they enter anything else,
# get them to enter again (and repeat until the conditions are satisfied). Finally print the number that
# they entered

# A4a:

print("\nQ4b\n")
# Q4b: Continue this code and print "prime" if the number is a prime number and "not prime" otherwise

# A4b:


# input_list = []
# user_input = int(input("Enter a number: "))
#
# while user_input < 100:
#     if isprime(user_input):
#         print(f"{user_input} is a prime number.")
#     else:
#         print(f"{user_input} is not a prime number.")
#     input_list.append(user_input)
#     user_input = int(input("Enter another number: "))
#
# print(input_list)

print("\nQ1a\n")
# Q1a: Write a function which takes in an integer as an argument and returns the divisors of that number as a list
# e.g. f(12) = [1, 2, 3, 4, 6, 12]
# hint: range(1, n) returns a collection of the numbers from 1 to n-1

# A1a:

def function(number):
    new_list = []
    for i in range(1, number + 1):
        if number % i == 0:
            new_list.append(i)
    print(new_list)

function(12)
function(50)

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

print(function(24, 8))
print(function(100, 17))
print("\nQ2a\n")
# Q2a: write a function which takes a letter (as a string) as an input and outputs it's position in the alphabet
# alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
#             "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

# A2a:
def function(user_input):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
    position = alphabet.index(user_input)

    result = alphabet.index(alphabet[position + 1])
    print(result)

function('b')
function('z')

print("\nQ2b\n")
# Q2b: create a function which takes a persons name as an input string and returns an
# ID number consisting of the positions of each letter in the name
# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14

# A2b:

def function(user_input):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
    for letter in user_input:
        if letter in alphabet:
            position = alphabet.index(letter + 1)


    # position = alphabet.index(user_input)
    #
    # result = alphabet.index(alphabet[position + 1])
    #
    # print(result)



# def function(name):
#     for i in name:
#         if i == 'a':
#             print('0')
#         elif i == 'b':
#             print('1')
#         elif i == 'c':
#             print('2')
#         elif i == 'd':
#             print('3')
#         elif i == 'e':
#             print('4')
#         elif i == 'f':
#             print('5')
#         elif i == 'g':
#             print('6')
#         elif i == 'h':
#             print('7')
#         elif i == 'i':
#             print('8')
#         elif i == 'j':
#             print('9')
#         elif i == 'k':
#             print('10')
#         elif i == 'l':
#             print('11')
#         elif i == 'm':
#             print('12')
#         elif i == 'n':
#             print('13')
#         elif i == 'o':
#             print('14')
#         elif i == 'p':
#             print('15')
#         elif i == 'q':
#             print('16')
#         elif i == 'r':
#             print('17')
#         elif i == 's':
#             print('18')
#         elif i == 't':
#             print('19')
#         elif i == 'u':
#             print('20')
#         elif i == 'v':
#             print('21')
#         elif i == 'w':
#             print('22')
#         elif i == 'x':
#             print('23')
#         elif i == 'y':
#             print('24')
#         elif i == 'z':
#             print('25')
#
# function('bob')
# function('sam')

# def code_name(name):
#     result = ""
#     for i in name:
#         result += str(get_position(i))
#
#     return result
#
# print(code_name("bob"))

print("\nQ2c\n")
# Q2c: Create a function which turns this ID into a password. The function should subtract
# the sum of the numbers in the id that was generated from the whole number of the id.
# e.g. f("bob") -> 1134 (because bob's id was 1141 and 1+1+4+1 = 7 so 1141 - 7 = 1134)

# A2c:


print("\nQ3a\n")
# Q3a: Write a function which takes an integer as an input, and returns true if the number is prime, false otherwise.

# A3a:

def function(integer):
    if isprime(integer):
        return True
    else:
        return False

print(function(100))
print(function(7))

print("\nQ3b\n")
# Q3b: Now add some functionality to the function which does not error if the user inputs something other than a digit

# A3b:
