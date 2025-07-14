# Recursive Multiplication
# This program performs multiplication of two numbers using recursion.
# It handles both positive and negative integers, and the base case is when the second number is zero.
# The function recursively adds the first number to itself, reducing the second number until it reaches zero.
def recursive_multiply(a, b):
    if b == 0: #base case
        return 0
    if b < 0: #handle negative numbers
        return -recursive_multiply(a, -b)
    return a + recursive_multiply(a, b-1)

print(recursive_multiply(1, 2))
print(recursive_multiply(3, 4))
print(recursive_multiply(-2, 10))


