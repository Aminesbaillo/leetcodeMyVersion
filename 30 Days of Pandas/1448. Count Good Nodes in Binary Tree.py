class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def CreateBinaryTree(arr):
    if not arr:
        return None
    root = TreeNode(arr[0])
    node = [root]  # This holds the TreeNode objects, not values.
    idx = 1
    while idx < len(arr):
        d = node.pop(0)  # pop the first node in the list
        
        # Left child
        if arr[idx] is not None:
            d.left = TreeNode(arr[idx])
            node.append(d.left)  # append the left node (TreeNode)
        idx += 1
        
        # Right child
        if idx < len(arr) and arr[idx] is not None:
            d.right = TreeNode(arr[idx])
            node.append(d.right)  # append the right node (TreeNode)
        idx += 1

    return root

class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, maxVal):
            if not node:
                return 0
            good = 1 if node.val >= maxVal else 0
            maxVal = max(node.val, maxVal)
            good += dfs(node.left, maxVal)
            good += dfs(node.right, maxVal)

            return good
    
        return dfs(root, root.val)

# Test the solution
sol = Solution()
root = CreateBinaryTree([3,1,4,3,None,1,5])  # Use None for null values
print(sol.goodNodes(root))  # Expected output: 4
