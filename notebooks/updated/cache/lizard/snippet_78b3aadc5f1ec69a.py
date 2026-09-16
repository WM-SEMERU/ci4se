def adjust(self, amount, update=True, flow=True, fee=0.0):
    self._capital += amount
    self._last_fee += fee
    if flow:
        self._net_flows += amount
    if update:
        self.root.stale = True