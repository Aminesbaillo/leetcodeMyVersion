# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# create binary tree :
def create_binary_tree(arr):
    if not arr: return None 

    root = TreeNode(arr[0])
    stack = [root]
    i = 1
    while i < len(arr):
        node = stack.pop(0)
        if arr[i]:
            node.left = TreeNode(arr[i])
            stack.append(node.left)
        i += 1
        if i < len(arr) and arr[i]:
            node.right = TreeNode(arr[i])
            stack.append(node.right)
        i += 1

    return root 
root = create_binary_tree([4,2,7,1,3])

# search in binary search tree
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """ 
        if not root : return None
        queue = [root]
        while queue :
            node = queue.pop(0)
            if node.val == val : return node
            if node.left : queue.append(node.left)
            if node.right : queue.append(node.right)
        return None

# test the solution 

print(Solution().searchBST(root, 2))