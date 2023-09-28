from tree_nodes import Nodes

class Solution:
    def levelOrder(self, root):
        queue=[]
        tempQueue=[]
        tempList=[] # for purpose of storing nodes in same level and appending in queue this will be emptied after interation
        if not root:
            return []
        present_val=root
        tempQueue.append(present_val)
        tempQueue.append(None)# This is a delimeter for different levels
        while len(tempQueue)>1:
            present_val=tempQueue.pop(0)
           

            if present_val==None:
                tempQueue.append(None)# This is a kind of delimeter
                queue.append(tempList)
                
                tempList=[]
            else:
                if present_val.left:
                    lchild=present_val.left
                    tempQueue.append(lchild)
                if present_val.right:
                    rchild=present_val.right
                    tempQueue.append(rchild)
                tempList.append(present_val.data)
        queue.append(tempList)
        return queue
    
x=Solution()
tree=Nodes(data=1,left=Nodes(data=2,left=Nodes(data=4),right=Nodes(data=5)),right=Nodes(data=3))

y=x.levelOrder(tree)
for i in y:
    for z in i:
        print(z, end=" ")
    print()