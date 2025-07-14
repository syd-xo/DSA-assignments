# This program checks if a given string is a palindrome using stack and queue data structures.
# It reads a string, pushes each character onto a stack and enqueues it into a queue,
# then compares characters popped from the stack and dequeued from the queue.
# If they match for the entire string, it confirms that the string is a palindrome.
# It prints the result accordingly. 
class Solution:
    def __init__(self):
        self.stack = []
        self.queue = []

    def pushCharacter(self, char):
        self.stack.append(char)

    def enqueueCharacter(self, char):
        self.queue.append(char)

    def popCharacter(self):
        return self.stack.pop()

    def dequeueCharacter(self):
        return self.queue.pop(0)

# Read the input string
s = input().strip()
obj = Solution()

# Fill stack and queue
for char in s:
    obj.pushCharacter(char)
    obj.enqueueCharacter(char)

# Check for palindrome
is_palindrome = True
for i in range(len(s) // 2):
    if obj.popCharacter() != obj.dequeueCharacter():
        is_palindrome = False
        break

# Print result
if is_palindrome:
    print(f"The word, {s}, is a palindrome.")
else:
    print(f"The word, {s}, is not a palindrome.")
