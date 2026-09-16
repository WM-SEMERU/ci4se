def bpopmin(self, timeout=0):
    res = self.database.bzpopmin(self.key, timeout)
    if res is not None:
        return res[1], res[2]