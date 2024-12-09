# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def CreateBinaryTree(arr):
    if not arr : return None
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
root = CreateBinaryTree([1,2,3,None,5,None,4])
       

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        
        This function returns the right-side view of a binary tree. 
        The "right-side view" is defined as what you would see if 
        you stood to the right of the tree and looked inwards: 
        essentially, for each level of the tree, we pick out the 
        rightmost node.
        """
        # Debug: Print the initial state
        print("Entering rightSideView with root:", root.val if root else None)

        # If root is None, there's no tree
        if not root: 
            print("The tree is empty. Returning None.")
            return None

        res = []             # This will hold the final right-side view.
        queue = [root]       # We use a queue to perform a level-order traversal (BFS).
        
        # Debug: Show the initial queue state
        print("Initial queue:", [node.val for node in queue])
        
        # While there are nodes to process in the queue
        while queue:
            # The number of nodes in the current level
            size_level = len(queue)
            # Debug: Print current level size and which nodes are in this level
            print("\nProcessing a new level. Current level size:", size_level)
            print("Current level nodes:", [node.val for node in queue])
            
            # Process each node of the current levelw
            for i in range(size_level):
                # Pop the front of the queue
                node = queue.pop(0)
                # Debug: Show which node is being processed
                print(f"Processing node {node.val} at position {i} in this level.")
                
                # If i == 0, this means this node is the first node we encountered at this level.
                # Because we enqueue right children before left children, the first node we pop at each level
                # (i == 0) will actually be the rightmost node when viewed from the right side.
                if i == 0:
                    # Debug: This is the node visible from the right side
                    print(f"Node {node.val} is the rightmost visible node at this level. Adding to res.")
                    res.append(node.val)
                
                # Enqueue the right child first
                if node.right:
                    print(f"Node {node.val} has a right child {node.right.val}. Adding it to the queue.")
                    queue.append(node.right)

                # Enqueue the left child next
                if node.left:
                    print(f"Node {node.val} has a left child {node.left.val}. Adding it to the queue.")
                    queue.append(node.left)
            
            # Debug: Show the queue after processing the current level
            print("Queue after processing this level:", [node.val for node in queue])
        
        # Debug: Finished processing all levels
        print("\nFinished processing all levels. The right-side view is:", res)
        return res

#test the function 

sol = Solution()
print(sol.rightSideView(root)) # Expected Output: [1, 3, 4, 5]


        