def ints(self, qlist):
    m, n, t = self.args
    return (((n * i + j) * 2 + u) * t + k for i, j, u, k in qlist)