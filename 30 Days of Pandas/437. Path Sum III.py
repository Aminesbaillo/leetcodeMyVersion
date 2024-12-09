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


root = CreateBinaryTree([1,2,3,4,1,2,3])

class Solution(object):
    def pathSum(self, root: TreeNode, sum: int) -> int:
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        # Helper function that will recursively traverse the tree
        def DFS(node, prev_sum):
            
            if not node:
                return

            # Debug print: Print the current node and its value
            print(f"Visiting Node: {node.val}")

            # Current sum is the sum from root to the current node
            # prev_sum is the sum up to the parent node, and we add current node's value to it
            current_sum = prev_sum + node.val
            print(f"Current Sum (prev_sum + node.val): {prev_sum} + {node.val} = {current_sum}")

            # Calculate the difference to find a valid path
            diff = current_sum - sum
            print(f"Difference (current_sum - target): {current_sum} - {sum} = {diff}")

            # If the difference exists in the frequency map, it means we've found a valid path
            if diff in freq:
                self.count += freq[diff]
                print(f"Found a valid path: diff = {diff} exists in freq. Count is now: {self.count}")

            # Update the frequency map with the current sum
            if current_sum in freq:
                freq[current_sum] += 1
            else:
                freq[current_sum] = 1
            print(f"Updated frequency map: {freq}")

            # Traverse the left and right children (DFS recursion)
            print("Traversing Left Child")
            DFS(node.left, current_sum)
            print("Traversing Right Child")
            DFS(node.right, current_sum)

            # Backtrack: remove the current sum from the frequency map (we're done with this path)
            freq[current_sum] -= 1
            print(f"Backtracking: Decreased count of current_sum in freq. New freq: {freq}")

        # Initialize the count variable to track valid paths
        self.count = 0

        # Initialize frequency map. It starts with {0: 1} because there is one way to reach sum = 0 (the empty path)
        freq = {0: 1}

        # Start DFS traversal from the root node with initial sum 0
        DFS(root, 0)

        # Return the total count of valid paths
        return self.count

#test the solution 
sol = Solution()
# root = CreateBinaryTree([10,5,-3,3,2,None,11,3,-2,None,1])
print(sol.pathSum(root, 6))