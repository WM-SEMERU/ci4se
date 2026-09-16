def delta(self, local=False):
    s, e = self.get(local)
    return e - s