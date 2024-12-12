# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def creatBST(arr):
    if not arr:
        return None
    root = TreeNode(arr[0])
    queue = [root]
    i = 1 
    while i < len(arr):
        node = queue.pop(0)
        if  arr[i] is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1
    return root

root = creatBST([5,3,6,2,4,None,7])
class Solution(object):
    def findMin(self, node):
        # Debug: We are finding the minimum value in this subtree
        print(f"    findMin: Entering subtree rooted at {node.val} to find min.")
        while node.left:
            print(f"    findMin: Moving left from {node.val} to {node.left.val}")
            node = node.left
        print(f"    findMin: Found min node with value {node.val}")
        return node
    def deleteNode(self, root, key):
            if root :
                print(f"\ndeleteNode: At node {root.val}, looking for key {key}.")
            else:
                print(f"\ndeleteNode: Reached a null subtree while looking for key {key}. Returning None.")
                return None

            if key < root.val:
                print(f"  Key {key} < {root.val}, so move to the left subtree.")
                root.left = self.deleteNode(root.left, key)
            elif key > root.val:
                # Debug: Key is greater, go to right subtree
                print(f"  Key {key} > {root.val}, so move to the right subtree.")
                root.right = self.deleteNode(root.right, key)
            else:
                # Debug: Found the node to delete
                print(f"  Found the node {root.val} to delete.")

                # Case 1: Node has no left child
                if root.left is None:
                    print(f"  Node {root.val} has no left child, replacing it with its right child.")
                    return root.right

                # Case 2: Node has no right child
                elif root.right is None:
                    print(f"  Node {root.val} has no right child, replacing it with its left child.")
                    return root.left

                # Case 3: Node has two children
                else:
                    print(f"  Node {root.val} has two children. Finding its inorder successor.")
                    successor = self.findMin(root.right)
                    print(f"  Inorder successor is {successor.val}. Replacing {root.val}'s value with {successor.val}.")
                    root.val = successor.val
                    print(f"  Deleting the inorder successor {successor.val} from the right subtree.")
                    root.right = self.deleteNode(root.right, successor.val)
            return root
    
# test the function 

s = Solution()
print(s.deleteNode(root, 3))

def node_to_list(root):
    if not root:
        return []
    queue = [root]
    result = []
    while queue:
        node = queue.pop(0)
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result

print(node_to_list(root))