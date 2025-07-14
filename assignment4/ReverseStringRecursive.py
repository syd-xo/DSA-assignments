# This program reverses a string using recursion.
# The base case is when the string is empty, returning the empty string.
# Otherwise, it recursively calls itself with the substring excluding the first character,
# and appends the first character to the end of the result.
# It prints the reversed string.
def reverse_string(s):
    if s == "":
        return s
    else:
        return reverse_string(s[1:]) + s[0]

original = "hello"
reversed_string = reverse_string(original)
print("Reversed string:", reversed_string)
