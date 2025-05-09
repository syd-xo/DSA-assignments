def reverse_string(s):
    if len(s) <= 1: #base case
        return s
    return reverse_string(s[1:]) + s[0] #recursive case

print(reverse_string("hello"))
print(reverse_string("world"))