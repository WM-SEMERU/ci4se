def _lt_from_ge(self, other):
    op_result = self.__ge__(other)
    if op_result is NotImplemented:
        return NotImplemented
    return not op_result