def iteritems(self, pattern='*'):
    for key in self.keys(pattern):
        yield key, self[key]