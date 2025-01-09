#Create a node

class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        
# head=Node(5)
# print(head.value)   

class LinkedList:
    def __init__(self):
        self.head=None

#Insertion at beginning        
    def insertFront(self,value):
        print("Inserting value:",value)
        
        # Step 1: Create a new Node
        newNode=Node(value)
        
        # Step 2: Set next of new_node to the current head
        newNode.next=self.head
        
        # Step 3: Set new_node as the head
        self.head=newNode

#Insertion at end        
    def insertEnd(self,value):
        print("Inserting at end value:",value)
        newNode=Node(value)

        if not self.head:
            self.head=newNode
            return
        current=self.head
        while current.next:
            current=current.next
        current.next=newNode
        

#Insertion at Kth position        
    def insertAtPos(self,value,k):
        print("Inserting at postion:",value)
        newNode=Node(value)
        
        # Case 1: Insert at head if k == 0
        if k == 0:
            newNode.next = self.head
            self.head = newNode
            return

        # Traverse to (k-1)-th position
        current = self.head
        pos = 0
        while current and pos < k-1 :
            current=current.next
            pos+=1  
            
        # Case 2: If current is None, k is out of bounds
        if not current:
            print("Position out of bounds")
            return  
        newNode.next=current.next    
        current.next=newNode               

#Get head value        
    def getHeadValue(self):
        if self.head is None:
            return -1
        else:
            return self.head.value 
        
#Traverse           
    def printList(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")  # Indicate the end of the list
        
        
# Create an instance of LinkedList
list=LinkedList()
list.insertFront(4)
print("get head value:",list.getHeadValue())  
 
list.insertFront(7)
print("get head value:",list.getHeadValue()) 

list.insertEnd(8)

list.insertAtPos(9,3)

list.printList()
#Insertion at end    
 

