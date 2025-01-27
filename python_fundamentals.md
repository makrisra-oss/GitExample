# Python Fundamentals  

## 1. Introduction to Python  

### What is Python?  
- **Python** is a high-level, interpreted programming language known for its simplicity and readability.  
- It supports multiple programming paradigms: procedural, object-oriented, and functional.  
- Widely used in web development, data science, AI, automation, and more.  

### Key Features:  
- Easy-to-read syntax.  
- Extensive standard library.  
- Platform-independent.  
- Dynamically typed (no need to declare variable types).  

---

## 2. Python Basics  

### Variables and Data Types  
```python
# Variables
x = 10        # Integer
y = 3.14      # Float
name = "Alice"  # String
is_valid = True  # Boolean
Data Structures
List: Ordered, mutable collection.
fruits = ["apple", "banana", "cherry"]
Tuple: Ordered, immutable collection.
point = (3, 4)
Set: Unordered collection of unique items.
colours = {"red", "blue", "green"}
Dictionary: Key-value pairs.
person = {"name": "Alice", "age": 30}
Control Flow

```

### If-else statement

```
if x > 5:
    print("x is greater than 5")
else:
    print("x is 5 or less")

# For loop
for fruit in fruits:
    print(fruit)
```
### While loop

```
while x > 0:
    print(x)
    x -= 1
    
 ```
### Functions
```
def greet(name):
return f"Hello, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!
```
## 3. Object-Oriented Programming (OOP)

### Classes and Objects
```
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"
```

### Create an object
```
dog = Animal("Dog")
print(dog.speak())  # Output: Dog makes a sound
Inheritance
class Dog(Animal):
    def speak(self):
        return f"{self.name} barks"

my_dog = Dog("Buddy")
print(my_dog.speak())  # Output: Buddy barks
4. File Handling
```
### Reading and Writing Files
### Writing to a file

```
with open("example.txt", "w") as file:
    file.write("Hello, world!")

```
### Reading from a file

```
with open("example.txt", "r") as file:
    content = file.read()
    print(content)  # Output: Hello, world!
```
# 4. Error Handling

```
Try-Except Block
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("This block always executes")
```