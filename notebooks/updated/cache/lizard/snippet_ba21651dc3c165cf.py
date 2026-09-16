def is_dtype_equal(self, other):
    try:
        return hash(self.dtype) == hash(other.dtype)
    except (AttributeError, TypeError):
        return False