 
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Function to construct a binary tree from a given array 
def CreateBinaryTree(arr):
    if not arr:
        return None
    root = TreeNode(arr[0])
    queue = [root]
    i = 1
    while i < len(arr):
        node = queue.pop(0)
        if arr[i] :
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1
        if i < len(arr) and arr[i]:
            node.right = TreeNode(arr[i])
            queue.append(node.right)

        i += 1
    return root

# root = CreateBinaryTree([1,None,1,1,1,None,None,1,1,None,1,None,None,None,1])
root =  CreateBinaryTree([1,1,1,None,1,None,None,1,1,None,1])
# Longest ZigZag Path in a Binary Tree
class Solution(object):
    def longestZigZag(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        return max(self.helpers(root.left, True, 0), self.helpers(root.right, False, 0))

    def helpers(self, node, isleft, depth):
        if not node : return depth

        if isleft:
            depth = max(
                depth, 
                self.helpers(node.right, False, depth + 1),
                self.helpers(node.left, True, 0)
                )
        else : # we previously went through left
           depth = max(
               depth, 
               self.helpers(node.left, True, depth + 1),
               self.helpers(node.right, False, 0)
               )

        return depth 

# Test the Solution
sol = Solution()
print(sol.longestZigZag(root))
