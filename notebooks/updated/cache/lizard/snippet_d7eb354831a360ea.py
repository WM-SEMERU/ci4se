def widen(self, other):
    if self.low < other.low:
        low = -float('inf')
    else:
        low = self.low
    if self.high > other.high:
        high = float('inf')
    else:
        high = self.high
    return Interval(low, high)