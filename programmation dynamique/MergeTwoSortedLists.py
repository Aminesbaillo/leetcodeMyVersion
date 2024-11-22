# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        current = dummy 
        while list1 and list2 :
            if list1.val < list2.val :
                current.next = list1
                list1 = list1.next
            else : 
                current.next = list2
                list2 = list2.next
            current = current.next
        if not list1: 
            current.next= list2
        else :
            current.next = list1
        return dummy.next

# Helper function to convert a Python list to a ListNode
def list_to_linked_list(lst):
    dummy = ListNode()
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Helper function to convert a ListNode to a Python list
def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Create instances of ListNode from the input lists
list1 = list_to_linked_list([1, 2, 4])
list2 = list_to_linked_list([1, 3, 4])

# Create a Solution object
solution = Solution()

# Call the mergeTwoLists function with ListNode instances
merged_list = solution.mergeTwoLists(list1, list2)

# Output the merged list
print(linked_list_to_list(merged_list))
