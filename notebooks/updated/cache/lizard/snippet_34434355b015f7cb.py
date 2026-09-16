def foreach(self, f):
    f = fail_on_stopiteration(f)

    def processPartition(iterator):
        for x in iterator:
            f(x)
        return iter([])
    self.mapPartitions(processPartition).count()