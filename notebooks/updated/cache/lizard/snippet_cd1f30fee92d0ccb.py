def register(self, func, order):
    token = self.Token()
    self._filter_order.append((order, token, func))
    self._filter_order.sort(key=lambda x: x[0])
    return token