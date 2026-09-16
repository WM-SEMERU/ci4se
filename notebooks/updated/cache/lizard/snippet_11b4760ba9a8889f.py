def shift(self, x):
    for i in xrange(len(self)):
        self[i] = self[i].shift(x)
    return self