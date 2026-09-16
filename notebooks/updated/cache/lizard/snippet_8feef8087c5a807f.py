def filter(self, f):

    def func(iterator):
        return filter(f, iterator)
    return self.mapPartitions(func, True)