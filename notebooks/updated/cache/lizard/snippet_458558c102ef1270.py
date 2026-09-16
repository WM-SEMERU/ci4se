def observe(self, amount):
    self._count.inc(1)
    self._sum.inc(amount)