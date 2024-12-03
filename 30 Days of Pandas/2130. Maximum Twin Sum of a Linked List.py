# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



# Create Linked list 
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    prev = head 
    for ele in arr[1:]:
        current = ListNode(ele)
        prev.next = current
        prev = current
    return head


# solution 
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
         # twin sum is sum of zth and wth nodes where (z = n - w -1) where z and w are both in (0-indexed)

        if not head :
            return None 
        
        elif not head.next.next :
            return head.val + head.next.val
        stack = []
        slow = head
        fast = head
        max_twin = 0
        while fast and fast.next :
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        
        while slow :
            d = stack.pop()
            if abs(d + slow.val) > max_twin:
                max_twin = d + slow.val 
            slow = slow.next
        return max_twin

head = create_linked_list([47,22,81,46,94,95,90,22,55,91,6,83,49,65,10,32,41,26,83,99,14,85,42,99,89,69,30,92,32,74,9,81,5,9]) #[5, 4, 2, 1], 6)
Solution = Solution()
print(Solution.pairSum(head))   


# def test_solution():
#     test_cases = [
#         ([5, 4, 2, 1], 6),  # General Case 1
#         ([4, 2, 2, 3], 7),  # General Case 2
#         ([1, 100000], 100001),  # Minimum Length Case
#         ([5, 5, 5, 5], 10),  # All Nodes Equal
#         ([1, 3, 5, 7], 8),  # All Odd Numbers
#         ([2, 4, 6, 8], 10),  # All Even Numbers
#         ([-5, -4, -2, -1], -6),  # Negative Numbers
#         # ([i for i in range(1, 10001)], 10001),  # Large List Test (Performance)
#         ([10, 20, 30, 40], 50)  # Identical Pair Test
#     ]
    
#     for idx, (arr, expected) in enumerate(test_cases):
#         head = create_linked_list(arr)
#         solution = Solution()
#         result = solution.pairSum(head)
        
#         assert result == expected, f"Test case {idx + 1} failed: expected {expected}, got {result}"
    
#     print("All test cases passed!")

# # Run the test function
# test_solution()
