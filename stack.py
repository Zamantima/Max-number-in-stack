class Stack:
    def __init__(self):
        self.stack = []
        self.maxStack = []

    def push(self, data):
        self.stack.append(data)
        if len(self.maxStack) < 1:
            self.maxStack.append(data)
        elif self.maxStack[-1] <= data:
            self.maxStack.append(data)

    def pop(self):
        if len(self.stack) < 1:
            return
        data = self.stack[0]
        del self.stack[0]
        if self.stack[0] == self.maxStack[-1]:
            del self.maxStack[-1]
        self.maxStack = [max(self.stack)]


    def peek(self):
        return self.maxStack[-1]

    def display_main_stack(self):
        return self.stack

    def display_max_stack(self):
        return self.maxStack
