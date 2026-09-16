def startsafter(self, other):
    if self.is_valid_range(other):
        if self.lower == other.lower:
            return other.lower_inc or not self.lower_inc
        elif self.lower_inf:
            return False
        elif other.lower_inf:
            return True
        else:
            return self.lower > other.lower
    elif self.is_valid_scalar(other):
        return self.lower >= other
    else:
        raise TypeError("Unsupported type to test for starts after '{}'".
            format(other.__class__.__name__))