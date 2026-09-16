def tail(self, n=5):
    return MultiIndex([v.tail(n) for v in self.values], self.names)