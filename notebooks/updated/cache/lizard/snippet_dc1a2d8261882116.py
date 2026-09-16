def sell(self, quantity, **kwargs):
    self.parent.order('SELL', self, quantity=quantity, **kwargs)