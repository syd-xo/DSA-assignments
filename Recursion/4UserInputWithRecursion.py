def countdown(n):
   if n >= 1:
       print(n)
       countdown(n-1)

# Input validation
while True:
    try:
        n = int(input('Enter a positive number to count down from: '))
        if n > 0:
            break
        else:
            print('Enter a number greater than or equal to 0.')
    except ValueError:
        print('Invalid input. Enter a valid integer.')

#Recursion
countdown(n)

#Another way to write it
#