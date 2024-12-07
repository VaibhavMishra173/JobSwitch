# s = []
# s.append('https://www.cnn.com/')
# s.append('https://www.cnn.com/world')
# s.append('https://www.cnn.com/india')
# s.append('https://www.cnn.com/china')

# s.pop()
# s.pop()
# s[-1]

# Using Deque
from collections import deque
# stack = deque()

# # dir(stack)

# stack.append("https://www.cnn.com/")
# print(stack)

# stack.append("https://www.cnn.com/world")
# print(stack)

# stack.append("https://www.cnn.com/india")
# stack.append("https://www.cnn.com/china")
# print(stack)

# stack.pop()
# stack.pop()
# print(stack)


# Using Class

class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self,val):
        self.container.append(val)
        
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return  self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)
    
s = Stack()
s.push(5)
s.is_empty()
s.pop()
s.is_empty()
s.push(9)
s.push(34)
s.push(78)
s.push(12)
s.peek()
s.pop()
s.pop()
s.pop()
s.pop()

 

