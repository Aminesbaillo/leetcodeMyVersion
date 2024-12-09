#  Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Create a binary tree from a list:
def create_binary_tree(lst):
    if not list :
        return None
    root = TreeNode(lst[0])
    queue = [root]
    idx = 1
    while idx < len(lst):
        node = queue.pop(0)
        if lst[idx] :
            node.left = TreeNode(lst[idx])
            queue.append(node.left)
        idx += 1
        if lst[idx] :
            node.right = TreeNode(lst[idx])
            queue.append(node.right)
        idx += 1

    return root



class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return max(left_depth, right_depth) + 1


# test the Solution 
# test the function
sol = Solution()
# test the function
lst = [3,9,20,None,None,15,7]
root = create_binary_tree(lst)
print(sol.maxDepth(root))

