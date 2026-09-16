def complement(self):
    if self.is_empty:
        return StridedInterval.top(self.bits)
    if self.is_top:
        return StridedInterval.empty(self.bits)
    y_plus_1 = StridedInterval._modular_add(self.upper_bound, 1, self.bits)
    x_minus_1 = StridedInterval._modular_sub(self.lower_bound, 1, self.bits)
    dist = StridedInterval._wrapped_cardinality(y_plus_1, x_minus_1, self.bits
        ) - 1
    if dist < 0:
        new_stride = 0
    elif self._stride == 0:
        new_stride = 1
    else:
        new_stride = fractions.gcd(self._stride, dist)
    return StridedInterval(lower_bound=y_plus_1, upper_bound=x_minus_1,
        bits=self.bits, stride=new_stride, uninitialized=self.uninitialized)