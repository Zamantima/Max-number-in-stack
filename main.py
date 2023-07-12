from stack import Stack
myStack = Stack()
from random import randint
for num in range(0,10):
    randnum = randint(0,10)
    myStack.push(randnum)

print(f"My Main stack: {myStack.display_main_stack()}")
print(f"My Max stack: {myStack.display_max_stack()}")
print(f"The max value is: {myStack.peek()}")

