#Create a node

class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        
# head=Node(5)
# print(head.value)   

#Insertion at beginning    

class LinkedList:
    def __init__(self):
        self.head=None
        
    def insertFront(self,value):
        print("Inserting value:",value)
        
        # Step 1: Create a new Node
        newNode=Node(value)
        
        # Step 2: Set next of new_node to the current head
        newNode.next=self.head
        
        # Step 3: Set new_node as the head
        self.head=newNode
        
    def getHeadValue(self):
        if self.head is None:
            return -1
        else:
            return self.head.value    
        
            
        
# Create an instance of LinkedList
list=LinkedList()
list.insertFront(4)
print("get head value:",list.getHeadValue())   

list.insertFront(7)
print("get head value:",list.getHeadValue())   
 
list.insertFront(7)
print("get head value:",list.getHeadValue())   

list1=LinkedList()
list1.insertFront(2)
print('Get head',list1.getHeadValue())
       