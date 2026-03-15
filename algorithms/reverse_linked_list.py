# Reverse a Linked List - LeetCode #206
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

def list_to_array(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

nodes = [ListNode(i) for i in range(1, 6)]
for i in range(len(nodes) - 1):
    nodes[i].next = nodes[i + 1]

reversed_head = reverse_list(nodes[0])
print(list_to_array(reversed_head))  # [5, 4, 3, 2, 1]
