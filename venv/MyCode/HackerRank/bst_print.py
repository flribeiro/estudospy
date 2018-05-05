import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data

class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        queue = [root] if root else []
        for n in queue:
            print('\nnode: {}'.format(n.data))

        while queue:
            node = queue.pop()
            print(node.data, end=" ")

            if node.left: queue.insert(0,node.left)
            if node.right: queue.insert(0,node.right)
            for i,n in enumerate(queue):
                print('\nnode {}: {}'.format(i, n.data))


T=int(input())
# T = 6
myTree=Solution()
inputarray=[3,5,4,7,2,1]
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
# for i in inputarray:
#     root=myTree.insert(root,i)
myTree.levelOrder(root)
