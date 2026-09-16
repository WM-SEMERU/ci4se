def map(self, f, preservesPartitioning=False):

    def func(iterator):
        return map(f, iterator)
    return self.mapPartitions(func, preservesPartitioning)