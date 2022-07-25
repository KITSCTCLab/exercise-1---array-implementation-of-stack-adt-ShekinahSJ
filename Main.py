import os
class Stack:
    def __init__(self, size):
        """self.items is the stack
           self.size is the max size of the stack which is an input from the user"""
        self.items = []
        self.size = size

    def is_empty(self):
        """If the stack is empty then its length is 0"""
        if len(self.items)==0:
            return True
        else:
            return False

    def is_full(self):
        """If the stack is full then its length is as much as the max size given by the user"""
        if len(self.items)==self.size:
            return True
        else:
            return False

    def push(self, data):
        """First, check if the stack is full before trying to push, to avoid overflow"""
        if not self.is_full():
            self.items.append(data)

    def pop(self):
        """First, check if the stack is empty before trying to pop, to avoid underflow"""
        if not self.is_empty():
            self.items.pop()

    def status(self):
        """displaying each element in the stack"""
        for i in self.items():
            print(i)

# Do not change the following code
size, queries = map(int, input().rstrip().split())
stack = Stack(size)
for line in range(queries):
    values = list(map(int, input().rstrip().split()))
    if values[0] == 1:
        stack.push(values[1])
    elif values[0] == 2:
        stack.pop()
stack.status()
