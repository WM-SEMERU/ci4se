def adjacent(self, other):
    if not self.is_valid_range(other):
        raise TypeError(
            "Unsupported type to test for inclusion '{0.__class__.__name__}'"
            .format(other))
    elif not self or not other:
        return False
    return (self.lower == other.upper and self.lower_inc != other.upper_inc or
        self.upper == other.lower and self.upper_inc != other.lower_inc)