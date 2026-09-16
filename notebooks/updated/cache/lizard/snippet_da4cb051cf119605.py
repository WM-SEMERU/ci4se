def mul(left, right):
    from .mv_mul import MvMul
    length = max(left, right)
    if length == 1:
        return Mul(left, right)
    return MvMul(left, right)