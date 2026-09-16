def mcons(self, iterable):
    head = self
    for elem in iterable:
        head = head.cons(elem)
    return head