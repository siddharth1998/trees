from tree_nodes import Nodes

class solution(object):
    def preOrder(self,root):
        #root, left , right
        if root==None:
            return
        print(root.data)
        self.preOrder(root.left)
        self.preOrder(root.right)
    
    def inOrder(self,root):
        # left, root, right
        if root==None:
            return 
        self.inOrder(root.left)
        print(root.data)
        self.inOrder(root.right)

    def postOrder(self,root):
        if root==None:
            return 
        self.postOrder(root.left)
        self.postOrder(root.right)
        print(root.data)


tree=Nodes(data=1,left=Nodes(data=2,left=Nodes(data=4),right=Nodes(data=5)),right=Nodes(data=3))
x=solution()

print("\n This is preOrder ")
x.preOrder(tree)
print("\n this is InOrder ")
x.inOrder(tree)
print("\n this is PostOrder ")
x.postOrder(tree)