def peek(self, default=None):
    try:
        result = self.pointer.next()
        self.pointer = itertools.chain([result], self.pointer)
        return result
    except StopIteration:
        return default