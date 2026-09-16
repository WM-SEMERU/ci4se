def remove(self, position):
    if position <= 0:
        return self.remove_first()
    if position >= self.length() - 1:
        return self.remove_last()
    counter = 0
    last_node = self.head
    current_node = self.head
    while current_node is not None and counter <= position:
        if counter == position:
            last_node.next_node = current_node.next_node
            return True
        last_node = current_node
        current_node = current_node.next_node
        counter += 1
    return False