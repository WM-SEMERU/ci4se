def group(self):
    yield self.current
    for num, item in enumerate(self.iterator, 1):
        self.current = item
        if num == self.limit:
            break
        yield item
    else:
        self.on_going = False