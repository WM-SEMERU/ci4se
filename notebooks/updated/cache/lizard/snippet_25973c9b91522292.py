def remove(self, data):
    current_node = self._first_node
    deleted = False
    if self._size == 0:
        return
    if data == current_node.data():
        if current_node.next() is None:
            self._first_node = LinkedListNode(None, None)
            self._last_node = self._first_node
            self._size = 0
            return
        current_node = current_node.next()
        self._first_node = current_node
        self._size -= 1
        return
    while True:
        if current_node is None:
            deleted = False
            break
        next_node = current_node.next()
        if next_node is not None:
            if data == next_node.data():
                next_next_node = next_node.next()
                current_node.update_next(next_next_node)
                next_node = None
                deleted = True
                break
        current_node = current_node.next()
    if deleted:
        self._size -= 1