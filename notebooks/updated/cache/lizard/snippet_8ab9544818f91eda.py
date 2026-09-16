def peek(self):
    if self.reading is None:
        raise StreamEmptyError(
            'peek called on virtual stream walker without any data',
            selector=self.selector)
    return self.reading