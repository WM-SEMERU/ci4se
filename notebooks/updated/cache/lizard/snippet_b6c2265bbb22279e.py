def init(self, single=None, swallow_exceptions=True):
    for d in self.disks:
        for v in d.init(single, swallow_exceptions=swallow_exceptions):
            yield v