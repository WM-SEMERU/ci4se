def lookup(self, tmp):
    if tmp < 0 or tmp > self.types_used:
        l.debug('Invalid temporary number %d', tmp)
        raise IndexError(tmp)
    return self.types[tmp]