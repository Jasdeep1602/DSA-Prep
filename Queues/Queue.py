#implement queue using array

class QueueUsingArray:
    def __init__(self, capacity):
        """Initialize the queue with a fixed capacity."""
        self.queue = [None] * capacity  # Fixed-size array
        self.capacity = capacity
        self.front = 0
        self.rear = -1
        self.size = 0

    def enqueue(self, item):
        """Add an item to the end of the queue."""
        if self.size == self.capacity:
            raise OverflowError("Queue is full")
        # Circular increment of rear pointer
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        self.size += 1

    def dequeue(self):
        """Remove and return the front item from the queue."""
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        item = self.queue[self.front]
        # Move the front pointer forward
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item

    def front_item(self):
        """Return the front item without removing it."""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.queue[self.front]

    def is_empty(self):
        """Check if the queue is empty."""
        return self.size == 0

    def is_full(self):
        """Check if the queue is full."""
        return self.size == self.capacity

    def get_size(self):
        """Return the number of items in the queue."""
        return self.size

# Example usage
queue = QueueUsingArray(5)  # Queue with capacity of 5
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print("Front item:", queue.front_item())  # Output: Front item: 10
print("Dequeue:", queue.dequeue())        # Output: Dequeue: 10
print("Queue size:", queue.get_size())    # Output: Queue size: 2
print("Is empty:", queue.is_empty())      # Output: Is empty: False

queue.enqueue(40)
queue.enqueue(50)
queue.enqueue(60)  # Raises OverflowError if the queue is full


#implement queue using linked list


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self, item):
        """Add an item to the end of the queue."""
        new_node = Node(item)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

    def dequeue(self):
        """Remove and return the front item from the queue."""
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        value = self.front.value
        self.front = self.front.next
        if self.front is None:  # If the queue becomes empty
            self.rear = None
        self.size -= 1
        return value

    def front_item(self):
        """Return the front item without removing it."""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.front.value

    def is_empty(self):
        """Check if the queue is empty."""
        return self.front is None

    def get_size(self):
        """Return the number of items in the queue."""
        return self.size
    
    

#implement queue using 2 Stacks


class QueueUsingTwoStacks:
    def __init__(self):
        self.stack1 = []  # Stack used for enqueue
        self.stack2 = []  # Stack used for dequeue

    def enqueue(self, item):
        """Add an item to the end of the queue."""
        self.stack1.append(item)

    def dequeue(self):
        """Remove and return the front item from the queue."""
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        if not self.stack2:  # If stack2 is empty, transfer elements from stack1
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def front(self):
        """Return the front item without removing it."""
        if self.is_empty():
            raise IndexError("Queue is empty")
        if not self.stack2:  # If stack2 is empty, transfer elements from stack1
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def is_empty(self):
        """Check if the queue is empty."""
        return not self.stack1 and not self.stack2

    def size(self):
        """Return the number of items in the queue."""
        return len(self.stack1) + len(self.stack2)

    
    