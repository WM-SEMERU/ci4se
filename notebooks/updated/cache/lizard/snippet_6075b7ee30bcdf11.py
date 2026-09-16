def is_contradictory(self, other):
    other = IntervalCell.coerce(other)
    assert other.low <= other.high, 'Low must be <= high'
    if max(other.low, self.low) <= min(other.high, self.high):
        return False
    else:
        return True