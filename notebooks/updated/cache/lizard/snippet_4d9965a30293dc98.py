def order(self, order):
    order = order if isinstance(order, Order) else Order(order)
    order.object_getattr = self.object_getattr
    self.orders.append(order)
    return self