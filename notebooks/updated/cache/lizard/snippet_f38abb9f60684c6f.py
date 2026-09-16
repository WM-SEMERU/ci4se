def endsbefore(self, other):
    if self.is_valid_range(other):
        if self.upper == other.upper:
            return not self.upper_inc or other.upper_inc
        elif self.upper_inf:
            return False
        elif other.upper_inf:
            return True
        else:
            return self.upper <= other.upper
    elif self.is_valid_scalar(other):
        return self.upper <= other
    else:
        raise TypeError("Unsupported type to test for ends before '{}'".
            format(other.__class__.__name__))