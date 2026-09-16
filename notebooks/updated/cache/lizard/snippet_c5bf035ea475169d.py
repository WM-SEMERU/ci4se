def remove_last(self):
    if self.length() <= 1:
        self.head = None
        return True
    node = self.head
    while node is not None:
        is_last_but_one = (node.next_node is not None and node.next_node.
            next_node is None)
        print(node.val, is_last_but_one)
        if is_last_but_one:
            node.next_node = None
            return True
        node = node.next_node
    return False