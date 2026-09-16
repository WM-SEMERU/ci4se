def add_moveTo(self, x, y):
    moveTo = self._add_moveTo()
    pt = moveTo._add_pt()
    pt.x, pt.y = x, y
    return moveTo