def _transformBy(self, matrix, **kwargs):
    t = transform.Transform(*matrix)
    x, y = t.transformPoint((self.x, self.y))
    self.x = x
    self.y = y