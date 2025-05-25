from collections import deque

class TreeNode:
    def __init__(self, val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
    def __str__(self):
        return str(self.val)
    
    
    def preorder(self,node):
        if not node:
            return
        
        print(node)
        self.preorder(node.left)
        self.preorder(node.right)
        
    def inorder(self,node):
        if not node:
            return
        
        self.inorder(node.left)
        print(node)
        self.inorder(node.right)
        
    def postorder(self,node):
        if not node:
            return
        
        self.postorder(node.left)
        self.postorder(node.right)
        print(node)
        
    def iterative_preorder(self,node):
        if not node:
            return
        
        stack=[]
        stack.append(node)
        
        while stack:
            node=stack.pop()
            print(node)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
                
    def levelorder(self,node):
        if not node:
            return
        
        queue=deque()
        queue.append(node)
        
        while queue:
            node=queue.popleft()
            print(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                

    def maxHeight(self,node):
        if not node:
            return 0

        left=self.maxHeight(node.left) 
        right=self.maxHeight(node.right)

        return 1 + max(left, right)
            
    # Zigzag Level Order Traversal
    # get the level of the tree and array of each level            
                
    def zigzagLevelOrder(self, node):
        if not node:
            return []
            
        queue=deque([node])
        arr=[]
        level=0

        while queue:
            length=len(queue)
            inner=[]
            for _ in range(length):
                node=queue.popleft()
                inner.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            level+=1
        
            if level%2==0:
                inner.reverse()        
                    
            arr.append(inner)
        print(arr,level)
                

A=TreeNode(1)
B=TreeNode(2)
C=TreeNode(3)
D=TreeNode(4)
E=TreeNode(5)
F=TreeNode(10)
A.left=B
A.right=C
B.left=D
B.right=E
C.left=F

A.iterative_preorder(A)


