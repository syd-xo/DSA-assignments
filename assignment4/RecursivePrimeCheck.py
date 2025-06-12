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