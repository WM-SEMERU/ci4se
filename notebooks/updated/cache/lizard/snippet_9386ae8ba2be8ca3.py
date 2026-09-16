def broadcast_equals(self, other, equiv=duck_array_ops.array_equiv):
    try:
        self, other = broadcast_variables(self, other)
    except (ValueError, AttributeError):
        return False
    return self.equals(other, equiv=equiv)