# practice_03_loops.py
"""
Loop Practice
"""

# Exercise 1: Print Pattern
print("=== Exercise 1: Triangle Pattern ===")
def print_triangle(n):
    for i in range(1, n + 1):
        print('*' * i)

print_triangle(5)

# Exercise 2: Multiplication Table
print("\n=== Exercise 2: Multiplication Table ===")
def multiplication_table(n):
    print(f"Multiplication Table for {n}:")
    for i in range(1, 11):
        print(f"{n} × {i:2} = {n * i:3}")

multiplication_table(7)

# Exercise 3: Sum of Numbers
print("\n=== Exercise 3: Sum Calculator ===")
def sum_of_numbers(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

my_numbers = [10, 20, 30, 40, 50]
print(f"Sum of {my_numbers} = {sum_of_numbers(my_numbers)}")
print(f"Sum using built-in sum(): {sum(my_numbers)}")

# Exercise 4: Factorial
print("\n=== Exercise 4: Factorial ===")
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

for i in range(1, 8):
    print(f"{i}! = {factorial(i)}")

# Exercise 5: Fibonacci Sequence
print("\n=== Exercise 5: Fibonacci ===")
def fibonacci(n):
    a, b = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

print(f"First 10 Fibonacci numbers: {fibonacci(10)}")