def rotate_right(head, k):
    if not head or not head.next:
        return head
    current = head
    length = 1
    while current.next:
        current = current.next
        length += 1
    current.next = head
    k = k % length
    for i in range(length - k):
        current = current.next
    head = current.next
    current.next = None
    return head