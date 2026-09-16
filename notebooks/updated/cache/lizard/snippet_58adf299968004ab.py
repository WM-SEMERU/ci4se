def concat(self, one, two):
    if not len(one) == len(two) == 6:
        raise ValueError('bad sequ. length')
    self.a, self.b, self.c, self.d, self.e, self.f = TOOLS._concat_matrix(one,
        two)
    return self