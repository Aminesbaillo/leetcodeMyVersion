# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def CreateBinaryTree(arr):
    if not arr:
        return None
    
    root = TreeNode(arr[0]) 
    queue = [root]
    i = 1
    while i < len(arr):
        node = queue.pop(0)
        
        if arr[i] is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        
        if i+1 < len(arr) and arr[i+1] is not None:
            node.right = TreeNode(arr[i+1])
            queue.append(node.right)
        
        i += 2
    return root 
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        res = [(-float('inf'), 0)]
        queue = [root]
        level = 0 
        while queue:
            cuurent_sum = 0
            size_level = len(queue)
            level += 1
            for i in range(size_level):
                node = queue.pop(0)
                cuurent_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if cuurent_sum > res[0][0]:
                res.pop(0)
                res.append((cuurent_sum, level))
        
        return res[0][1]
    
# test the function 
root = CreateBinaryTree([989,None,10250,98693,-89388,None,None,None,-32127])

sol = Solution()
print(sol.maxLevelSum(root))