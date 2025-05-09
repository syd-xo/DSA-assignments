def recursive_multiply(a, b):
    if b == 0: #base case
        return 0
    if b < 0: #handle negative numbers
        return -recursive_multiply(a, -b)
    return a + recursive_multiply(a, b-1)

print(recursive_multiply(1, 2))
print(recursive_multiply(3, 4))
print(recursive_multiply(-2, 10))


