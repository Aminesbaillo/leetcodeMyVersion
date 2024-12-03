# 1 : Create ListNode class
class ListNode:
    """"
    ListNode class represent each Node in the linked list
    """
    def __init__(self, val = 0, next= None):
        self.val = val #store the value of the node
        self.next = next # pointer to the nexte node "default is None"



# test the function :: it's woork ^-^
#----------------------------------------------------------------
# node = ListNode(5)
# print(node.val)
#----------------------------------------------------------------


# 2 : Create a simple Linke List
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
    return head 

head = create_linked_list([1, 2, 3, 4, 5])


# 3 : print the linked lis :
def print_linked_list(head):
    current = head 
    arr = []
    while current:
        arr.append(current.val)
        current = current.next

    print(" -> ".join(map(str, arr)))


# print_linked_list(head)  # Expected output: 1 -> 2 -> 3 -> 4

# 4 : Implementation of oddEvenList Function 
def oddEvenList(head):
    if not head or not head.next:
        return None 
    odd = head
    even = head.next
    even_head = even
    
    while even and even.next:
        odd.next = odd.next.next
        even.next = even.next.next

        odd = odd.next
        even = even.next

    odd.next = even_head
    return head

# test the function 
reordered_head = oddEvenList(head)
print_linked_list(reordered_head)