#implement stack using fixed array

class Stack:
    def __init__(self, capacity):
        self.capacity = capacity  # Maximum size of the stack
        self.stack = [None] * capacity  # Fixed-size array
        self.top = -1  # Points to the top of the stack

    def push(self, item):
        if self.top == self.capacity - 1:
            raise OverflowError("Stack overflow: Cannot push to a full stack")
        self.top += 1
        self.stack[self.top] = item  
        
    def pop(self):
        if self.top == -1:
            raise IndexError("Stack underflow: Cannot pop from an empty stack")
        item = self.stack[self.top]
        self.stack[self.top] = None  # Clear the slot (optional)
        self.top -= 1
        return item
    
    def peek(self):
        if self.top == -1:
            raise IndexError("Cannot peek: Stack is empty")
        
        return self.stack[self.top]             
            
            
            
s=Stack(4)
s.push(10)   
s.push(12)
s.push(13)
s.pop()
s.peek()
