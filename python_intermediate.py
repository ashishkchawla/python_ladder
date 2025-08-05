"""
Python Intermediate Learning Script
This script covers intermediate Python concepts with explanations, examples, and practice questions.
"""

# ===== 1. Advanced Functions =====
# Python functions can be more sophisticated with default arguments, keyword arguments, and more.

# Examples
print("\nExamples:")
def greet(name, greeting="Hello", punctuation="!"):
    return f"{greeting}, {name}{punctuation}"

print(greet("Alice"))  # Uses defaults
print(greet("Bob", "Hi", "?"))  # Overrides defaults
print(greet(greeting="Good morning", name="Charlie"))  # Keyword arguments

def flexible_function(*args, **kwargs):
    print(f"Positional arguments: {args}")
    print(f"Keyword arguments: {kwargs}")

flexible_function(1, 2, 3, name="Alice", age=25)

# Practice Question 1
print("\nPractice Question 1:")
print("Create a function that:")
print("1. Takes any number of numbers as positional arguments")
print("2. Takes optional 'operation' and 'round_to' as keyword arguments")
print("3. Performs the specified operation (sum, product, average) on the numbers")
print("4. Rounds the result to the specified number of decimal places")

# ===== 2. *args and **kwargs =====
# *args collects positional arguments into a tuple, **kwargs collects keyword arguments into a dictionary.

# Examples
print("\nExamples:")
def sum_all(*args):
    return sum(args)

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print("Sum of 1, 2, 3, 4:", sum_all(1, 2, 3, 4))
print_info(name="Alice", age=25, city="New York")

def wrapper_function(*args, **kwargs):
    print("Calling function with:")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")
    # This could call another function with the same arguments

# Practice Question 2
print("\nPractice Question 2:")
print("Create a function that:")
print("1. Takes any number of dictionaries as *args")
print("2. Merges all dictionaries into a single dictionary")
print("3. If there are conflicting keys, keeps the value from the last dictionary")
print("4. Returns the merged dictionary")

# ===== 3. Higher-Order Functions =====
# Functions that take other functions as arguments or return functions.

# Examples
print("\nExamples:")
def apply_operation(func, *args):
    return func(*args)

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

print("Square of 5:", apply_operation(square, 5))
print("Cube of 3:", apply_operation(cube, 3))

def create_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier

double = create_multiplier(2)
triple = create_multiplier(3)

print("Double of 5:", double(5))
print("Triple of 4:", triple(4))

# Practice Question 3
print("\nPractice Question 3:")
print("Create a higher-order function that:")
print("1. Takes a function and a list as arguments")
print("2. Applies the function to each element in the list")
print("3. Returns a new list with the results")
print("4. Also create a function that filters elements based on a condition")

# ===== 4. Iterators =====
# Iterators are objects that can be iterated upon, implementing __iter__ and __next__ methods.

# Examples
print("\nExamples:")
class CountDown:
    def __init__(self, start):
        self.start = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start <= 0:
            raise StopIteration
        self.start -= 1
        return self.start + 1

print("Countdown from 5:")
for num in CountDown(5):
    print(num, end=" ")
print()

# Built-in iterators
numbers = [1, 2, 3, 4, 5]
iterator = iter(numbers)
print("First element:", next(iterator))
print("Second element:", next(iterator))

# Practice Question 4
print("\nPractice Question 4:")
print("Create an iterator class that:")
print("1. Generates Fibonacci numbers up to a given limit")
print("2. Implements both __iter__ and __next__ methods")
print("3. Raises StopIteration when the limit is reached")
print("4. Use it in a for loop to print Fibonacci numbers")

# ===== 5. Generators =====
# Generators are functions that use 'yield' to return values one at a time.

