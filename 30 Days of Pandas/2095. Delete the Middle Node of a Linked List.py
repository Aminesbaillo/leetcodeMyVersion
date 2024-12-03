# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next :
            return None
        slow, fast = head, head
        prev = None
        while fast and fast.next :
            fast = fast.next.next
            prev = slow
            slow = slow.next

        print('prev:', prev.val )
        print('slow:', slow.val)
        prev.next = slow.next
        return head
    




# Helper functions to convert list to linked list and vice versa
def list_to_linkedlist(lst):
    dummy = ListNode()
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def linkedlist_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Test cases
solution = Solution()

# Example 1: [1, 3, 4, 7, 1, 2, 6]
head = list_to_linkedlist([1, 3, 4, 7, 1, 2, 6])
new_head = solution.deleteMiddle(head)
print(linkedlist_to_list(new_head))  # Expected: [1, 3, 4, 1, 2, 6]

# Example 2: [1, 2, 3, 4]
head = list_to_linkedlist([1, 2, 3, 4])
new_head = solution.deleteMiddle(head)
print(linkedlist_to_list(new_head))  # Expected: [1, 2, 4]

# Example 3: [2, 1]
head = list_to_linkedlist([2, 1])
new_head = solution.deleteMiddle(head)
print(linkedlist_to_list(new_head))  # Expected: [2]
