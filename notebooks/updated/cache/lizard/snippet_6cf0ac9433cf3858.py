def avg(self, func=lambda x: x):
    count = self.count()
    if count == 0:
        raise NoElementsError('Iterable contains no elements')
    return float(self.sum(func)) / float(count)