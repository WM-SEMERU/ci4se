def solution(self, b):
    if isinstance(b, numbers.Number):
        b = StridedInterval(lower_bound=b, upper_bound=b, stride=0, bits=
            self.bits)
    else:
        raise ClaripyOperationError(
            'Oops, Strided intervals cannot be passed as "parameter to function solution. To implement'
            )
    if self.intersection(b).is_empty:
        return False
    return True