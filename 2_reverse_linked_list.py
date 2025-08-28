class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head):
    prev, curr = None, head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev, curr = curr, nxt
    return prev

if __name__ == "__main__":
    # Example: 1 -> 2 -> 3 -> None
    head = ListNode(1, ListNode(2, ListNode(3)))
    new_head = reverse_linked_list(head)
    while new_head:
        print(new_head.val, end=" -> ")
        new_head = new_head.next
