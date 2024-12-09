# basec TreeNode Class
class TreeNode(object):
    def __init__(self, val = 0, left = None, right = None):
        self.val = val # value sorted in the node
        self.left = left # left child could be None
        self.right = right # right child could be None


# Creating simply binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)


# functions to transfer lis into binary node tree
def CreateBinaryNode(arr):
    if not arr: 
        return None 
    root = TreeNode(arr[0])
    node = [root]
    idx = 1
    while idx < len(arr):
        d = node.pop(0)
        if arr[idx] is not None:
            d.left = TreeNode(arr[idx])
            node.append(d.left)

        idx += 1
        if idx < len(arr) and arr[idx] is not None:
            d.right = TreeNode(arr[idx])
            node.append(d.right)
        idx += 1
    return root 

# => test the createBinaryTree function
L_test = [1,2,3,4,5]
root = CreateBinaryNode(L_test)


# Recursive preorder Trversal(Root, left, right) function
def preorder(node):
    """Preorder traversal with arrows showing the path"""
    if node:
        # Print the node with an arrow if it's part of the preorder path
        print(f"---> {node.val}", end=" ")
        preorder(node.left)  # Traverse left subtree
        preorder(node.right)  # Traverse right subtree
# => test the preorder function
# print('preorder function : \n',preorder(root))


# Recursive Inorder Traversal(left, root, right) function
def inorder(node):
    if node:
        inorder(node.left) # traverse left subtree
        print(f"-> {node.val}", end = " ") # visit the root
        inorder(node.right) # traverse right subtree
# => test the inorder function
# print('inorder function : \n', inorder(root))

# Recursive postorder traversal(left, right, root) function
def postorder(node):
    if node:
        postorder(node.left) # traverse left subtree
        postorder(node.right) # traverse right subtree
        print(f"-> {node.val}", end = " ") # visit the root
# => test the postorder function
# print('postorder function : \n', postorder(root))


# Level-order Traversal (Breadth-first Search) function
from collections import deque

def LevelOrder(node):
    if not node:
        return []
    result = []
    queue = deque([node])
    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result


# => test the LevelOrder function
# print('Level Order function : \n', LevelOrder(root))


# Finding the maximum depth of binary tree
def maxDepth(node):
    if not node :
        return 0
    left_depth = maxDepth(node.left)
    right_depth = maxDepth(node.right)
    return max(left_depth, right_depth) + 1

# => test the maxDepth function
# print('maxDepth function : \n', maxDepth(root))


# check if a binary tree is Symmetric
def isSymmetric(node):
    if not node:
        return True 
    def ismirror(t1, t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        return (t1.val == t2.val) and ismirror(t1.left, t2.right) and ismirror(t1.right, t2.left)
    
    return ismirror(node.left, node.right)
# => test the isSymmetric function
root2 = CreateBinaryNode([1,2,2,3,4,4,3])  # create a symmetric binary tree
print('is symmetric : \n', isSymmetric(root2)) # test the function




