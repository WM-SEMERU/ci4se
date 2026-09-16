def peek_many(self, n):
    if n == 0:
        return []
    elif n == 1:
        return [self.peek()]
    else:
        items = list(self.pop_many(n))
        self.update(items)
        return items