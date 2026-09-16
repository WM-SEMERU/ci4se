def order(self, order=None):
    if order is None:
        return int(self.url.order)
    self.url.order = str(order)