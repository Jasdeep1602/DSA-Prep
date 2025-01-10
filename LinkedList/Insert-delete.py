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
        
#Deletion at beginning        
    def deleteFront(self):
        if not self.head:
            return
        
        #preserve head value
        current=self.head
        
        #check if LL doest onlt have 1 node
        if current.next:
            self.head=current.next

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
        
        
#Deletion at end  
    def deleteEnd(self):
        if not self.head:
            return
        # If there's only one node
        if not self.head.next:  
            self.head = None
            return 
        
        current=self.head
        while current.next and current.next.next:
            current=current.next
        
        current.next=None
        
            

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
        
        
#Deletion at Kth position        
    def deleteAtPos(self,k):
        # Case 1: Delete at head if k == 1
        if k == 1:
            self.head = self.head.next
            return
        
        # Traverse to (k-1)-th position
        current = self.head
        pos=1
        while current and pos<k-1:
            current=current.next
            pos+=1
             
        # Case 2: If current is None, k is out of bounds
        if not current or not current.next:  
            print("Position out of bounds")
            return
        
        current.next=current.next.next

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


# list.deleteFront()
# print("get head value:",list.getHeadValue()) 

# list.deleteEnd()
list.deleteAtPos(3)

list.printList()
 

