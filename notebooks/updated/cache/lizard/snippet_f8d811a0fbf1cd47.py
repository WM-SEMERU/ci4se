def set_attachments_order(self, order):
    if isinstance(order, basestring):
        new_order = self.storage.get('order', [])
        new_order.append(order)
        order = new_order
    self.storage.update({'order': order})