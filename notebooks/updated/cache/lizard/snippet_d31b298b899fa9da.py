def _conditional_toward_zero(method, sign):
    return (method is RoundingMethods.ROUND_HALF_ZERO or method is
        RoundingMethods.ROUND_HALF_DOWN and sign == 1 or method is
        RoundingMethods.ROUND_HALF_UP and sign == -1)