# Examples
print("\nExamples:")
def fibonacci_generator(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

print("First 8 Fibonacci numbers:")
for num in fibonacci_generator(8):
    print(num, end=" ")
print()

def infinite_counter():
    num = 0
    while True:
        yield num
        num += 1

counter = infinite_counter()
print("First 5 numbers from infinite counter:")
for _ in range(5):
    print(next(counter), end=" ")
print()

# Generator expressions
squares = (x**2 for x in range(5))
print("Squares from generator expression:", list(squares))

# Practice Question 5
print("\nPractice Question 5:")
print("Create a generator that:")
print("1. Yields prime numbers up to a given limit")
print("2. Uses the Sieve of Eratosthenes algorithm")
print("3. Can be used in a for loop")
print("4. Also create a generator expression for even squares")

# ===== 6. Advanced Comprehensions =====
# Comprehensions with conditions and nested structures.

# Examples
print("\nExamples:")
# List comprehension with condition
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print("Even squares:", even_squares)

# Dictionary comprehension
word_lengths = {word: len(word) for word in ["apple", "banana", "cherry"]}
print("Word lengths:", word_lengths)

# Set comprehension
unique_chars = {char for word in ["hello", "world"] for char in word}
print("Unique characters:", unique_chars)

# Nested list comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print("Flattened matrix:", flattened)

# Practice Question 6
print("\nPractice Question 6:")
print("Using comprehensions:")
print("1. Create a dictionary mapping numbers to their factors")
print("2. Create a set of all vowels from a list of words")
print("3. Create a list of tuples (number, square, cube) for numbers 1-5")
print("4. Create a nested list comprehension for a 3x3 identity matrix")

# ===== 7. Unpacking Operators =====
# * for iterables and ** for dictionaries.

# Examples
print("\nExamples:")
# Unpacking lists
numbers = [1, 2, 3]
print("Unpacked numbers:", *numbers)

# Merging lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged = [*list1, *list2]
print("Merged lists:", merged)

# Unpacking dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged_dict = {**dict1, **dict2}
print("Merged dictionaries:", merged_dict)

# Function arguments
def print_args(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

args_list = [1, 2, 3]
kwargs_dict = {"name": "Alice", "age": 25}
print_args(*args_list, **kwargs_dict)

# Practice Question 7
print("\nPractice Question 7:")
print("Create a function that:")
print("1. Takes any number of lists as arguments")
print("2. Uses unpacking to merge all lists")
print("3. Removes duplicates while preserving order")
print("4. Returns the merged, deduplicated list")

# ===== 8. Type Hinting =====
# Type hints help with code documentation and IDE support.

# Examples
print("\nExamples:")
from typing import List, Dict, Tuple, Optional, Union, Callable

def greet_person(name: str, age: int) -> str:
    return f"Hello {name}, you are {age} years old"

def calculate_average(numbers: List[float]) -> float:
    return sum(numbers) / len(numbers)

def get_user_info(user_id: int) -> Optional[Dict[str, Union[str, int]]]:
    # Simulate database lookup
    if user_id == 1:
        return {"name": "Alice", "age": 25}
    return None

def process_data(data: List[Union[int, str]], 
                processor: Callable[[Union[int, str]], str]) -> List[str]:
    return [processor(item) for item in data]

print(greet_person("Alice", 25))
print(calculate_average([1.5, 2.5, 3.5]))
print(get_user_info(1))

# Practice Question 8
print("\nPractice Question 8:")
print("Create functions with type hints that:")
print("1. Takes a list of numbers and returns their statistics (min, max, avg)")
print("2. Takes a dictionary of user data and validates required fields")
print("3. Takes a function and applies it to each element of a list")
print("4. Uses Optional and Union types appropriately")

# ===== 9. Virtual Environments and pip =====
# Virtual environments isolate project dependencies.

# Examples
print("\nExamples:")
print("Virtual Environment Commands:")
print("# Create virtual environment:")
print("python -m venv myenv")
print("# Activate (Windows):")
print("myenv\\Scripts\\activate")
print("# Activate (macOS/Linux):")
print("source myenv/bin/activate")
print("# Install packages:")
print("pip install package_name")
print("# Create requirements.txt:")
print("pip freeze > requirements.txt")
print("# Install from requirements.txt:")
print("pip install -r requirements.txt")

# Practice Question 9
print("\nPractice Question 9:")
print("Set up a virtual environment and:")
print("1. Install numpy, pandas, and matplotlib")
print("2. Create a requirements.txt file")
print("3. Write a script that uses these packages")
print("4. Deactivate and reactivate the environment")

# ===== 10. Packaging =====
# Creating distributable Python packages.

# Examples
print("\nExamples:")
print("Basic package structure:")
print("my_package/")
print("├── __init__.py")
print("├── module1.py")
print("├── module2.py")
print("├── setup.py")
print("└── README.md")

print("\nsetup.py example:")
print("from setuptools import setup, find_packages")
print("setup(")
print("    name='my_package',")
print("    version='1.0.0',")
print("    packages=find_packages(),")
print("    install_requires=['numpy'],")
print("    author='Your Name',")
print("    description='A sample package'")
print(")")

# Practice Question 10
print("\nPractice Question 10:")
print("Create a simple package that:")
print("1. Has multiple modules with different functions")
print("2. Includes a setup.py file")
print("3. Can be installed with pip install -e .")
print("4. Has proper __init__.py files")

# ===== 11. Closures =====
# Functions that remember values from their enclosing scope.

# Examples
print("\nExamples:")
def outer_function(x):
    def inner_function(y):
        return x + y  # x is captured from outer scope
    return inner_function

add_five = outer_function(5)
print("Add five to 3:", add_five(3))

def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

my_counter = counter()
print("Counter values:", my_counter(), my_counter(), my_counter())

# Practice Question 11
print("\nPractice Question 11:")
print("Create a closure that:")
print("1. Remembers a list of numbers")
print("2. Has an inner function that adds a number to the list")
print("3. Has another inner function that returns the sum of all numbers")
print("4. Demonstrates the closure maintaining state")

# ===== 12. Decorators =====
# Functions that modify other functions.

# Examples
print("\nExamples:")
import time
import functools

def timer_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

def cache_decorator(func):
    cache = {}
    @functools.wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@timer_decorator
@cache_decorator
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print("Fibonacci(10):", fibonacci(10))

# Practice Question 12
print("\nPractice Question 12:")
print("Create decorators that:")
print("1. Logs function calls with arguments and return values")
print("2. Retries a function up to 3 times if it raises an exception")
print("3. Validates function arguments based on type hints")
print("4. Measures memory usage of a function")

# ===== 13. Context Managers =====
# Objects that can be used with the 'with' statement.

# Examples
print("\nExamples:")
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

# Using context manager
with FileManager("test.txt", "w") as f:
    f.write("Hello, World!")

# Using contextlib
from contextlib import contextmanager

@contextmanager
def timer():
    start = time.time()
    yield
    end = time.time()
    print(f"Operation took {end - start:.4f} seconds")

with timer():
    time.sleep(1)

# Practice Question 13
print("\nPractice Question 13:")
print("Create context managers that:")
print("1. Temporarily changes the working directory")
print("2. Suppresses specific exceptions")
print("3. Measures and logs the time taken for operations")
print("4. Manages database connections")

# ===== 14. Regular Expressions =====
# Pattern matching and text processing.

# Examples
print("\nExamples:")
import re

# Basic patterns
text = "My email is alice@example.com and phone is 123-456-7890"
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
phone_pattern = r'\d{3}-\d{3}-\d{4}'

emails = re.findall(email_pattern, text)
phones = re.findall(phone_pattern, text)

print("Emails found:", emails)
print("Phones found:", phones)

# Substitution
text = "Hello World, hello Python, hello everyone"
new_text = re.sub(r'hello', 'hi', text, flags=re.IGNORECASE)
print("After substitution:", new_text)

# Validation
def is_valid_email(email):
    pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$'
    return bool(re.match(pattern, email))

print("Valid email?", is_valid_email("alice@example.com"))
print("Valid email?", is_valid_email("invalid-email"))

# Practice Question 14
print("\nPractice Question 14:")
print("Create regex patterns that:")
print("1. Validates phone numbers in different formats")
print("2. Extracts dates in MM/DD/YYYY format")
print("3. Finds all words that start with a capital letter")
print("4. Validates password strength (8+ chars, uppercase, lowercase, digit)")

# ===== 15. Testing (pytest, unittest) =====
# Writing and running tests for your code.

# Examples
print("\nExamples:")
import unittest

class MathOperations:
    def add(self, a, b):
        return a + b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

class TestMathOperations(unittest.TestCase):
    def setUp(self):
        self.math = MathOperations()
    
    def test_add(self):
        self.assertEqual(self.math.add(2, 3), 5)
        self.assertEqual(self.math.add(-1, 1), 0)
    
    def test_multiply(self):
        self.assertEqual(self.math.multiply(2, 3), 6)
        self.assertEqual(self.math.multiply(0, 5), 0)
    
    def test_divide(self):
        self.assertEqual(self.math.divide(6, 2), 3)
        self.assertEqual(self.math.divide(5, 2), 2.5)
    
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.math.divide(5, 0)

# Pytest example (would be in a separate file)
print("\nPytest example (test_math.py):")
print("import pytest")
print("from math_operations import MathOperations")
print("")
print("@pytest.fixture")
print("def math_ops():")
print("    return MathOperations()")
print("")
print("def test_add(math_ops):")
print("    assert math_ops.add(2, 3) == 5")
print("")
print("def test_divide_by_zero(math_ops):")
print("    with pytest.raises(ValueError):")
print("        math_ops.divide(5, 0)")

# Practice Question 15
print("\nPractice Question 15:")
print("Create comprehensive tests for:")
print("1. A Calculator class with basic operations")
print("2. A StringProcessor class with text manipulation methods")
print("3. A BankAccount class with deposit/withdraw operations")
print("4. Use both unittest and pytest frameworks")

# ===== 16. Logging =====
# Proper logging for debugging and monitoring.

# Examples
print("\nExamples:")
import logging

# Basic logging setup
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

def process_data(data):
    logger.info(f"Processing {len(data)} items")
    
    try:
        result = sum(data)
        logger.info(f"Processing completed successfully. Sum: {result}")
        return result
    except Exception as e:
        logger.error(f"Error processing data: {e}")
        raise

# Custom logger
class CustomLogger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        
        # Create handlers
        file_handler = logging.FileHandler(f'{name}.log')
        console_handler = logging.StreamHandler()
        
        # Create formatters
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        
        # Add handlers
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)
    
    def info(self, message):
        self.logger.info(message)
    
    def error(self, message):
        self.logger.error(message)
    
    def debug(self, message):
        self.logger.debug(message)

# Practice Question 16
print("\nPractice Question 16:")
print("Create a logging system that:")
print("1. Logs different levels (DEBUG, INFO, WARNING, ERROR)")
print("2. Writes to both file and console")
print("3. Includes timestamps and log levels")
print("4. Creates a custom logger class for your application")

# ===== 17. Advanced Data Structures =====
# Collections module and custom data structures.

# Examples
print("\nExamples:")
from collections import defaultdict, Counter, namedtuple, deque

# DefaultDict
word_count = defaultdict(int)
words = ["apple", "banana", "apple", "cherry", "banana"]
for word in words:
    word_count[word] += 1
print("Word count:", dict(word_count))

# Counter
letter_count = Counter("hello world")
print("Letter count:", letter_count)
print("Most common:", letter_count.most_common(3))

# NamedTuple
Person = namedtuple('Person', ['name', 'age', 'city'])
person = Person('Alice', 25, 'New York')
print("Person:", person)
print("Name:", person.name)

# Deque
queue = deque([1, 2, 3])
queue.append(4)
queue.appendleft(0)
print("Queue:", queue)
print("Popped from left:", queue.popleft())

# Practice Question 17
print("\nPractice Question 17:")
print("Create data structures that:")
print("1. Use defaultdict to group items by category")
print("2. Use Counter to analyze text frequency")
print("3. Use namedtuple for structured data")
print("4. Use deque for efficient queue operations")

# ===== 18. Functional Programming =====
# Using functional programming concepts in Python.

# Examples
print("\nExamples:")
from functools import reduce, partial

# Map, filter, reduce
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Map
squares = list(map(lambda x: x**2, numbers))
print("Squares:", squares)

# Filter
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", evens)

# Reduce
sum_all = reduce(lambda x, y: x + y, numbers)
print("Sum of all numbers:", sum_all)

# Partial functions
def greet(greeting, name):
    return f"{greeting}, {name}!"

hello_greet = partial(greet, "Hello")
good_morning_greet = partial(greet, "Good morning")

print(hello_greet("Alice"))
print(good_morning_greet("Bob"))

# Practice Question 18
print("\nPractice Question 18:")
print("Create functional programming solutions that:")
print("1. Use map to transform a list of strings")
print("2. Use filter to extract specific data")
print("3. Use reduce to perform complex calculations")
print("4. Use partial to create specialized functions")

# ===== 19. Metaclasses =====
# Classes that create other classes.

# Examples
print("\nExamples:")
class MetaLogger(type):
    def __new__(cls, name, bases, attrs):
        # Add logging to all methods
        for key, value in attrs.items():
            if callable(value) and not key.startswith('__'):
                attrs[key] = cls.add_logging(value)
        return super().__new__(cls, name, bases, attrs)
    
    @staticmethod
    def add_logging(func):
        def wrapper(*args, **kwargs):
            print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
            result = func(*args, **kwargs)
            print(f"{func.__name__} returned: {result}")
            return result
        return wrapper

class Calculator(metaclass=MetaLogger):
    def add(self, a, b):
        return a + b
    
    def multiply(self, a, b):
        return a * b

calc = Calculator()
print("Calculator with logging:")
calc.add(2, 3)
calc.multiply(4, 5)

# Practice Question 19
print("\nPractice Question 19:")
print("Create metaclasses that:")
print("1. Automatically add validation to class attributes")
print("2. Create singleton classes")
print("3. Add timing decorators to all methods")
print("4. Implement a registry pattern for classes")

# ===== 20. Async Programming =====
# Asynchronous programming with asyncio.

# Examples
print("\nExamples:")
import asyncio

# Simple async function
async def count_up():
    for i in range(5):
        print(f"Count: {i}")
        await asyncio.sleep(1)

# Async function with aiohttp (commented out as it requires installation)
print("Async programming example (requires aiohttp):")
print("async def fetch_data(url):")
print("    async with aiohttp.ClientSession() as session:")
print("        async with session.get(url) as response:")
print("            return await response.text()")

# Practice Question 20
print("\nPractice Question 20:")
print("Create async programs that:")
print("1. Fetch data from multiple URLs concurrently")
print("2. Process a queue of tasks asynchronously")
print("3. Implement a simple async web server")
print("4. Use asyncio for I/O-bound operations")

print("\n" + "="*50)
print("Intermediate Python Concepts Complete!")
print("Practice these concepts to strengthen your Python skills.")
print("="*50) 