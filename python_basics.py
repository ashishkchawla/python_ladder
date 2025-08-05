"""
Python Learning Script
This script covers essential Python concepts with explanations, examples, and practice questions.
"""

# ===== 1. Syntax Basics =====
# Python is known for its clean and readable syntax.
# Basic syntax rules:
# - Indentation is used for code blocks (typically 4 spaces)
# - No semicolons needed at the end of lines
# - Comments start with #
# - Variables are dynamically typed

# Example
print("\nExample:")
print("Hello, World!")  # This prints a string
result = 5 + 3
print(f"5 + 3 = {result}")

# Practice Question 1
print("\nPractice Question 1:")
print("Write a program that prints your name and age using proper Python syntax.")

# ===== 2. Variables and Data Types =====
# Python has several built-in data types:
# - int: Integer numbers
# - float: Decimal numbers
# - str: Strings (text)
# - bool: Boolean values (True/False)
# - None: Represents absence of a value

# Examples
print("\nExamples:")
age = 25
print(f"Integer example - age: {age}, type: {type(age)}")

height = 1.75
print(f"Float example - height: {height}, type: {type(height)}")

name = "John"
print(f"String example - name: {name}, type: {type(name)}")

is_student = True
print(f"Boolean example - is_student: {is_student}, type: {type(is_student)}")

empty_value = None
print(f"None example - empty_value: {empty_value}, type: {type(empty_value)}")

# Practice Question 2
print("\nPractice Question 2:")
print("Create variables for:")
print("1. Your favorite number")
print("2. Your height in meters")
print("3. Your full name")
print("4. Whether you like Python (boolean)")
print("Then print all variables with their types.")

# ===== 3. Conditionals =====
# Conditional statements help make decisions in code using if, elif, and else statements.

# Examples
print("\nExamples:")
age = 18
if age < 18:
    print("You are a minor")
elif age == 18:
    print("You just became an adult")
else:
    print("You are an adult")

x, y = 10, 20
if x < y:
    print("x is less than y")
elif x == y:
    print("x equals y")
else:
    print("x is greater than y")

# Practice Question 3
print("\nPractice Question 3:")
print("Write a program that:")
print("1. Takes a number as input")
print("2. Checks if it's positive, negative, or zero")
print("3. If positive, checks if it's even or odd")
print("4. Prints appropriate messages for each case")

# ===== 4. Loops =====
# Python has two main types of loops: for and while loops.

# Examples
print("\nExamples:")
print("For loop with range:")
for i in range(5):
    print(i)

