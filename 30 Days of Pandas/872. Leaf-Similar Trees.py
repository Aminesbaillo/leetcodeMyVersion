class TreeNode(object):
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
def CreateBinaryTree(lst):
    if not lst:
        return None
    root = TreeNode(lst[0])
    queue = [root]
    idx = 1
    while idx < len(lst):
        node = queue.pop(0)
        if lst[idx]:
            node.left = TreeNode(lst[idx])
            queue.append(node.left)
        idx += 1
        if lst[idx]:
            node.right = TreeNode(lst[idx])
            queue.append(node.right)
        idx += 1
    return root


class Solution(object):
    def LeafSimilar(self, root1, root2):
        def getLeavesSequence(root):
            leaves = []
            def dfs(node):
                if not node:
                    return
                if not node.left and not node.right:
                    leaves.append(node.val)
                dfs(node.left)
                dfs(node.right) 
            dfs(root)
            return leaves
        return getLeavesSequence(root1) == getLeavesSequence(root2)
    
# test the solution :
sol = Solution()

root1 = CreateBinaryTree([3,5,1,6,2,9,8,None,None,7,4])
root2 = CreateBinaryTree([3,5,1,6,7,4,2,None,None,None,None,None,None,9,8])
print(sol.LeafSimilar(root1, root2))