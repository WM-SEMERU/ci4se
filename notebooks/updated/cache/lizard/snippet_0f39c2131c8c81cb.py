def orders(self):
    self.account.refresh()
    return [o for o in self.account.openorders if self.bot['market'] == o.
        market and self.account.openorders]