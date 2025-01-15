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



#implement stack using Linked List

class Node:
    """A node in the linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer to the next node


class Stack:
    """Stack implementation using a linked list."""
    def __init__(self):
        self.top = None  # Pointer to the top of the stack
        self.size = 0    # Track the size of the stack

    def push(self, item):
        """Add an item to the top of the stack."""
        new_node = Node(item)
        new_node.next = self.top  # Link the new node to the current top
        self.top = new_node       # Update the top to the new node
        self.size += 1

    def pop(self):
        """Remove and return the top item from the stack."""
        if self.top == None:
            raise IndexError("Pop from an empty stack")
        data = self.top.data
        self.top = self.top.next  # Move the top pointer to the next node
        self.size -= 1
        return data

    def peek(self):
        """Return the top item of the stack without removing it."""
        if self.top == None:
            raise IndexError("Peek from an empty stack")
        return self.top.data




#implement stack using 2 Queues


class StackUsingQueues:
    def __init__(self):
        # Initialize two queues as empty lists
        self.queue1 = []  # Primary queue
        self.queue2 = []  # Temporary queue for operations

    def push(self, item):
        # Add the new item to queue2
        self.queue2.append(item)

        # Move all elements from queue1 to queue2 to maintain stack order
        while self.queue1:
            self.queue2.append(self.queue1.pop(0))  # Dequeue from queue1 and enqueue to queue2

        # Swap queue1 and queue2
        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self):
        # Remove and return the top item (front of queue1)
        if not self.queue1:
            return None  # If stack is empty
        return self.queue1.pop(0)

    def top(self):
        # Return the top item without removing it
        if not self.queue1:
            return None  # If stack is empty
        return self.queue1[0]

    def is_empty(self):
        # Check if the stack is empty
        return len(self.queue1) == 0
