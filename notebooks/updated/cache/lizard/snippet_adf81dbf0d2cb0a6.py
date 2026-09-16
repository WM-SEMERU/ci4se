def order_by(self, *args, **kwds):
    self._order_by.order_by(*args, **kwds)
    return self