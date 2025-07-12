# Python program that counts down numbers from n to 1 using recursion method
# A recursive function-> a function that calls itself (use if- else)
def countdown(n):
    if n >= 1:
        print(n)
        countdown(n - 1)
countdown (10)


###Another way to write it
# def countdown(n):
#     print(n)
# if n == 1:
#     return n
# else:
#     countdown(n - 1)