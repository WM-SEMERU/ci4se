def next(self):
    if self.r == self.repeats:
        self.i = (self.i + 1) % self.lenght
        self.r = 0
    self.r += 1
    if self.stopping and self.i == 0 and self.r == 1:
        self.stopped = True
    if self.i == 0 and self.stopped:
        raise StopIteration
    else:
        iterator = self.iterators[self.i]
        return iterator.next()