#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Decrement n in each iteration
    return result

if len(sys.argv) != 2:
    print("Usage: ./factorial.py <number>")
    sys.exit(1)

try:
    number = int(sys.argv[1])
except ValueError:
    print("Please provide a valid integer.")
    sys.exit(1)

if number < 0:
    print("Factorial is not defined for negative numbers.")
    sys.exit(1)

f = factorial(number)
print(f)
