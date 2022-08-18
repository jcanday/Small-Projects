from collections import deque
from this import d


class Node:
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right
    
    def __str__(self) -> str:
        return "Node(" + str(self.value) + ")"
    
#recursive dfs
#preorder
def walk(tree):
    if tree is not None:
        print(tree)
        walk(tree.left)
        walk(tree.right)
        
#inorder
def walk2(tree):
    if tree is not None:
        walk2(tree.left)
        print(tree)
        walk2(tree.right)
        
#postorder
def walk3(tree):
    if tree is not None:
        walk3(tree.left)
        walk3(tree.right)
        print(tree)
        
#iterative
def walk4(tree,stack=[]):
    stack.append(tree)
    while len(stack) > 0:
        node = stack.pop()
        if node is not None:
            print(node)
            stack.append(node.right)
            stack.append(node.left)
            
mytree = Node('A', Node('B',Node('D'),Node('E')),Node('C',Node('F'),Node('G')))


walk3(mytree)

#Binary Tree Depth
#recursive DFS
def maxDepth(self, root: Node) -> int:
    if not root:
        return 0
    return 1+ max(maxDepth(root.left),maxDepth(root.right))

#iterative BFS
def maxDepth1(self, root: Node) -> int:
    if not root:
        return 0
    
    level = 1
    q = deque([root])
    while q:
        for i in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        level += 1
        
    return level
        
def maxDepth2(self, root: Node) -> int:
    stack= [[root,1]]
    res = 0
    
    while stack:
        node,depth = stack.pop()
        
        if node:
            res = max(res, depth)
            stack.append([node.left],depth+1)
            stack.append([node.right],depth+1)
    
    return res