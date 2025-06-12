def reverse_string(s):
    if s == "":
        return s
    else:
        return reverse_string(s[1:]) + s[0]

original = "hello"
reversed_string = reverse_string(original)
print("Reversed string:", reversed_string)
