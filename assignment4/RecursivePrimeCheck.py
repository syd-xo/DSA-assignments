# This program checks if a number is prime using recursion.
# It handles numbers less than 2 as non-prime and uses a recursive function to check divisibility.
# The base case is when the divisor reaches 1, confirming the number is prime if no divisors were found.
# It prints whether the number is prime or not.
def is_prime(n, divisor= None):
    if n < 2:
        return False
    if divisor is None:
        divisor = n - 1
    if divisor == 1:
        return True
    if n % divisor == 0:
        return False
    return is_prime(n, divisor - 1)

print(is_prime(21))
print(is_prime(7))
print(is_prime(11))