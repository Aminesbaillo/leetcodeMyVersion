class TreeNode(object):
    def __init__(self, val= 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def CreateBinaryTree(arr):
    if not arr: return

    root = TreeNode(arr[0])
    q = [root]
    i = 1
    while i < len(arr):
        node = q.pop(0)
        if arr[i]:
            node.left = TreeNode(arr[i])
            q.append(node.left)
        i += 1
        if i < len(arr) and arr[i]:
            node.right = TreeNode(arr[i])
            q.append(node.right)
        i += 1
    return root



#create a root node
root = CreateBinaryTree([3,5,1,6,2,0,8,None,None,7,4])
p = TreeNode(5)
q = TreeNode(1)
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root : return None
        if root == p or root == q: return root.val
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        if l and r : return root.val

        else : return l if l else r
# test the solution :
sol = Solution()
print(sol.lowestCommonAncestor(root, p, q))