print("\nFor loop with list:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

print("\nWhile loop:")
count = 0
while count < 3:
    print(f"Count is {count}")
    count += 1

# Practice Question 4
print("\nPractice Question 4:")
print("Write a program that:")
print("1. Uses a for loop to print the first 10 Fibonacci numbers")
print("2. Uses a while loop to find the factorial of a given number")

# ===== 5. Functions =====
# Functions are reusable blocks of code that perform specific tasks.

# Examples
def greet(name):
    return f"Hello, {name}!"

def calculate_rectangle_area(length, width=1):
    return length * width

def sum_all(*args):
    return sum(args)

print("\nExamples:")
print(greet("Alice"))
print(f"Area with both parameters: {calculate_rectangle_area(5, 3)}")
print(f"Area with default width: {calculate_rectangle_area(5)}")
print(f"Sum of 1, 2, 3: {sum_all(1, 2, 3)}")

# Practice Question 5
print("\nPractice Question 5:")
print("Create a function that:")
print("1. Takes a list of numbers as input")
print("2. Returns a tuple containing the minimum, maximum, and average of the numbers")
print("3. Has a default parameter for rounding the average to a specified number of decimal places")

# ===== 6. Lists and Tuples =====
# Lists are mutable sequences, while tuples are immutable sequences.

# Examples
print("\nExamples:")
fruits = ["apple", "banana", "cherry"]
print("Original list:", fruits)

fruits.append("orange")
fruits.insert(1, "mango")
fruits.remove("banana")
print("Modified list:", fruits)

print("First two items:", fruits[:2])
print("Last two items:", fruits[-2:])

coordinates = (10, 20)
print("\nTuple:", coordinates)
print("First coordinate:", coordinates[0])

x, y = coordinates
print(f"Unpacked coordinates: x={x}, y={y}")

# Practice Question 6
print("\nPractice Question 6:")
print("Create a program that:")
print("1. Takes a list of numbers")
print("2. Creates a new list with only even numbers")
print("3. Creates a tuple with the original list's statistics (sum, average, min, max)")
print("4. Prints both the new list and the statistics tuple")

# ===== 7. Dictionaries and Sets =====
# Dictionaries store key-value pairs, while sets store unique elements.

# Examples
print("\nExamples:")
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print("Dictionary:", person)
print("Name:", person["name"])

person["job"] = "Developer"
del person["age"]
print("Modified dictionary:", person)

fruits = {"apple", "banana", "cherry"}
print("\nSet:", fruits)

fruits.add("orange")
fruits.remove("banana")
print("Modified set:", fruits)

set1 = {1, 2, 3}
set2 = {3, 4, 5}
print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference:", set1 - set2)

# Practice Question 7
print("\nPractice Question 7:")
print("Create a program that:")
print("1. Creates a dictionary of student grades")
print("2. Calculates the average grade for each student")
print("3. Creates a set of unique grades across all students")
print("4. Prints the student with the highest average grade")

# ===== 8. List Comprehensions =====
# List comprehensions provide a concise way to create lists based on existing lists.

# Examples
print("\nExamples:")
squares = [x**2 for x in range(5)]
print("Squares:", squares)

even_squares = [x**2 for x in range(10) if x % 2 == 0]
print("Even squares:", even_squares)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print("Flattened matrix:", flattened)

# Practice Question 8
print("\nPractice Question 8:")
print("Using list comprehension:")
print("1. Create a list of all numbers from 1 to 100 that are divisible by both 3 and 5")
print("2. Create a list of tuples containing numbers and their squares for numbers 1 to 10")
print("3. Create a list of all vowels from a given string")

# ===== 9. String Manipulation =====
# Python provides powerful string manipulation capabilities.

# Examples
print("\nExamples:")
text = "  Hello, World!  "
print("Original:", text)
print("Strip:", text.strip())
print("Lowercase:", text.lower())
print("Uppercase:", text.upper())
print("Replace:", text.replace("World", "Python"))

name = "Alice"
age = 25
print(f"{name} is {age} years old")

words = "Python is awesome".split()
print("Split words:", words)
print("Joined with dashes:", "-".join(words))

# Practice Question 9
print("\nPractice Question 9:")
print("Write a program that:")
print("1. Takes a sentence as input")
print("2. Counts the number of words")
print("3. Reverses each word")
print("4. Joins the reversed words back into a sentence")
print("5. Prints both the original and modified sentences")

# ===== 10. Exception Handling =====
# Exception handling helps manage errors gracefully in Python.

# Examples
print("\nExamples:")
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(f"10 divided by {number} is {result}")
except ValueError:
    print("Please enter a valid number")
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("This will always execute")

# Practice Question 10
print("\nPractice Question 10:")
print("Create a program that:")
print("1. Takes a list of numbers as input")
print("2. Calculates the average of the numbers")
print("3. Handles potential errors (empty list, non-numeric values)")
print("4. Uses try-except-finally blocks appropriately")

# ===== 11. File I/O =====
# Python provides easy ways to read from and write to files.

# Examples
print("\nExamples:")
with open("example.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a test file.")

with open("example.txt", "r") as file:
    content = file.read()
    print("File content:")
    print(content)

with open("example.txt", "r") as file:
    print("\nReading line by line:")
    for line in file:
        print(line.strip())

# Practice Question 11
print("\nPractice Question 11:")
print("Create a program that:")
print("1. Creates a file with student records (name, grade)")
print("2. Reads the file and calculates the average grade")
print("3. Writes the results to a new file")
print("4. Handles potential file I/O errors")

# ===== 12. Modules =====
# Modules help organize Python code into reusable components.

# Examples
print("\nExamples:")
import math
import random
from datetime import datetime

print("Pi:", math.pi)
print("Square root of 16:", math.sqrt(16))

print("Random number:", random.randint(1, 10))
print("Random choice:", random.choice(["apple", "banana", "cherry"]))

now = datetime.now()
print("Current time:", now.strftime("%Y-%m-%d %H:%M:%S"))

# Practice Question 12
print("\nPractice Question 12:")
print("Create a program that:")
print("1. Uses the `random` module to generate a list of random numbers")
print("2. Uses the `math` module to calculate statistics (mean, standard deviation)")
print("3. Uses the `datetime` module to track when the calculations were performed")

# ===== 13. Classes and Objects =====
# Classes are blueprints for creating objects with attributes and methods.

# Examples
print("\nExamples:")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
    
    def have_birthday(self):
        self.age += 1
        return f"Happy birthday! {self.name} is now {self.age} years old."

person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

print(person1.greet())
print(person2.greet())
print(person1.have_birthday())

# Practice Question 13
print("\nPractice Question 13:")
print("Create a `BankAccount` class that:")
print("1. Has attributes for account number, balance, and owner name")
print("2. Has methods for deposit, withdraw, and check balance")
print("3. Includes proper validation (e.g., can't withdraw more than balance)")
print("4. Creates multiple accounts and demonstrates the methods")

# ===== 14. Decorators =====
# Decorators are a way to modify functions using other functions.

# Examples
print("\nExamples:")
import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time:.2f} seconds to execute")
        return result
    return wrapper

@timer_decorator
def slow_function():
    time.sleep(1)
    return "Function completed"

print(slow_function())

# Practice Question 14
print("\nPractice Question 14:")
print("Create a decorator that:")
print("1. Logs function calls with their arguments")
print("2. Caches function results to avoid redundant calculations")
print("3. Applies the decorator to a function that calculates Fibonacci numbers")

# ===== 15. Lambda Functions =====
# Lambda functions are small anonymous functions defined with the lambda keyword.

# Examples
print("\nExamples:")
square = lambda x: x**2
print("Square of 5:", square(5))

multiply = lambda x, y: x * y
print("5 * 3:", multiply(5, 3))

numbers = [1, 5, 3, 9, 2]
sorted_numbers = sorted(numbers, key=lambda x: x)
print("Sorted numbers:", sorted_numbers)

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)

# Practice Question 15
print("\nPractice Question 15:")
print("Create a program that:")
print("1. Uses lambda functions to sort a list of tuples by different criteria")
print("2. Uses lambda with map to transform a list of numbers")
print("3. Uses lambda with filter to extract specific elements from a list")

# ===== 16. Virtual Environments and Packages =====
# Virtual environments help manage project dependencies, and pip is the package installer for Python.

# Examples
print("\nExamples:")
try:
    import numpy as np
    
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])
    
    print("Array addition:", arr1 + arr2)
    print("Array multiplication:", arr1 * arr2)
    print("Array mean:", np.mean(arr1))
except ImportError:
    print("NumPy is not installed. Please install it using: pip install numpy")

# Practice Question 16
print("\nPractice Question 16:")
print("Create a program that:")
print("1. Sets up a virtual environment")
print("2. Installs required packages (e.g., numpy, pandas)")
print("3. Creates a requirements.txt file")
print("4. Demonstrates the use of installed packages") 