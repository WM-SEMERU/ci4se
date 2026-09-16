def tuples(self, rlist):
    m, n, t = self.args
    for r in rlist:
        r, k = divmod(r, t)
        r, u = divmod(r, 2)
        i, j = divmod(r, n)
        yield i, j, u, k