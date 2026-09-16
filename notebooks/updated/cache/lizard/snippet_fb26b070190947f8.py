def is_contradictory(self, other):
    other = self.coerce(other)
    to_i = self.to_i
    assert to_i(other.low) <= to_i(other.high), 'Low must be <= high'
    if max(map(to_i, [other.low, self.low])) <= min(map(to_i, [other.high,
        self.high])):
        return False
    else:
        return True