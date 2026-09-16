def _call(self, x, out=None):
    if out is None:
        return self.operator(x * self.vector)
    else:
        tmp = self.domain.element()
        x.multiply(self.vector, out=tmp)
        self.operator(tmp, out=out)