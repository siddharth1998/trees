class Node():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def insert(root,new_data):
    tempNode=Node(new_data)
    if root==None:
        return tempNode

    if new_data < root.data:
        root.left= insert(root.left,new_data) 
    else:
        root.right=insert(root.right,new_data)

    return root

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.data, end=' ')
        inorder_traversal(root.right)

root = None
keys = [50, 30, 70, 20, 40, 60, 80]

for key in keys:
    
    root = insert(root, key)

# Print the inorder traversal of the BST to check if insertion worked correctly
inorder_traversal(root)