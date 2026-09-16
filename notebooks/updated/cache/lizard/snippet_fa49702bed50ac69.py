def delete_from(self, basic_block):
    if basic_block is None:
        return
    if self.lock:
        return
    self.lock = True
    if self.prev is basic_block:
        if self.prev.next is self:
            self.prev.next = None
        self.prev = None
    for i in range(len(self.comes_from)):
        if self.comes_from[i] is basic_block:
            self.comes_from.pop(i)
            break
    self.lock = False