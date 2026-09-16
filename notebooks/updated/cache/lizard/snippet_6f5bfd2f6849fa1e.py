def next(self):
    if self.index < self.length:
        index = self.index
        self.index += 1
        return self.data[index]
    else:
        raise StopIteration()